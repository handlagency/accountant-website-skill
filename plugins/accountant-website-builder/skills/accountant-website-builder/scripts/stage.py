"""The cinematic "stage" hero: a background plate, layered animated subjects that fly out of the hero on scroll,
a giant echo word for depth, particles and mouse parallax. Imported by build.py. HandL Agency, MIT licence."""

STAGE_CSS = r"""
/* ---------- stage hero ---------- */
.hero-stage{position:relative;height:100vh;min-height:700px;padding:14px}
.st-card{position:relative;height:100%;border-radius:26px;overflow:hidden;isolation:isolate;background:var(--card)}
.st-frame{position:absolute;left:50%;top:50%;width:max(100%,calc((100vh - 28px)*1.7778));aspect-ratio:16/9;transform:translate(-50%,-50%)}
.st-plate{position:absolute;inset:-3%;width:106%;height:106%;object-fit:cover;transform:translate(calc(var(--mx,0)*-14px),calc(var(--my,0)*-10px)) scale(1.04);animation:kb 26s ease-in-out infinite alternate}
@keyframes kb{to{scale:1.06}}
.st-echo{position:absolute;right:4%;top:50%;transform:translate(calc(var(--mx,0)*-26px),-50%);font-family:var(--dfont),serif;font-weight:var(--dw);font-size:clamp(120px,19vw,340px);letter-spacing:-.05em;line-height:.8;color:var(--ink);opacity:.07;white-space:nowrap;pointer-events:none}
.st-canvas{position:absolute;inset:0;width:100%;height:100%;pointer-events:none}
.st-shade{position:absolute;inset:0;background:linear-gradient(90deg,var(--shade) 0%,transparent 58%)}
.st-subjects{position:absolute;inset:14px;pointer-events:none;z-index:5}
.st-subjects .st-frame{will-change:transform}
.fly{position:absolute;inset:0;transform-origin:70% 40%}
.par{position:absolute;inset:0;transform:translate(calc(var(--mx,0)*26px),calc(var(--my,0)*18px))}
.lay{position:absolute}
.lay>img{display:block;width:100%;height:auto;filter:drop-shadow(0 40px 50px rgba(0,0,0,var(--sh,.18)))}
.shine{position:absolute;inset:0;-webkit-mask:var(--m) center/100% 100% no-repeat;mask:var(--m) center/100% 100% no-repeat;background:linear-gradient(105deg,transparent 38%,rgba(255,255,255,.75) 50%,transparent 62%);background-size:260% 100%;mix-blend-mode:soft-light;animation:shine 5s ease-in-out infinite}
@keyframes shine{0%{background-position:130% 0}55%,100%{background-position:-130% 0}}
.m-glide{animation:glide 7s ease-in-out infinite}
@keyframes glide{0%,100%{transform:translate(0,0) rotate(0)}50%{transform:translate(-2.5%,-5%) rotate(-3.5deg)}}
.m-float{animation:floaty 6s ease-in-out infinite}
@keyframes floaty{0%,100%{transform:translate(0,0) rotate(-2deg)}50%{transform:translate(0,-7%) rotate(3deg)}}
.m-float.d2{animation-duration:7.4s;animation-delay:-2s}.m-float.d3{animation-duration:8.6s;animation-delay:-4s}
.m-hover{animation:hov 5s ease-in-out infinite}
@keyframes hov{0%,100%{transform:translate(0,0)}25%{transform:translate(-3%,-4%)}50%{transform:translate(1.5%,-1%)}75%{transform:translate(-1%,-5%)}}
.m-hover>img{animation:buzz .12s linear infinite alternate}
@keyframes buzz{to{transform:translateY(1.2%)}}
.ghost{position:absolute;inset:0;width:100%;filter:blur(5px) brightness(1.3);opacity:.0;animation:ghost .09s steps(2) infinite}
@keyframes ghost{50%{opacity:.55;transform:translateY(-2.5%) scaleY(1.04)}}
.m-rock{animation:rock 5.5s ease-in-out infinite;transform-origin:50% 80%}
@keyframes rock{0%,100%{transform:translateY(0) rotate(-2.4deg)}50%{transform:translateY(3%) rotate(2.4deg)}}
.refl{position:absolute;left:0;top:96%;width:100%;transform:scaleY(-.55);transform-origin:top;opacity:.28;filter:blur(2px);-webkit-mask:linear-gradient(transparent 30%,#000);mask:linear-gradient(transparent 30%,#000)}
.ripple{position:absolute;left:50%;top:100%;width:120%;aspect-ratio:5/1;border:2px solid rgba(255,255,255,.55);border-radius:50%;transform:translate(-50%,-50%) scale(.3);opacity:0;animation:rip 4.8s ease-out infinite}
.ripple:nth-of-type(2){animation-delay:1.6s}.ripple:nth-of-type(3){animation-delay:3.2s}
@keyframes rip{15%{opacity:.7}100%{transform:translate(-50%,-50%) scale(1.6);opacity:0}}
.m-flow{animation:flow 6s ease-in-out infinite}
@keyframes flow{0%,100%{transform:scale(1) rotate(0);filter:brightness(1)}50%{transform:scale(1.04) rotate(-2deg);filter:brightness(1.25) saturate(1.2)}}
.wings{position:absolute;perspective:1100px}
.wings .w{position:absolute;top:0;width:50.6%;transform-style:preserve-3d}
.wings .w img{width:100%;display:block;filter:drop-shadow(0 30px 40px rgba(0,0,0,.18))}
.wings .wl{left:0;transform-origin:100% 50%;animation:flapL .62s ease-in-out infinite alternate}
.wings .wr{right:0;transform-origin:0 50%;animation:flapR .62s ease-in-out infinite alternate}
@keyframes flapL{from{transform:rotateX(28deg) rotateY(4deg)}to{transform:rotateX(28deg) rotateY(56deg)}}
@keyframes flapR{from{transform:rotateX(28deg) rotateY(-4deg)}to{transform:rotateX(28deg) rotateY(-56deg)}}
.m-drift{animation:drift 9s ease-in-out infinite}
@keyframes drift{0%,100%{transform:translate(0,0) rotate(-6deg)}33%{transform:translate(-6%,-8%) rotate(4deg)}66%{transform:translate(4%,-3%) rotate(-2deg)}}
.st-copy{position:absolute;left:14px;bottom:14px;z-index:7;padding:0 clamp(26px,4.6vw,80px) clamp(40px,8vh,96px);max-width:min(46rem,56%)}
.st-copy h1.display{font-size:clamp(50px,6.2vw,112px)}
.st-copy .sub{color:var(--muted)}
.st-panel{position:absolute;right:42px;bottom:42px;z-index:7;width:270px;padding:18px 20px;border-radius:20px;background:var(--glass);backdrop-filter:blur(18px) saturate(1.3);border:1px solid rgba(255,255,255,.28);color:var(--ink)}
.st-panel b{display:flex;align-items:center;gap:9px;font-size:13px;letter-spacing:.04em;text-transform:none;color:var(--muted);font-weight:500;margin-bottom:10px}
.st-panel ul{list-style:none;margin:0;padding:0;font-size:15px}
.st-panel li{display:flex;justify-content:space-between;gap:12px;padding:8px 0;border-top:1px solid color-mix(in srgb,var(--ink) 12%,transparent)}
.st-panel li span{color:var(--muted)}
.st-scroll{position:absolute;left:50%;bottom:36px;z-index:7;transform:translateX(-50%);font-size:12px;letter-spacing:.18em;color:var(--muted)}
.coin{position:absolute;perspective:900px;animation:cfall var(--dur) linear infinite;animation-delay:var(--del)}
.coin .spin{position:relative;width:100%;aspect-ratio:1;transform-style:preserve-3d;animation:cspin var(--sp) linear infinite}
.coin .spin img{position:absolute;inset:0;width:100%;height:100%;backface-visibility:visible}
.coin .spin img.e{filter:brightness(.62)}
.coin{filter:blur(var(--bl)) drop-shadow(0 30px 40px rgba(40,30,80,.22))}
@keyframes cfall{0%{transform:translate(0,-38vh) rotate(0);opacity:0}8%{opacity:1}92%{opacity:1}100%{transform:translate(var(--sw),62vh) rotate(var(--rt));opacity:0}}
@keyframes cspin{from{transform:rotateX(var(--tilt)) rotateY(0)}to{transform:rotateX(var(--tilt)) rotateY(360deg)}}
@media (max-width:900px){.st-copy{max-width:100%}.st-panel{display:none}.st-echo{font-size:34vw}}
@media (prefers-reduced-motion:reduce){.fly{transform:none!important}}
"""

STAGE_JS = r"""
(()=>{const hero=document.querySelector('.hero-stage');if(!hero)return;
const fly=hero.querySelector('.fly');
addEventListener('mousemove',e=>{hero.style.setProperty('--mx',(e.clientX/innerWidth-.5).toFixed(3));hero.style.setProperty('--my',(e.clientY/innerHeight-.5).toFixed(3))},{passive:true});
const onScroll=()=>{const p=Math.min(1.6,scrollY/innerHeight);if(fly){const e=p*p*(3-2*Math.min(1,p));fly.style.transform=`translate(${e*9}vw,${p*64}vh) rotate(${e*10}deg) scale(${1-e*.45})`;fly.style.opacity=String(Math.max(0,1-Math.max(0,p-.8)/.45))}};
addEventListener('scroll',onScroll,{passive:true});onScroll();
const cv=hero.querySelector('.st-canvas');if(!cv)return;const kind=cv.dataset.kind,cols=(cv.dataset.cols||'#ffffff').split(',');const ctx=cv.getContext('2d');let W,H,dpr;
const size=()=>{dpr=Math.min(2,devicePixelRatio||1);W=cv.clientWidth;H=cv.clientHeight;cv.width=W*dpr;cv.height=H*dpr;ctx.setTransform(dpr,0,0,dpr,0,0)};size();addEventListener('resize',size);
let seed=7;const rnd=()=>((seed=(seed*16807)%2147483647)/2147483647);
const N={petals:28,gold:80,sparkle:110,receipts:12,mist:7,dust:40}[kind]||30;
const P=[...Array(N)].map(()=>({x:rnd(),y:rnd(),z:.4+rnd()*.9,r:rnd()*6.28,v:.2+rnd()*.8,t:rnd()*6.28,c:cols[Math.floor(rnd()*cols.length)]}));
let last=performance.now();
const draw=now=>{const dt=Math.min(.05,(now-last)/1000);last=now;ctx.clearRect(0,0,W,H);
for(const p of P){p.t+=dt*(.8+p.v);
 if(kind==='petals'){p.x+=dt*.018*p.v+Math.sin(p.t)*.0006;p.y+=dt*.03*p.z;p.r+=dt*p.v;if(p.y>1.05){p.y=-.05;p.x=rnd()}if(p.x>1.05)p.x=-.05;
  ctx.save();ctx.translate(p.x*W,p.y*H);ctx.rotate(p.r);ctx.scale(1,.45+.35*Math.sin(p.t*2));ctx.globalAlpha=.75;ctx.fillStyle=p.c;ctx.beginPath();ctx.ellipse(0,0,7*p.z,4.2*p.z,0,0,6.28);ctx.fill();ctx.restore()}
 else if(kind==='receipts'){p.y-=dt*.02*p.v;p.x+=Math.sin(p.t*.6)*.0007;p.r+=dt*.6*p.v;if(p.y<-.08){p.y=1.08;p.x=.45+rnd()*.55}
  ctx.save();ctx.translate(p.x*W,p.y*H);ctx.rotate(p.r);ctx.scale(Math.cos(p.t*.9),1);ctx.globalAlpha=.9;ctx.fillStyle='#fff';ctx.shadowColor='rgba(30,60,140,.18)';ctx.shadowBlur=14;const w=16*p.z+6,h=w*1.5;ctx.fillRect(-w/2,-h/2,w,h);ctx.shadowBlur=0;ctx.fillStyle='rgba(30,60,140,.22)';for(let i=1;i<5;i++)ctx.fillRect(-w/2+3,-h/2+i*h/6,w*(i%2?.7:.5),1.2);ctx.restore()}
 else if(kind==='mist'){p.x+=dt*.006*p.v;if(p.x>1.3)p.x=-.3;const g=ctx.createRadialGradient(p.x*W,(.55+p.y*.4)*H,0,p.x*W,(.55+p.y*.4)*H,260*p.z);g.addColorStop(0,'rgba(255,255,255,.22)');g.addColorStop(1,'rgba(255,255,255,0)');ctx.fillStyle=g;ctx.fillRect(0,0,W,H)}
 else{const up=kind==='gold'?-.012:-.004;p.y+=dt*up*p.v;p.x+=dt*(kind==='sparkle'?.01:.002)*p.v+Math.sin(p.t*.5)*.0004;if(p.y<-.02){p.y=1.02;p.x=rnd()}if(p.x>1.02)p.x=-.02;
  const a=.25+.75*Math.abs(Math.sin(p.t));const r=(kind==='dust'?1.2:1.6)*p.z+.4;ctx.globalAlpha=a;ctx.fillStyle=p.c;ctx.shadowColor=p.c;ctx.shadowBlur=10;ctx.beginPath();ctx.arc(p.x*W,p.y*H,r,0,6.28);ctx.fill();ctx.shadowBlur=0;ctx.globalAlpha=1}}
requestAnimationFrame(draw)};requestAnimationFrame(draw)})();
"""


def _layer(L, i):
    """One animated subject layer positioned in % of the 16:9 frame."""
    m = L.get("motion", "float")
    pos = f'left:{L["left"]}%;top:{L["top"]}%;width:{L["width"]}%'
    img = f'<img src="{L["src"]}" alt="">'
    extra = ""
    if L.get("shine"):
        extra += f'<div class="shine" style="--m:url({L["src"]})"></div>'
    if m == "hover":
        extra += f'<img class="ghost" src="{L["src"]}" alt="">'
    if m == "rock":
        extra += f'<img class="refl" src="{L["src"]}" alt=""><i class="ripple"></i><i class="ripple"></i><i class="ripple"></i>'
    cls = {"glide": "m-glide", "float": f"m-float d{(i % 3) + 1}", "hover": "m-hover", "rock": "m-rock", "flow": "m-flow"}.get(m, "m-float")
    return f'<div class="lay {cls}" style="{pos}">{img}{extra}</div>'


def stage_hero(s, words):
    sc = s["scene"]
    layers = "".join(_layer(L, i) for i, L in enumerate(sc.get("layers", [])))
    w = sc.get("wings")
    if w:
        layers += (f'<div class="lay m-drift" style="left:{w["left"]}%;top:{w["top"]}%;width:{w["width"]}%">'
                   f'<div class="wings" style="position:relative;width:100%;aspect-ratio:1/{w["aspect"]}">'
                   f'<div class="w wl"><img src="{w["l"]}" alt=""></div><div class="w wr"><img src="{w["r"]}" alt=""></div></div></div>')
    for i, c in enumerate(sc.get("coins", {}).get("items", [])):
        src = sc["coins"]["src"]
        stack = "".join(f'<img class="{'e' if 0 < z < 7 else ''}" src="{src}" alt="" style="transform:translateZ({z - 3.5:.1f}px)">' for z in range(8))
        layers += (f'<div class="coin" style="left:{c[0]}%;top:{c[1]}%;width:{c[2]}%;--dur:{c[3]}s;--del:{-c[4]}s;--bl:{c[5]}px;'
                   f'--sp:{c[6]}s;--tilt:{c[7]}deg;--sw:{c[8]}vw;--rt:{c[9]}deg"><div class="spin">{stack}</div></div>')
    panel = "".join(f"<li>{a}<span>{b}</span></li>" for a, b in sc.get("panel", []))
    return (f'<section class="hero hero-stage" style="--shade:{sc.get("shade", "transparent")};--glass:{sc.get("glass", "rgba(255,255,255,.55)")};--dfont:\'{s["display"]}\';--dw:{s["dweight"]}">'
            f'<div class="st-card"><div class="st-frame"><img class="st-plate" src="{sc["plate"]}" alt="">'
            f'<div class="st-echo" aria-hidden="true">{sc.get("echo", "")}</div></div>'
            f'<canvas class="st-canvas" data-kind="{sc.get("particles", "dust")}" data-cols="{",".join(sc.get("colors", ["#ffffff"]))}"></canvas>'
            f'<div class="st-shade"></div>'
            '</div>'
            f'<div class="st-subjects" aria-hidden="true"><div class="st-frame"><div class="fly"><div class="par">{layers}</div></div></div></div>'
            f'<div class="st-copy">{words}</div>'
            + (f'<div class="st-panel rise" style="--d:.9s"><b><span class="pulse"></span>{sc.get("panel_title", "At a glance")}</b><ul>{panel}</ul></div>' if panel else "")
            + '<div class="st-scroll rise" style="--d:1.2s">Scroll</div>'
            '</section>')
