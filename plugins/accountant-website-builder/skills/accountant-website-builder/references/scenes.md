# Building a stage scene

A scene is a background **plate** plus one or more animated **layers** cut out of the same image, positioned in % of a 16:9 frame. The plate fills the hero (it's cropped like `object-fit: cover`); the layers sit above it and move.

## The `scene` object in brief.json

| Field | What it is |
|---|---|
| `plate` | Background image with the object removed |
| `layers` | List of `{src, left, top, width, motion, shine}`. `left`/`top`/`width` are % of the 16:9 frame, taken from where the object sat in the original image |
| `coins` | Optional coin rain: `{src, items: [[left%, top%, width%, fall s, delay s, blur px, spin s, tilt deg, sway vw, rotate deg], ...]}`. Each coin spins in 3D with real thickness |
| `wings` | Optional flapping object split down the middle: `{l, r, left, top, width, aspect}` |
| `particles` | `petals`, `gold`, `sparkle`, `receipts`, `mist` or `dust` |
| `colors` | Particle colours |
| `echo` | Giant word behind the object (the town works well) |
| `shade` | Colour the left of the hero fades to, so the headline reads |
| `glass` | Background of the info panel |
| `panel`, `panel_title` | Three `[label, value]` rows for the glass panel (true promises only) |

## Motion types
- `glide`: slow banking flight (birds, cranes, paper planes)
- `hover`: fast buzz with a wing-blur ghost (hummingbirds, drones)
- `float`: weightless bob and tilt, staggered when there are several (parcels, cards, devices)
- `rock`: rocking on water with a reflection and ripples (boats)
- `flow`: breathing glow and scale (ribbons, liquid metal)
- `shine: true` adds a light sweep across the object's surface (metal and glass)

## Making a new scene
1. **Still:** an image model at 16:9, e.g. "Ultra-premium cinematic 3D product render for a website hero, photoreal materials, soft global illumination, generous empty space on the left for a headline. [ONE finance object and what it's made of] on the right side of the frame. Background: [colour]. Absolutely no words, letters, numbers, logos, currency symbols or real banknote designs."
2. **Cut-out:** remove the background (Apple Vision, remove.bg or similar), keep the full frame size, then trim to the object and note its left/top/width as % of the frame.
3. **Plate:** ask the model to edit the still: "Remove [the object] completely and fill the area with the background exactly as it would look, matching lighting and grain. Change nothing else."
4. **Coins or flapping objects:** generate the object alone, face-on and symmetric, on a plain background.

Good finance objects: coins, a crane or plane folded from security-pattern paper, a gold bird, glass parcels (e-commerce), a paper boat made from a tax form, a chrome ribbon (payroll), glass blocks stacking (growth), a key (onboarding). Avoid stock clichés: handshakes, calculators, piggy banks.
