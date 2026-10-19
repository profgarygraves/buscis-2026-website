"""Compose prototype pages from shared partials + program data.
Mirrors the planned PHP structure on the live server:
  inc/header.php, inc/footer.php, inc/programs.php (data), program.php (template)
"""
import pathlib, sys, re
ROOT = pathlib.Path(__file__).parent
SITE = "--site" in sys.argv   # GitHub Pages build: every page gets a full HTML wrapper, photos copied in
S = ROOT / "src"; OUT = ROOT / ("docs" if SITE else "dist"); OUT.mkdir(exist_ok=True)
sys.path.insert(0, str(S))
from programs import P, GROUPS, JOBS, SCHED, LEADS
from people import STAFF, DEPTS, FACULTY, SOCIAL, CLUB
from pages import PAGES, COUNSELORS, ESARS

def ico(d):
    return ('<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{d}</svg>')

TOK = {
 "{{FLAG}}": '<svg width="20" height="22" viewBox="0 0 20 22" aria-hidden="true"><rect x="1" y="1" width="2.5" height="20" fill="#0F406B"/><path d="M3.5 2h14l-3.5 5 3.5 5h-14z" fill="#FFD600" stroke="#B89A00" stroke-width=".6"/></svg>',
 "{{I_CAL}}": ico('<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M16 3v4M8 3v4M3 10h18"/>'),
 "{{I_BOOK}}": ico('<path d="M4 4h6a3 3 0 0 1 3 3v13a2 2 0 0 0-2-2H4z"/><path d="M20 4h-6a3 3 0 0 0-1 .2V20a2 2 0 0 1 2-2h5z"/>'),
 "{{I_MAP}}": ico('<path d="M9 4 3 6v14l6-2 6 2 6-2V4l-6 2z"/><path d="M9 4v14M15 6v14"/>'),
 "{{I_USER}}": ico('<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>'),
 "{{I_USERS}}": ico('<circle cx="9" cy="8" r="3.5"/><path d="M2 20a7 7 0 0 1 14 0"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M22 20a7 7 0 0 0-4-6.3"/>'),
 "{{I_DOC}}": ico('<path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6M8 13h8M8 17h5"/>'),
 "{{I_CLOCK}}": ico('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'),
 "{{I_BRIEF}}": ico('<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2M3 13h18"/>'),
 "{{I_GLOBE}}": ico('<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>'),
 "{{I_SHIRT}}": ico('<path d="M8 3 3 6l2 5 2-1v11h10V10l2 1 2-5-5-3a4 4 0 0 1-8 0z"/>'),
 "{{I_SPARK}}": ico('<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M6 18l2.5-2.5M15.5 8.5 18 6"/>'),
 "{{SCHED}}": "https://schedule.nocccd.edu/?college=2",
}
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700'
         '&family=Questrial&family=Sorts+Mill+Goudy&display=swap">')


SICON = {
 "Facebook": '<svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M13.5 22v-8h2.7l.4-3.2h-3.1V8.8c0-.9.3-1.6 1.6-1.6h1.7V4.4c-.3 0-1.3-.1-2.5-.1-2.5 0-4.1 1.5-4.1 4.2v2.3H7.5V14h2.7v8z"/></svg>',
 "Instagram": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg>',
 "LinkedIn": '<svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M4 9h3.6v11H4zM5.8 3.5a2.1 2.1 0 1 1 0 4.2 2.1 2.1 0 0 1 0-4.2zM9.8 9h3.4v1.6c.5-.9 1.7-1.9 3.5-1.9 3.7 0 4.3 2.4 4.3 5.5V20h-3.6v-5.1c0-1.2 0-2.8-1.7-2.8s-2 1.3-2 2.7V20H9.8z"/></svg>',
 "YouTube": '<svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M22 8.2a3 3 0 0 0-2.1-2.1C18 5.6 12 5.6 12 5.6s-6 0-7.9.5A3 3 0 0 0 2 8.2 31 31 0 0 0 1.6 12 31 31 0 0 0 2 15.8a3 3 0 0 0 2.1 2.1c1.9.5 7.9.5 7.9.5s6 0 7.9-.5a3 3 0 0 0 2.1-2.1 31 31 0 0 0 .4-3.8 31 31 0 0 0-.4-3.8zM10 15V9l5.2 3z"/></svg>',
}
TOK["{{SOCIAL_ICONS}}"] = "".join(f'<li><a href="{u}" aria-label="{n} {h}">{SICON[n]}</a></li>' for n, h, u in SOCIAL)
TOK["{{SOCIAL_LIST}}"] = "".join(f'<li><a href="{u}">{SICON[n]}<span>{n} <small>{h}</small></span></a></li>' for n, h, u in SOCIAL)
TOK["{{CLUB}}"] = CLUB

BY_EMAIL = {f[1]: f for f in FACULTY}
DEPT_COLOR = {"acct": "law", "bus": "biz", "cis": "tech", "pleg": "para", "staff": "biz"}

def slug(name):
    import re
    return re.sub(r"[^a-z]+", "-", name.split(",")[0].lower().replace("dr. ", "")).strip("-")

def initials(name):
    parts = [w for w in name.split(",")[0].replace("Dr. ", "").split() if w[0].isalpha()]
    return (parts[0][0] + parts[-1][0]).upper()

PHOTO_ALIASES = {"sandy-carter": "sandy-santalia-carter"}
def photo(name):
    s = slug(name); s = PHOTO_ALIASES.get(s, s)
    return f"img/people/{s}.jpg" if (ROOT / "img" / "people" / f"{s}.jpg").exists() else None

def person(name, role="", area="", email="", phone="", dept="bus"):
    # Live site (PHP): if file_exists("img/people/{slug}.jpg") print <img>, else the initials tile below.
    src = photo(name)
    ph = (f'<div class="ph c-{DEPT_COLOR[dept]}"><img src="{src}" alt="{name}" loading="lazy" width="600" height="750"></div>' if src
          else f'<div class="ph c-{DEPT_COLOR[dept]}"><span>{initials(name)}</span></div>')
    meta = (f'<b class="nm">{name}</b>' + (f'<span class="rl">{role}</span>' if role else "")
            + (f'<span class="ar">{area}</span>' if area else "")
            + (f'<span class="ct">{phone}</span>' if phone else "")
            + (f'<span class="ct mail">{email}</span>' if email else ""))
    return f'<li class="person">{ph}<div class="pm">{meta}</div></li>'

def last_name(n):
    w = n.split()
    return (w[-2] + " " + w[-1]) if len(w) > 2 and w[-2] in ("St.", "de", "Van") else w[-1]

def lead_of(key):
    f = BY_EMAIL[LEADS[key]]
    return f[0], f[1], f[2]

LEAD_ROLES = {}
for _k, _e in LEADS.items():
    LEAD_ROLES.setdefault(_e, []).append(P[_k]["name"])

def lead_line(key):
    n, e, d = lead_of(key)
    src = photo(n)
    av = f'<img src="{src}" alt="">' if src else initials(n)
    return (f'<p class="leadline"><span class="av c-{DEPT_COLOR[d]}">{av}</span>'
            f'<span><span class="k">Program lead</span><b>Prof. {n}</b></span></p>')

def faculty_page():
    staff = "".join(person(n, t, "", e, ph, "staff") for n, t, ph, e in STAFF)
    radios = ('<input type="radio" name="dept" id="d-all" checked><label for="d-all">All departments</label>'
              + "".join(f'<input type="radio" name="dept" id="d-{k}"><label for="d-{k}"><i style="background:var(--{DEPT_COLOR[k]})"></i>{v}</label>' for k, v in DEPTS))
    hide = ",\n".join(f".dir:has(#d-{k}:checked) .dept:not(.dp-{k})" for k, _ in DEPTS)
    secs = []
    for k, v in DEPTS:
        ppl = sorted([f for f in FACULTY if f[2] == k], key=lambda f: (photo(f[0]) is None, last_name(f[0]), f[0]))
        cards = "".join(person(f[0], " &middot; ".join(x for x in [f[3], ("Program Lead: " + ", ".join(LEAD_ROLES[f[1]])) if f[1] in LEAD_ROLES else ""] if x), f[4], f[1], "", k) for f in ppl)
        secs.append(f'<section class="dept dp-{k}"><div class="group-label"><span class="swatch" style="background:var(--{DEPT_COLOR[k]})"></span><h3>{v}</h3><span>{len(ppl)} faculty</span></div><ul class="people">{cards}</ul></section>')
    return f"""<style>{hide}{{display:none}}</style>
<main id="main">
<section class="hero slim"><div class="wrap"><div>
  <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Business &amp; CIS</a> &rsaquo; Faculty &amp; Staff</nav>
  <h1>Faculty &amp; Staff</h1>
  <p class="lead">{len(FACULTY)} faculty across four departments, plus the division office team. Faculty with a photo on file are listed first, then everyone else, alphabetically by last name.</p>
</div></div></section>
<section class="section"><div class="wrap">
  <div class="section-head"><div><h2>Division office</h2><p>Building 300, Room 325 &middot; buscis@fullcoll.edu &middot; 714-992-7032</p></div></div>
  <ul class="people staff">{staff}</ul>
</div></section>
<section class="section dir" style="padding-top:0"><div class="wrap">
  <div class="section-head"><div><h2>Faculty</h2><p>Office hours are posted in each course in Canvas.</p></div>
  <fieldset class="filter"><legend>Show faculty by department</legend>{radios}</fieldset></div>
  {"".join(secs)}
</div></section>
<div class="wrap reviewed">Page last reviewed: Fall 2026</div>
</main>
"""

def content_page(pg):
    todo = (f'<div class="todo" role="note"><b>Update needed before launch:</b> {pg["todo"]}</div>' if pg["todo"] else "")
    body = (pg["body"].replace("{{COUNSELORS}}", "".join(person(n, t, "", e, "", "staff") for n, t, e in COUNSELORS))
            .replace("{{ESARS}}", ESARS)
            .replace("{{STAFF}}", "".join(person(n, t, "", e, ph, "staff") for n, t, ph, e in STAFF)))
    return f"""<main id="main">
<section class="hero slim"><div class="wrap"><div>
  <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Business &amp; CIS</a> &rsaquo; {pg["eyebrow"]} &rsaquo; {pg["title"]}</nav>
  <h1>{pg["title"]}</h1><p class="lead">{pg["lead"]}</p>
</div></div></section>
<section class="section"><div class="wrap">{todo}<div class="two"><div class="prose">{body}</div><aside>{pg["aside"]}</aside></div></div></section>
<div class="wrap reviewed">Page last reviewed: Fall 2026</div>
</main>
"""

PILL = {"AST": "AS-T", "AA": "AA", "AS": "AS", "C": "Cert", "SK": "Skills"}
FULL = {"AST": "AS-T degree", "AA": "AA degree", "AS": "AS degree"}
TAGS = {"biz": "Business &amp; Management", "law": "Accounting &amp; Law", "para": "Paralegal Studies", "tech": "Technology"}
TOTAL = sum(len(p["awards"]) for p in P.values())

def summary_chips(aw):
    deg = [a for a in aw if a["kind"] in FULL]; cer = [a for a in aw if a["kind"] in ("C", "SK")]
    out = []
    if len(deg) == 1: out.append(FULL[deg[0]["kind"]])
    elif deg: out.append(f"{len(deg)} degrees")
    if cer: out.append("1 certificate" if len(cer) == 1 else f"{len(cer)} certificates")
    return "".join(f"<span>{c}</span>" for c in out)

def awards_block(p):
    items = "".join(f'<li><a href="{a["url"]}"><span class="pill k-{a["kind"]}">{PILL[a["kind"]]}</span>{a["name"]}</a></li>' for a in p["awards"])
    return (f'<details class="aw"><summary><span class="aw-chips">{summary_chips(p["awards"])}</span>'
            f'<span class="aw-more">Show all</span></summary><ul class="awlist">{items}</ul></details>')

def start_links(p, titles=False):
    parts = [f'<a href="{SCHED}{kw}"><b>{code}</b>{" " + t if titles else ""}</a>' for kw, code, t in p["starts"]]
    return " or ".join(parts)

def start_line(p):
    t = len(p["starts"]) == 1
    return f'<p class="start">{{{{FLAG}}}}<span><span class="k">Start here</span>{start_links(p, titles=t)}</span></p>'

def card(key):
    p = P[key]; c = p["color"]
    tag = p.get("tag", TAGS[c]); new = ' <span class="new">NEW</span>' if p.get("new") else ""
    snap = f'<p class="snap">{p["snap"]}</p>' if p["snap"] else ""
    links = (f'<div class="prog-links{" full" if p.get("featured") else ""}"><a href="{p["file"]}">Explore program &rarr;</a>'
             f'<a href="{SCHED}{p["subj"]}">{p["subj"]} classes</a></div>')
    head = f'<a class="prog-head" href="{p["file"]}"><span class="tag">{tag}</span><h3>{p["name"]}{new}</h3></a>'
    if p.get("featured"):
        hl = "".join(f"<li>{h}</li>" for h in p["highlights"])
        body = (f'<div><p>{p["desc"]}</p><ul class="list">{hl}</ul>{awards_block(p)}</div>'
                f'<div style="display:grid;gap:14px;align-content:start">{start_line(p)}{snap}{lead_line(key)}</div>{links}')
        return f'<article class="prog a-{c} featured">{head}<div class="prog-body">{body}</div></article>'
    return f'<article class="prog a-{c}">{head}<div class="prog-body"><p>{p["desc"]}</p>{awards_block(p)}{start_line(p)}{snap}{lead_line(key)}{links}</div></article>'

def programs_html():
    out = []
    for gid, label, keys in GROUPS:
        colors = list(dict.fromkeys(P[k]["color"] for k in keys))
        sw = "".join(f'<span class="swatch" style="background:var(--{c})"></span>' for c in colors)
        out.append(f'<div class="group g-{gid}"><div class="group-label">{sw}<h3>{label}</h3>'
                   f'<span>{len(keys)} program areas</span></div><div class="grid n{len(keys)}">'
                   + "".join(card(k) for k in keys) + '</div></div>')
    return "\n".join(out)

def program_page(key):
    p = P[key]; c = p["color"]; tag = p.get("tag", TAGS[c])
    new = ' <span class="new">NEW</span>' if p.get("new") else ""
    first = p["starts"][0]
    facts = [("Start here", " or ".join(f'<a href="{SCHED}{kw}"><b>{code}</b></a> {t}' for kw, code, t in p["starts"])),
             ("Awards", f'{len([a for a in p["awards"] if a["kind"] in FULL])} degree(s), {len([a for a in p["awards"] if a["kind"] in ("C","SK")])} certificate(s)'.replace("0 degree(s), ", "").replace("1 degree(s)", "1 degree").replace("(s)", "s").replace("1 certificates", "1 certificate")),
             ("Hornet Pathway", '<a href="https://www.fullcoll.edu/hornet-pathways/">Applied Technology, Engineering and Mathematics</a>' if c == "tech" else
                                ('<a href="https://pathways.fullcoll.edu/category/public-service-and-education/">Public Service and Education</a>' if c == "para" else
                                 '<a href="https://pathways.fullcoll.edu/category/business/">Business</a>'))]
    ln, le, ld = lead_of(key)
    facts.append(("Program lead", f'Prof. {ln}<br>{le}'))
    facts_html = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in facts)

    rows = "".join(f'<tr><td><a href="{a["url"]}">{a["name"]}</a></td><td><span class="pill{" deg" if a["kind"] in FULL else ""}">'
                   f'{FULL.get(a["kind"], "Skills certificate" if a["kind"] == "SK" else "Certificate")}</span></td></tr>' for a in p["awards"])
    blocks = [f'<div class="block"><h2>About the program</h2>{"".join(f"<p>{x}</p>" for x in p["overview"])}</div>']
    if p.get("notice"):
        blocks.append(f'<div class="block notice"><strong>Important notice.</strong> {p["notice"]}</div>')
    blocks.append('<div class="block"><h2>Choose your award</h2><div class="tablebox"><table><thead><tr><th>Award</th><th>Type</th></tr></thead>'
                  f'<tbody>{rows}</tbody></table></div><p class="small">Each award links to its official catalog page for required courses and units.</p></div>')
    if p.get("events"):
        ev = "".join(f'<li><b>{n}</b> <span class="when">{w}</span><br>{d}</li>' for n, w, d in p["events"])
        blocks.append(f'<div class="block"><h2>Events every semester</h2><ul class="events">{ev}</ul></div>')
    if p["jobs"]:
        jr = "".join(f'<tr><td>{JOBS[j][0]}{" <span class=\"pill\">Bachelor&#8217;s</span>" if JOBS[j][3] else ""}</td><td class="num">{JOBS[j][1]}</td><td class="num">{JOBS[j][2]}/hr</td></tr>' for j in p["jobs"])
        blocks.append('<div class="block"><h2>Where it can lead</h2><div class="tablebox"><table><thead><tr><th>Occupation</th><th>OC jobs, 2024</th><th>Median pay</th></tr></thead>'
                      f'<tbody>{jr}</tbody></table></div><p class="small">Orange County data from Lightcast, as reported in the Fullerton College Institutional Effectiveness Report 2024-25. '
                      f'Roles marked Bachelor&#8217;s usually require a four-year degree. {p.get("jobs_note","")}</p></div>')
    if p["faculty"] or True:
        fac = sorted(p["faculty"], key=lambda f: f["email"] != LEADS[key])
        if not any(f["email"] == LEADS[key] for f in fac):
            ln, le, ld = lead_of(key); fac.insert(0, {"name": ln, "email": le, "role": "", "area": BY_EMAIL[le][4]})
        fl = "".join(person(BY_EMAIL.get(f["email"], (f["name"],))[0],
                            (("Program Lead" + (" &middot; " + f["role"] if f["role"] and f["role"] != "Program Lead" else "")) if f["email"] == LEADS[key] else f["role"]),
                            f["area"], f["email"], "", BY_EMAIL.get(f["email"], ("","","bus"))[2]) for f in fac)
        blocks.append(f'<div class="block"><h2>Faculty</h2><ul class="people compact">{fl}</ul><p class="small"><a href="faculty.html">See all division faculty &rarr;</a></p></div>')

    plan = [("Find " + first[1] + " in the schedule", SCHED + first[0]), (f'All {p["subj"]} classes this term', SCHED + p["subj"])]
    if p.get("map"): plan.append(("Program map", p["map"]))
    plan += [("Business program maps" if c != "tech" else "Hornet Pathways program maps", "https://www.fullcoll.edu/hornet-pathways/"),
             ("Career education counselors", "counselors.html"), ("Apply for a certificate", "forms.html")]
    plan_html = "".join(f'<li><a href="{u}">{t}</a></li>' for t, u in plan)
    docs = ""
    if p.get("docs"):
        docs = '<div class="aside-card"><h2>Program documents</h2><ul>' + "".join(f'<li><a href="{u}">{t}</a></li>' for t, u in p["docs"]) + '</ul></div>'
    hl = "".join(f"<li>{h}</li>" for h in p["highlights"])
    deadlines = ''
    rel = "".join(f'<a class="a-{P[r]["color"]}" href="{P[r]["file"]}">{P[r]["name"]}<span>{P[r]["desc"].split(".")[0]}.</span></a>' for r in p["related"])

    return f'''<main id="main">
<section class="phero a-{c}">
  <div class="wrap">
    <div>
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Business &amp; CIS</a> &rsaquo; <a href="index.html#programs">Programs</a> &rsaquo; {p["name"]}</nav>
      <span class="tag">{tag}</span>
      <h1>{p["name"]}{new}</h1>
      <p>{p["lead"]}</p>
      <div class="btns">
        <a class="btn btn-primary" href="{SCHED}{first[0]}">Find {first[1]} in the schedule</a>
        <a class="btn btn-ghost on-color" href="#awards">See degrees &amp; certificates</a>
      </div>
    </div>
    <aside class="facts" aria-labelledby="qf"><h2 id="qf">Quick facts</h2><dl>{facts_html}</dl></aside>
  </div>
</section>
<section class="section">
  <div class="wrap two">
    <div class="prose" id="awards">{"".join(blocks)}</div>
    <aside>
      <div class="aside-card highlight"><h2>Highlights</h2><ul class="ticks">{hl}</ul></div>
      <div class="aside-card"><h2>Plan your classes</h2><ul>{plan_html}</ul></div>
      {deadlines}
      {docs}
    </aside>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap"><h2 style="font-size:24px;margin-bottom:16px">Related programs</h2><div class="related">{rel}</div></div>
</section>
<div class="wrap reviewed">Page last reviewed: Fall 2026</div>
</main>
'''

css = (S / "style.css").read_text()
header = (S / "header.html").read_text()
footer = (S / "footer.html").read_text()


# Names that always link to the person's own faculty page (set once, applied site-wide)
NAME_LINKS = {"Gary Graves": "https://ggraves.faculty.fullcoll.edu/"}

def link_names(html):
    import re
    out, in_a, in_head = [], 0, False
    for tok in re.split(r"(<[^>]+>)", html):
        if tok.startswith("<"):
            t = tok.lower()
            if t.startswith("<a ") or t == "<a>": in_a += 1
            elif t.startswith("</a"): in_a = max(0, in_a - 1)
            elif t.startswith("<title") or t.startswith("<style") or t.startswith("<script"): in_head = True
            elif t.startswith("</title") or t.startswith("</style") or t.startswith("</script"): in_head = False
            out.append(tok)
        elif in_a or in_head:
            out.append(tok)
        else:
            for name, url in NAME_LINKS.items():
                tok = tok.replace(name, f'<a class="namelink" href="{url}">{name}</a>')
            tok = re.sub(r"\b([\w.+-]+@(?:fullcoll\.edu|gmail\.com))\b", r'<a href="mailto:\1">\1</a>', tok)
            out.append(tok)
    return "".join(out)

def page(title, body, is_index, desc=None):
    html = (f'<title>{title}</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n'
            f'<meta name="description" content="{desc or "Business and Computer Information Systems Division at Fullerton College: 69 degrees and certificates in business, accounting, paralegal studies, and technology."}">\n'
            f'{FONTS}\n<style>\n{css}\n</style>\n'
            + header.replace("{{NAV_PROGRAMS}}", "" if is_index else 'aria-current="page"')
            + body.replace("{{PROGRAMS}}", programs_html()).replace("{{AWARD_TOTAL}}", str(TOTAL)) + footer)
    for k, v in TOK.items():
        html = html.replace(k, v)
    if SITE:
        html = html.replace('<meta name="claude:viewport-fit-sides" content="cover">', '<meta name="robots" content="noindex, nofollow">')
        html = html.replace('<a class="skip" href="#main">Skip to content</a>',
            '<a class="skip" href="#main">Skip to content</a><div class="preview-bar">Design preview for faculty review. Not the official site. '
            'Send comments to Gary Graves, ggraves@fullcoll.edu, or <a href="https://github.com/profgarygraves/buscis-2026-website/issues">open an issue on GitHub</a>.</div>', 1)
    if SITE or not is_index:  # standalone pages need their own skeleton
        html = ('<!doctype html>\n<html lang="en"><head><meta charset="utf-8">'
                '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
                + html.replace('</style>\n', '</style>\n</head><body>\n', 1) + '\n</body></html>')
    assert "{{" not in html, title
    return link_names(html)

(OUT / "index.html").write_text(page("Business & CIS Division", (S / "index.body.html").read_text(), True))
for k, p in P.items():
    (OUT / p["file"]).write_text(page(p["name"].replace("&amp;", "&"), program_page(k), False, (p["name"] + " at Fullerton College: " + p["desc"]).replace("&amp;", "&")))
(OUT / "faculty.html").write_text(page("Faculty & Staff", faculty_page(), False, "Faculty and staff directory for the Fullerton College Business & CIS Division: Accounting, Business Management, CIS, and Paralegal Studies."))
for pg in PAGES:
    (OUT / pg["file"]).write_text(page(pg["title"].replace("&amp;", "&"), content_page(pg), False, re.sub("<[^>]+>", "", pg["lead"]).replace("&amp;", "&")))
if SITE:
    import shutil
    shutil.copytree(ROOT / "img", OUT / "img", dirs_exist_ok=True)
    (OUT / ".nojekyll").write_text("")
print("built", 2 + len(P) + len(PAGES), "pages;", TOTAL, "awards")
