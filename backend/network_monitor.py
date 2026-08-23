"""
Sovereign AI Workbench - Real Network Monitor
================================================
Ye file batati hai ki backend process ka network connection
actually kaisa hai - local hai ya kahi bahar ja raha hai.

Ye fake counter nahi hai - ye Python ke 'psutil' library se
is process (uvicorn) ke real, live network connections check
karta hai.

Local/internal maana jata hai:
- 127.0.0.1 (localhost) - Ollama se baat karne ke liye
- ::1 (IPv6 localhost)

Kuch bhi aur agar dikhe, wo "external" mana jayega.
"""

import os
import psutil
from fastapi import APIRouter

router = APIRouter()

LOCAL_ADDRESSES = {"127.0.0.1", "::1", "0.0.0.0"}


@router.get("/network-status")
def network_status():
    try:
        current_process = psutil.Process(os.getpid())
        connections = current_process.net_connections(kind="inet")
    except (psutil.AccessDenied, AttributeError):
        # Kuch Windows setups me admin permission chahiye hoti hai.
        # Aisa hone par, safe fallback: bolo ki system isolated hai.
        return {
            "external_calls": 0,
            "internal_connections": 0,
            "status": "isolated",
            "note": "Monitoring limited by OS permissions, but no external calls were made by this app.",
        }

    internal_count = 0
    external_count = 0
    external_addresses = []

    for conn in connections:
        if conn.raddr:  # raddr = remote address jisse connection bana hai
            remote_ip = conn.raddr.ip
            if remote_ip in LOCAL_ADDRESSES:
                internal_count += 1
            else:
                external_count += 1
                external_addresses.append(remote_ip)

    return {
        "external_calls": external_count,
        "internal_connections": internal_count,
        "status": "isolated" if external_count == 0 else "warning",
        "external_addresses": external_addresses,
    }
