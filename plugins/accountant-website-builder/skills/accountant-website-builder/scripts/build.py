"""Render a cinematic, conversion-led website for an accountancy or bookkeeping firm from a brief.

Usage: python3 build.py brief.json out_dir/
The brief format is documented in references/brief.md. Writes out_dir/index.html and prints SEO checks.
HandL Agency, MIT licence.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from stage import STAGE_CSS, STAGE_JS, stage_hero  # noqa: E402

ARROW = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
MARK = '<svg viewBox="0 0 32 32" width="26" height="26" aria-hidden="true"><rect x="3" y="3" width="26" height="26" rx="8" fill="none" stroke="currentColor" stroke-width="2.4"/><path d="M10 20.5l4-5 3 3 5-7" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ICONS = [
    '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19V5M4 19h16M8 15l3-4 3 2 5-6"/></svg>',
    '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="8"/><path d="M12 8v4l3 2"/></svg>',
    '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 5h14v10H9l-4 4z"/></svg>',
]


def font_link(*fams):
    q = "&".join(f"family={f.replace(' ', '+')}:wght@300;400;500;600;700;800" for f in dict.fromkeys(fams))
    return f'<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?{q}&display=swap" rel="stylesheet">'


def video(src, cls, poster_dark=False):
    """Media slot: a video file/URL, an image, or None for the animated gradient (no stock media needed)."""
    if not src:
        return f'<div class="{cls} mesh" aria-hidden="true"><i></i><i></i><i></i></div>'
    if re.search(r"\.(png|jpe?g|webp|avif)$", src, re.I):
        return f'<img class="{cls}" src="{src}" alt="" loading="eager">'
    return f'<video class="{cls}" src="{src}" autoplay muted loop playsinline preload="auto"></video>'


def hero(s):
    v = s["variant"]
    btns = f'<div class="btns rise" style="--d:.5s"><a class="btn" href="#start">{s["cta"]}<span class="btn-dot">{ARROW}</span></a><a class="link" href="#prices">{s["cta2"]}</a></div>'
    words = f'<p class="eyebrow rise" style="--d:.05s">{s["eyebrow"]}</p><h1 class="display rise" style="--d:.15s">{s["h1"]}</h1><p class="sub rise" style="--d:.35s">{s["sub"]}</p>{btns}'
    if v == "stage":
        return stage_hero(s, words)
    if v == "card":
        return f'<section class="hero hero-card"><div class="hcard">{video(s["video"], "bgv")}<div class="hcard-shade"></div><div class="hcard-in">{words}</div><div class="chip rise" style="--d:.8s"><span class="pulse"></span>Taking new clients for November</div></div></section>'
    if v == "full":
        return f'<section class="hero hero-full">{video(s["video"], "bgv")}<div class="full-shade"></div><div class="full-in">{words}</div><div class="scroll-cue rise" style="--d:1s"><span></span>Scroll</div></section>'
    return f'<section class="hero hero-split"><div class="split-l">{words}<div class="mini-stats rise" style="--d:.7s">' + "".join(
        f'<div><b data-count="{st[0]}" data-suffix="{st[2] if len(st) > 2 else ""}">0</b><span>{st[1]}</span></div>' for st in s["stats"][:2]
    ) + f'</div></div><div class="split-r rise" style="--d:.25s">{video(s["video"], "bgv")}<div class="float-card"><span class="pulse"></span><div><b>{s.get("float", ("Next check-in", "Tuesday, 10:30"))[0]}</b><span>{s.get("float", ("Next check-in", "Tuesday, 10:30"))[1]}</span></div></div></div></section>'


def page(s):
    light = s.get("theme") != "dark" and s["variant"] != "full" and s["bg"].upper() not in ("#05070D",)
    nav_cls = "nav glass" if not light else "nav"
    marquee = "".join(f"<span>{m}</span><i></i>" for m in s["marquee"]) * 2
    stats = "".join(
        f'<div class="stat reveal"><b data-count="{st[0]}" data-suffix="{st[2] if len(st) > 2 else ""}">0</b><span>{st[1]}</span></div>' for st in s["stats"]
    )
    services = "".join(
        f'<article class="svc reveal" style="--d:{i * .08}s"><div class="svc-ico">{ICONS[i]}</div><h3>{t}</h3><p>{d}</p><span class="svc-more">Find out more {ARROW}</span></article>'
        for i, (t, d) in enumerate(s["services"])
    )
    steps = "".join(
        f'<li class="reveal" style="--d:{i * .1}s"><span class="n">0{i + 1}</span><div><h4>{t}</h4><p>{d}</p></div></li>' for i, (t, d) in enumerate(s["steps"])
    )
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{s['title']}</title>
<meta name="description" content="{s['sub']}">
{font_link(s['display'], s['body'])}
<style>
html,body{{background:{s['bg']};margin:0}}
:root{{--g1:{s['glow'][0]};--g2:{s['glow'][1]};--g3:{s['glow'][2]};--bg:{s['bg']};--ink:{s['ink']};--muted:{s['muted']};--accent:{s['accent']};--card:{s['card']};--cardInk:{s['cardInk']};--ease:cubic-bezier(.22,1,.36,1)}}
*{{box-sizing:border-box}}
body{{font-family:'{s['body']}',system-ui,sans-serif;color:var(--ink);-webkit-font-smoothing:antialiased;overflow-x:hidden}}
a{{color:inherit;text-decoration:none}}
.display{{font-family:'{s['display']}',serif;font-weight:{s['dweight']};{s['dstyle']}line-height:.98;margin:0}}
.wrap{{max-width:88rem;margin:0 auto;padding:0 clamp(20px,4vw,56px)}}
/* nav */
.nav{{position:fixed;top:16px;left:50%;transform:translateX(-50%);width:min(88rem,calc(100% - 32px));z-index:50;display:flex;align-items:center;justify-content:space-between;padding:12px 14px 12px 22px;border-radius:999px;transition:background .5s var(--ease),box-shadow .5s var(--ease)}}
.nav.scrolled{{background:color-mix(in srgb,var(--bg) 78%,transparent);backdrop-filter:blur(18px) saturate(1.4);box-shadow:0 10px 40px rgba(0,0,0,.08)}}
.nav.glass{{background:rgba(255,255,255,.06);backdrop-filter:blur(16px) saturate(1.3);border:1px solid rgba(255,255,255,.12)}}
.brand{{display:flex;align-items:center;gap:10px;font-weight:600;font-size:19px;letter-spacing:-.02em}}
.brand small{{font-weight:400;color:var(--muted);font-size:13px;margin-left:6px;letter-spacing:0}}
.nav ul{{display:flex;gap:32px;list-style:none;margin:0;padding:0;font-size:15px;color:var(--muted)}}
.nav ul a:hover{{color:var(--ink)}}
.btn{{display:inline-flex;align-items:center;gap:12px;background:var(--ink);color:var(--bg);font-weight:600;font-size:16px;padding:8px 8px 8px 26px;border-radius:999px;transition:transform .35s var(--ease),box-shadow .35s var(--ease)}}
.btn:hover{{transform:translateY(-2px);box-shadow:0 14px 30px rgba(0,0,0,.18)}}
.btn-dot{{display:grid;place-items:center;width:38px;height:38px;border-radius:50%;background:var(--bg);color:var(--ink);transition:transform .35s var(--ease)}}
.btn:hover .btn-dot{{transform:rotate(-45deg)}}
.nav .btn{{font-size:14px;padding:6px 6px 6px 20px}} .nav .btn-dot{{width:32px;height:32px}}
.link{{font-weight:500;border-bottom:1px solid currentColor;padding-bottom:2px;opacity:.8}}
.btns{{display:flex;align-items:center;gap:26px;margin-top:34px}}
.eyebrow{{font-size:14px;letter-spacing:.02em;color:var(--muted);margin:0 0 22px;display:flex;align-items:center;gap:10px}}
.eyebrow::before{{content:"";width:28px;height:1px;background:currentColor}}
.sub{{font-size:clamp(17px,1.35vw,20px);line-height:1.55;color:var(--muted);max-width:34rem;margin:26px 0 0}}
h1.display{{font-size:clamp(48px,6.4vw,104px)}}
/* entrance */
.rise{{opacity:0;transform:translateY(26px);filter:blur(6px);animation:rise 1.1s var(--ease) forwards;animation-delay:var(--d,0s)}}
@keyframes rise{{to{{opacity:1;transform:none;filter:none}}}}
.reveal{{opacity:0;transform:translateY(34px);transition:opacity 1s var(--ease),transform 1s var(--ease);transition-delay:var(--d,0s)}}
.reveal.in{{opacity:1;transform:none}}
/* hero: card */
.hero-card{{padding:92px clamp(14px,1.6vw,24px) 24px;height:100vh;min-height:680px}}
.hcard{{position:relative;height:100%;border-radius:28px;overflow:hidden}}
.bgv{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}
.mesh{{background:var(--card);overflow:hidden}}
.mesh i{{position:absolute;width:70%;aspect-ratio:1;border-radius:50%;filter:blur(70px);opacity:.85;animation:drift 18s ease-in-out infinite alternate}}
.mesh i:nth-child(1){{background:var(--g1);left:-10%;top:-20%}}
.mesh i:nth-child(2){{background:var(--g2);right:-15%;top:10%;animation-duration:22s}}
.mesh i:nth-child(3){{background:var(--g3);left:20%;bottom:-35%;animation-duration:26s}}
@keyframes drift{{to{{transform:translate(12%,10%) scale(1.15)}}}}
.hcard-shade{{position:absolute;inset:0;background:linear-gradient(90deg,color-mix(in srgb,var(--bg) 70%,transparent) 0%,transparent 55%)}}
.hcard-in{{position:relative;z-index:2;padding:clamp(40px,7vw,110px) clamp(28px,5vw,80px);max-width:52rem}}
.chip{{position:absolute;right:28px;bottom:28px;z-index:2;display:flex;align-items:center;gap:10px;padding:12px 18px;border-radius:999px;background:rgba(255,255,255,.7);backdrop-filter:blur(14px);font-size:14px;font-weight:500;color:#111}}
.pulse{{width:9px;height:9px;border-radius:50%;background:#22C55E;box-shadow:0 0 0 0 rgba(34,197,94,.6);animation:pulse 2s infinite}}
@keyframes pulse{{70%{{box-shadow:0 0 0 12px rgba(34,197,94,0)}}100%{{box-shadow:0 0 0 0 rgba(34,197,94,0)}}}}
/* hero: full */
.hero-full{{position:relative;height:100vh;min-height:700px;display:flex;align-items:flex-end;overflow:hidden}}
.full-shade{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.15) 0%,transparent 35%,color-mix(in srgb,var(--bg) 92%,transparent) 100%)}}
.full-in{{position:relative;z-index:2;padding:0 clamp(24px,5vw,80px) clamp(60px,9vh,110px);max-width:70rem}}
.hero-full h1.display{{font-size:clamp(56px,8vw,132px)}}

.hero-full .eyebrow{{color:rgba(255,255,255,.88);text-shadow:0 1px 18px rgba(0,0,0,.45)}}
.hero-full .sub{{color:rgba(255,255,255,.82);text-shadow:0 1px 18px rgba(0,0,0,.4)}}
.nav.glass small{{color:rgba(255,255,255,.7)}} .nav.glass ul{{color:rgba(255,255,255,.78)}}
.hero-split h1.display{{font-size:clamp(44px,5.3vw,90px)}}
.how-v::after{{content:"";position:absolute;inset:0;background:linear-gradient(180deg,transparent 45%,rgba(0,0,0,.55));z-index:1}}
.hero-full .btn{{background:var(--ink);color:var(--bg)}}
.scroll-cue{{position:absolute;right:clamp(24px,5vw,80px);bottom:60px;z-index:2;font-size:12px;letter-spacing:.2em;color:var(--muted);display:flex;flex-direction:column;align-items:center;gap:12px}}
.scroll-cue span{{width:1px;height:54px;background:linear-gradient(var(--ink),transparent);animation:cue 2.2s var(--ease) infinite}}
@keyframes cue{{0%{{transform:scaleY(0);transform-origin:top}}50%{{transform:scaleY(1);transform-origin:top}}51%{{transform-origin:bottom}}100%{{transform:scaleY(0);transform-origin:bottom}}}}
/* hero: split */
.hero-split{{display:grid;grid-template-columns:1.05fr .95fr;gap:clamp(24px,4vw,64px);align-items:center;min-height:100vh;padding:110px clamp(20px,4vw,56px) 40px;max-width:96rem;margin:0 auto}}
.split-r{{position:relative;height:min(78vh,760px);border-radius:32px;overflow:hidden}}
.float-card{{position:absolute;left:24px;bottom:24px;display:flex;align-items:center;gap:14px;padding:14px 20px;border-radius:18px;background:rgba(255,255,255,.78);backdrop-filter:blur(14px);color:#111;animation:float 5s ease-in-out infinite}}
.float-card b{{display:block;font-size:14px}} .float-card span{{font-size:13px;color:#555}}
@keyframes float{{50%{{transform:translateY(-8px)}}}}
.mini-stats{{display:flex;gap:44px;margin-top:56px;padding-top:28px;border-top:1px solid color-mix(in srgb,var(--ink) 14%,transparent)}}
.mini-stats b,.stat b{{display:block;font-family:'{s['display']}',serif;font-weight:{s['dweight']};font-size:44px;letter-spacing:-.03em}}
.mini-stats span,.stat span{{font-size:14px;color:var(--muted)}}
/* marquee */
.marquee{{overflow:hidden;padding:30px 0;border-block:1px solid color-mix(in srgb,var(--ink) 10%,transparent);mask:linear-gradient(90deg,transparent,#000 12%,#000 88%,transparent)}}
.track{{display:flex;align-items:center;width:max-content;animation:mq 34s linear infinite}}
.track span{{font-family:'{s['display']}',serif;font-size:26px;letter-spacing:-.02em;padding:0 30px;white-space:nowrap;color:color-mix(in srgb,var(--ink) 72%,transparent)}}
.track i{{width:7px;height:7px;border-radius:50%;background:var(--accent);flex:none}}
@keyframes mq{{to{{transform:translateX(-50%)}}}}
/* sections */
section.block{{padding:clamp(80px,11vw,150px) 0}}
.intro{{display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:end;margin-bottom:64px}}
.intro h2{{font-size:clamp(38px,4.4vw,68px)}}
.intro p{{font-size:20px;line-height:1.6;color:var(--muted);margin:0}}
.stats{{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-bottom:64px}}
.stat{{padding:30px 0;border-top:1px solid color-mix(in srgb,var(--ink) 16%,transparent)}}
.stat b{{font-size:clamp(56px,6vw,92px);line-height:1}}
.svcs{{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}}
.svc{{position:relative;padding:34px 30px 30px;border-radius:24px;background:var(--card);color:var(--cardInk);min-height:320px;display:flex;flex-direction:column;transition:transform .5s var(--ease),box-shadow .5s var(--ease)}}
.svc:hover{{transform:translateY(-8px);box-shadow:0 30px 60px rgba(0,0,0,.22)}}
.svc-ico{{width:48px;height:48px;border-radius:14px;display:grid;place-items:center;background:color-mix(in srgb,var(--cardInk) 10%,transparent);margin-bottom:auto}}
.svc h3{{font-family:'{s['display']}',serif;font-weight:{s['dweight']};font-size:30px;letter-spacing:-.03em;margin:60px 0 12px;line-height:1.05}}
.svc p{{margin:0 0 22px;line-height:1.55;opacity:.7}}
.svc-more{{display:flex;align-items:center;gap:8px;font-size:14px;font-weight:600;opacity:.85}}
.how{{display:grid;grid-template-columns:.9fr 1.1fr;gap:clamp(30px,5vw,80px);align-items:stretch}}
.how-v{{position:relative;border-radius:28px;overflow:hidden;min-height:560px}}
.how-v h3{{position:absolute;left:32px;bottom:28px;z-index:2;font-size:clamp(34px,3.4vw,52px);color:#fff;text-shadow:0 2px 30px rgba(0,0,0,.35);margin:0}}
.how ol{{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;justify-content:center}}
.how li{{display:flex;gap:28px;padding:34px 0;border-top:1px solid color-mix(in srgb,var(--ink) 14%,transparent)}}
.how .n{{font-family:'{s['display']}',serif;font-size:22px;color:var(--accent);min-width:42px}}
.how h4{{font-family:'{s['display']}',serif;font-weight:{s['dweight']};font-size:34px;letter-spacing:-.03em;margin:0 0 6px}}
.how p{{margin:0;color:var(--muted);font-size:17px}}
.closer{{text-align:center;padding:clamp(90px,12vw,170px) 0}}
.closer h2{{font-size:clamp(46px,6.4vw,104px);margin-bottom:38px}}
footer{{padding:40px 0 50px;color:var(--muted);font-size:14px;display:flex;justify-content:space-between;border-top:1px solid color-mix(in srgb,var(--ink) 10%,transparent)}}
:focus-visible{{outline:2px solid var(--accent);outline-offset:3px}}
@media (max-width:900px){{.nav ul{{display:none}}.hero-split,.intro,.how,.svcs,.stats{{grid-template-columns:1fr}}.split-r{{height:60vh}}}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important;transition:none!important}}.rise,.reveal{{opacity:1;transform:none;filter:none}}}}
{STAGE_CSS if s['variant'] == 'stage' else ''}
</style>
</head>
<body>
<header class="{nav_cls}" id="nav">
  <a class="brand" href="#">{MARK}{s['name']}<small>{s['tag']}</small></a>
  <nav aria-label="Main"><ul>{''.join(f'<li><a href="#">{n}</a></li>' for n in s['nav'])}</ul></nav>
  <a class="btn" href="#start">{s['cta']}<span class="btn-dot">{ARROW}</span></a>
</header>
<main>
{hero(s)}
<div class="marquee" aria-hidden="true"><div class="track">{marquee}</div></div>
<section class="block"><div class="wrap">
  <div class="intro"><h2 class="display reveal">What working with us<br>actually looks like.</h2><p class="reveal" style="--d:.1s">{s['sub']}</p></div>
  <div class="stats">{stats}</div>
  <div class="svcs">{services}</div>
</div></section>
<section class="block" style="padding-top:0"><div class="wrap how">
  <div class="how-v reveal">{video(s['second'], 'bgv')}<h3 class="display">Three steps.<br>No forms first.</h3></div>
  <ol>{steps}</ol>
</div></section>
<section class="closer" id="start"><div class="wrap">
  <h2 class="display reveal">{s['closer']}</h2>
  <a class="btn reveal" style="--d:.1s" href="#">{s['cta']}<span class="btn-dot">{ARROW}</span></a>
</div></section>
<div class="wrap"><footer><span>&copy; 2026 {s['name']}. </span><span>{s['tag']}</span></footer></div>
</main>
<script>
const nav=document.getElementById('nav');
addEventListener('scroll',()=>nav.classList.toggle('scrolled',scrollY>40),{{passive:true}});
const io=new IntersectionObserver(es=>es.forEach(e=>{{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target)}}}}),{{threshold:.18}});
document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
const count=el=>{{const end=+el.dataset.count,suf=el.dataset.suffix||'',t0=performance.now(),dur=1400;
  const tick=t=>{{const p=Math.min(1,(t-t0)/dur),v=Math.round(end*(1-Math.pow(1-p,3)));el.textContent=v+suf;if(p<1)requestAnimationFrame(tick)}};requestAnimationFrame(tick)}};
const co=new IntersectionObserver(es=>es.forEach(e=>{{if(e.isIntersecting){{count(e.target);co.unobserve(e.target)}}}}),{{threshold:.5}});
document.querySelectorAll('[data-count]').forEach(el=>co.observe(el));
document.querySelectorAll('video').forEach(v=>v.play().catch(()=>{{}}));
{STAGE_JS if s['variant'] == 'stage' else ''}
</script>
</body>
</html>
"""




def check(s):
    """The finance-firm rules the page must pass (references/finance-rules.md)."""
    plain = lambda h: re.sub(r"<[^>]+>", " ", h).replace("&amp;", "&")
    h1, title, town, service = plain(s["h1"]).lower(), s["title"].lower(), s["town"].lower(), s["service"].lower()
    issues = []
    if town not in h1 or service.split()[0] not in h1:
        issues.append(f'H1 should say the service and the town ("{s["service"]} in {s["town"]}"). Now: "{plain(s["h1"]).strip()}"')
    if town not in title or service.split()[0] not in title:
        issues.append(f'Page title should lead with "{s["service"]} in {s["town"]}". Now: "{s["title"]}"')
    if len(s["title"]) > 65:
        issues.append(f"Page title is {len(s['title'])} characters; keep it to 65 or fewer.")
    if not 120 <= len(s["sub"]) <= 165:
        issues.append(f"Subline is {len(s['sub'])} characters; 120 to 165 doubles as a good meta description.")
    return issues


def main():
    brief, out = Path(sys.argv[1]), Path(sys.argv[2])
    s = json.loads(brief.read_text())
    s.setdefault("second", s.get("video"))
    s.setdefault("glow", [s["accent"], s["card"], s["bg"]])
    s.setdefault("title", f'{s["service"]} in {s["town"]} | {s["name"].replace("&amp;", "&")}')
    s.setdefault("tag", f'{s["service"]}, {s["town"]}')
    out.mkdir(parents=True, exist_ok=True)
    # copy every local media file the brief points at into out/assets, so the site is self-contained
    import shutil
    def local(ref):
        if not ref or re.match(r"^(https?:|data:)", ref):
            return ref
        src = (brief.parent / ref).resolve()
        (out / "assets").mkdir(exist_ok=True)
        shutil.copy2(src, out / "assets" / src.name)
        return f"assets/{src.name}"
    for k in ("video", "second"):
        s[k] = local(s.get(k))
    sc = s.get("scene")
    if sc:
        sc["plate"] = local(sc["plate"])
        for L in sc.get("layers", []):
            L["src"] = local(L["src"])
        if sc.get("coins"):
            sc["coins"]["src"] = local(sc["coins"]["src"])
        if sc.get("wings"):
            sc["wings"]["l"], sc["wings"]["r"] = local(sc["wings"]["l"]), local(sc["wings"]["r"])
    (out / "index.html").write_text(page(s))
    print("built", out / "index.html")
    issues = check(s)
    print("SEO checks:", "all passed" if not issues else "")
    for i in issues:
        print("  -", i)


if __name__ == "__main__":
    main()
