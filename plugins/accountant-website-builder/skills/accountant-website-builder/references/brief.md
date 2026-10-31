# brief.json fields

Copy the closest file in `../examples/` and edit it. Every field is required unless marked optional.

| Field | What it is | Example |
|---|---|---|
| `slug` | Folder-safe name | `fenwick-lowe` |
| `name` | Firm name. Use `&amp;` for & | `Fenwick &amp; Lowe` |
| `service` | The service people search for | `Accountants` |
| `town` | Town, city or county | `Bristol` |
| `title` (optional) | Page title, 65 characters max. Defaults to "[service] in [town] \| [name]" | |
| `tag` (optional) | Small text next to the logo. Defaults to "[service], [town]" | `Chartered accountants, Bristol` |
| `variant` | Layout: `stage` (default), `split`, `card` or `full` (see layouts.md) | `stage` |
| `theme` | `light` or `dark` (sets the nav style) | `light` |
| `scene` | The animated hero scene, see scenes.md | |
| `video`, `second` | Hero media and second-section media: a video or image path/URL, or `null` for the animated gradient | `null` |
| `glow` | Three colours for the gradient | `["#8B78D8","#E7B8D6","#C9BDF2"]` |
| `bg`, `ink`, `muted`, `accent`, `card`, `cardInk` | Page background, text, secondary text, accent, card background, card text | |
| `display`, `body` | Google Fonts names for headings and body | `Fraunces`, `Inter` |
| `dweight`, `dstyle` | Heading weight and extra CSS (letter-spacing) | `400`, `letter-spacing:-0.035em;` |
| `eyebrow` | Short line above the H1: who you help | `Accountants for owner-managed businesses` |
| `h1` | Service + town + a human promise. `<br>` allowed | `Accountants in Bristol,<br>finally on your side.` |
| `sub` | 120 to 165 characters. Doubles as the meta description | |
| `cta`, `cta2` | Main button (one action) and a secondary link | `Get a fixed quote`, `See our prices` |
| `nav` | Four menu items | |
| `marquee` | Six or seven services for the moving strip | |
| `stats` | Three `[number, label, suffix]` promises the firm keeps. No invented results | `["48", "hour reply promise", "h"]` |
| `services` | Three `[title, description]` cards | |
| `steps` | Three `[title, description]` steps to get started | |
| `closer` | Last big line before the final button | |
| `float` (optional) | Floating card on the split layout: `[title, detail]` | `["Next check-in", "Tuesday, 10:30"]` |
