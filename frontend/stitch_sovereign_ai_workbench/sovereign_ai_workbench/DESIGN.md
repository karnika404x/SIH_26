---
name: Sovereign AI Workbench
colors:
  surface: '#0b1326'
  surface-dim: '#0b1326'
  surface-bright: '#31394d'
  surface-container-lowest: '#060e20'
  surface-container-low: '#131b2e'
  surface-container: '#171f33'
  surface-container-high: '#222a3d'
  surface-container-highest: '#2d3449'
  on-surface: '#dae2fd'
  on-surface-variant: '#c6c6cd'
  inverse-surface: '#dae2fd'
  inverse-on-surface: '#283044'
  outline: '#909097'
  outline-variant: '#45464d'
  surface-tint: '#bec6e0'
  primary: '#bec6e0'
  on-primary: '#283044'
  primary-container: '#0f172a'
  on-primary-container: '#798098'
  inverse-primary: '#565e74'
  secondary: '#b9c7df'
  on-secondary: '#233144'
  secondary-container: '#3c4a5e'
  on-secondary-container: '#abb9d1'
  tertiary: '#7bd1fa'
  on-tertiary: '#003547'
  tertiary-container: '#001a25'
  on-tertiary-container: '#288ab0'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dae2fd'
  primary-fixed-dim: '#bec6e0'
  on-primary-fixed: '#131b2e'
  on-primary-fixed-variant: '#3f465c'
  secondary-fixed: '#d5e3fc'
  secondary-fixed-dim: '#b9c7df'
  on-secondary-fixed: '#0d1c2e'
  on-secondary-fixed-variant: '#3a485b'
  tertiary-fixed: '#c0e8ff'
  tertiary-fixed-dim: '#7bd1fa'
  on-tertiary-fixed: '#001e2b'
  on-tertiary-fixed-variant: '#004d66'
  background: '#0b1326'
  on-background: '#dae2fd'
  surface-variant: '#2d3449'
  status-success: '#22c55e'
  status-error: '#ef4444'
  status-warning: '#f59e0b'
  border-muted: '#1e293b'
  surface-elevated: '#1e293b'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-md:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
  mono-label:
    fontFamily: monospace
    fontSize: 13px
    fontWeight: '400'
    lineHeight: '1'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 24px
  margin-desktop: 40px
  margin-mobile: 16px
  container-max: 1440px
---

## Brand & Style

The design system is engineered for the **Sovereign AI Workbench**, a high-stakes environment where security, functional clarity, and industrial reliability are paramount. Moving away from ephemeral aesthetics, this system adopts a **"Secure Ops Console"** approach. It is designed to evoke a sense of absolute control and structural integrity, shifting from the translucency of the inspiration toward solid, authoritative surfaces.

The visual identity is rooted in **Corporate Minimalism** with a technical, industrial edge. It prioritizes information density and utilitarian precision, ensuring that AI-driven data and system controls are presented with maximum legibility and zero distraction. The interface feels less like a website and more like a hardened digital tool.

## Colors

The palette is strictly functional, utilizing a deep navy foundation to reduce eye strain during prolonged operational sessions.

- **Primary & Background:** The seed color `#0f172a` serves as the bedrock. It is used for the base canvas and primary structural blocks, creating a unified, solid environment.
- **Secondary (Steel):** `#475569` is used for non-interactive structural elements, secondary text, and inactive iconography. It provides the "industrial steel" feel of the workbench.
- **Tertiary (Ice Blue):** `#7dd3fc` is the interactive catalyst. This color is reserved for primary actions, focus states, and active indicators to ensure they are immediately identifiable against the dark base.
- **Functional Accents:** A specialized Success Green (`#22c55e`) is used for system-ready states and confirmed operations, maintaining high contrast for critical status updates.

## Typography

The system utilizes **Inter** across all roles to maintain a neutral, systematic, and utilitarian appearance. 

- **Clarity First:** Headline weights are kept at Semibold (`600`) or Bold (`700`) to provide a clear hierarchy against the solid background panels.
- **Information Density:** Body text uses a standard 16px size for general reading, but falls back to 14px for data-heavy dashboard modules.
- **Technical Accents:** Labels use uppercase styling with increased letter spacing to differentiate metadata from content. For system logs or AI-generated tokens, a monospaced font is permitted to emphasize the technical nature of the output.

## Layout & Spacing

This design system employs a **Fixed-Fluid Hybrid Grid**. The content is housed within a maximum 1440px container for desktop to maintain scan-line efficiency.

- **Grid:** A 12-column grid system is used for desktop, 8-column for tablet, and 4-column for mobile.
- **Rhythm:** A 4px baseline grid ensures vertical consistency. Layout margins are generous (40px) to provide "breathing room" in otherwise high-density data views, while internal component padding is tight (8px-16px) to maximize on-screen information.
- **Reflow:** On mobile, complex sidebars collapse into a drawer, and multi-column data tables pivot to card-based stacks to ensure operational capability remains intact.

## Elevation & Depth

In accordance with the "Secure Ops" aesthetic, depth is communicated through **Tonal Layering** and **Structural Outlines** rather than soft shadows.

- **Level 0 (Base):** The core background (`#0f172a`).
- **Level 1 (Panels):** Raised surfaces use a slightly lighter hex (`#1e293b`) with a solid 1px border (`#334155`).
- **Level 2 (Popovers/Modals):** These use the same Level 1 fill but add a crisp, low-spread shadow (`0 4px 6px -1px rgba(0, 0, 0, 0.5)`) to clearly separate the element from the panel below.
- **No Translucency:** All surfaces are 100% opaque. This ensures maximum text contrast and a feeling of "hardware" stability.

## Shapes

The shape language is conservative and architectural. 

- **Primary Radius:** A consistent `0.25rem` (4px) radius is applied to buttons, input fields, and small containers. This provides just enough softness to feel modern while maintaining the "sharp" industrial tone.
- **Structural Elements:** Large dashboard panels or layout containers use the same 4px radius. 
- **Exceptions:** Status dots and small avatars may use a circular (pill) shape to distinguish them from functional interface controls.

## Components

### Buttons
- **Primary:** Solid Ice Blue (`#7dd3fc`) fill with dark text. No gradient.
- **Secondary:** Transparent fill with a 1px Steel Blue (`#475569`) border.
- **States:** Hover states should involve a simple brightness shift (10%) rather than a color change.

### Inputs & Form Fields
- **Background:** Solid dark navy, 1px border in `#334155`.
- **Focus:** The border changes to Ice Blue (`#7dd3fc`) with a subtle 2px outer glow in the same color (10% opacity).
- **Labels:** Always placed above the field in the `label-md` typographic style.

### Cards & Panels
- **Container:** Solid `#1e293b` fill.
- **Header:** Panels should include a distinct header area separated by a 1px horizontal rule to organize metadata and actions.

### Chips & Tags
- Used for status and filtering. These should have a subtle background (`#0f172a`) and a border matching their status color (e.g., Green for "Success").

### Data Tables
- High density is preferred. Rows should be separated by 1px solid lines (`#1e293b`). Hover states on rows should use a subtle background highlight to aid eye-tracking.