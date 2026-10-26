"""Build the Business & CIS Division site in English and Spanish.

    python3 build.py          # writes the GitHub Pages site to docs/ (English) and docs/es/ (Spanish)

Mirrors the planned PHP structure on the live server:
  inc/header.php, inc/footer.php, inc/programs.php (data), program.php (template)
"""
import pathlib, sys, re, shutil
ROOT = pathlib.Path(__file__).parent
S = ROOT / "src"; OUT = ROOT / "docs"
sys.path.insert(0, str(S))
from programs import P, GROUPS, JOBS, SCHED, LEADS, JOB_SOC, PATHWAYS, PW, CAREER_SOURCES
from programs_es import ES, GROUPS_ES, TAGS_ES, JOBS_ES, AREA_ES, ROLE_ES, DEPTS_ES
from people import STAFF, DEPTS, FACULTY, SOCIAL, CLUB, SCHEDULE_NAMES, LINKEDIN, NO_PHOTO
from urllib.parse import quote
from pages import PAGES, COUNSELORS, ESARS
import rotation as ROT
from clubs import CLUBS
from pages_es import PAGES_ES
from i18n import t

def L(lang, en, es):
    return en if lang == "en" else es

def ico(d):
    return ('<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{d}</svg>')

SICON = {
 "Facebook": '<svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M13.5 22v-8h2.7l.4-3.2h-3.1V8.8c0-.9.3-1.6 1.6-1.6h1.7V4.4c-.3 0-1.3-.1-2.5-.1-2.5 0-4.1 1.5-4.1 4.2v2.3H7.5V14h2.7v8z"/></svg>',
 "Instagram": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg>',
 "LinkedIn": '<svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M4 9h3.6v11H4zM5.8 3.5a2.1 2.1 0 1 1 0 4.2 2.1 2.1 0 0 1 0-4.2zM9.8 9h3.4v1.6c.5-.9 1.7-1.9 3.5-1.9 3.7 0 4.3 2.4 4.3 5.5V20h-3.6v-5.1c0-1.2 0-2.8-1.7-2.8s-2 1.3-2 2.7V20H9.8z"/></svg>',
 "YouTube": '<svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M22 8.2a3 3 0 0 0-2.1-2.1C18 5.6 12 5.6 12 5.6s-6 0-7.9.5A3 3 0 0 0 2 8.2 31 31 0 0 0 1.6 12 31 31 0 0 0 2 15.8a3 3 0 0 0 2.1 2.1c1.9.5 7.9.5 7.9.5s6 0 7.9-.5a3 3 0 0 0 2.1-2.1 31 31 0 0 0 .4-3.8 31 31 0 0 0-.4-3.8zM10 15V9l5.2 3z"/></svg>',
}
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
 "{{SCHED}}": "https://schedule.nocccd.edu/?college=2",
 "{{CLUB}}": CLUB,
 "{{ESARS}}": ESARS,
 "{{SOCIAL_ICONS}}": "".join(f'<li><a href="{u}" aria-label="{n} {h}">{SICON[n]}</a></li>' for n, h, u in SOCIAL),
 "{{SOCIAL_LIST}}": "".join(f'<li><a href="{u}">{SICON[n]}<span>{n} <small>{h}</small></span></a></li>' for n, h, u in SOCIAL),
}
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700'
         '&amp;family=Questrial&amp;family=Sorts+Mill+Goudy&amp;display=swap">')

BY_EMAIL = {f[1]: f for f in FACULTY}
DEPT_COLOR = {"acct": "law", "bus": "biz", "cis": "tech", "pleg": "para", "staff": "biz"}
TAGS = {"biz": "Business &amp; Management", "law": "Accounting &amp; Paralegal Studies", "para": "Paralegal Studies", "tech": "Technology"}

def pv(key, field, lang):
    """Program value in the requested language (falls back to English)."""
    if lang == "es" and field in ES.get(key, {}):
        return ES[key][field]
    return P[key].get(field)

def tr_area(s, lang): return AREA_ES.get(s, s) if lang == "es" else s
def tr_role(s, lang): return ROLE_ES.get(s, s) if lang == "es" else s

def slug(name):
    return re.sub(r"[^a-z]+", "-", name.split(",")[0].lower().replace("dr. ", "")).strip("-")

def initials(name):
    parts = [w for w in name.split(",")[0].replace("Dr. ", "").split() if w[0].isalpha()]
    return (parts[0][0] + parts[-1][0]).upper()

PHOTO_ALIASES = {"santalia-carter": "sandy-santalia-carter", "brenda-klingenmaier": "brenda-terry-klingenmaier",
                 "steve-john-haddadin": "steve-haddadin", "kathy-standen": "kathleen-standen"}
def photo(name):
    s = slug(name); s = PHOTO_ALIASES.get(s, s)
    return f"img/people/{s}.jpg" if (ROOT / "img" / "people" / f"{s}.jpg").exists() else None

def person(name, role="", area="", email="", phone="", dept="bus", lang="en", row=False):
    # Live site (PHP): if file_exists("img/people/{slug}.jpg") print <img>, else the initials tile.
    src = photo(name); R = "" if lang == "en" else "../"
    ph = (f'<div class="ph c-{DEPT_COLOR[dept]}"><img src="{R}{src}" alt="" loading="lazy" width="600" height="750"></div>' if src
          else f'<div class="ph c-{DEPT_COLOR[dept]}" aria-hidden="true"><span>{initials(name)}</span></div>')
    role = " &middot; ".join(tr_role(r.strip(), lang) for r in role.split(" &middot; ")) if role else ""
    meta = (f'<p class="nm">{name}</p>' + (f'<p class="rl">{role}</p>' if role else "")
            + (f'<p class="ar">{tr_area(area, lang)}</p>' if area else "")
            + (f'<p class="ct">{phone}</p>' if phone else "")
            + (f'<p class="ct mail">{email}</p>' if email else "")
            + (f'<p class="li"><a href="{LINKEDIN[email]}">{SICON["LinkedIn"]}LinkedIn<span class="sr-only">: {name}</span></a></p>' if email in LINKEDIN else "")
            + (f'<p class="cls"><a href="https://schedule.nocccd.edu/?college=2{("&amp;term=" + SCHEDULE_NAMES[email][1]) if SCHEDULE_NAMES[email][1] else ""}&amp;instr={quote(SCHEDULE_NAMES[email][0])}">'
               f'{L(lang, "Find classes", "Ver sus clases")}<span class="sr-only"> {L(lang, "taught by", "de")} {name}</span> &rarr;</a></p>'
               if email in SCHEDULE_NAMES else ""))
    if row or email in NO_PHOTO:  # text-only listing: no photo or initials tile
        return f'<li class="person prow"><div class="pm">{meta}</div></li>'
    return f'<li class="person">{ph}<div class="pm">{meta}</div></li>'

def last_name(n):
    w = n.split()
    return (w[-2] + " " + w[-1]) if len(w) > 2 and w[-2] in ("St.", "de", "Van") else w[-1]

def lead_of(key):
    f = BY_EMAIL[LEADS[key]]
    return f[0], f[1], f[2]

def lead_roles(email, lang):
    return [pv(k, "name", lang) for k, e in LEADS.items() if e == email]

def lead_line(key, lang):
    n, e, d = lead_of(key)
    src = photo(n); R = "" if lang == "en" else "../"
    av = f'<img src="{R}{src}" alt="">' if src else initials(n)
    return (f'<p class="leadline"><span class="av c-{DEPT_COLOR[d]}" aria-hidden="true">{av}</span>'
            f'<span><span class="k">{t("program_lead", lang)}</span><b>Prof. {n}</b></span></p>')

# ---------- awards ----------
PILL = {"en": {"AST": "AS-T", "AA": "AA", "AS": "AS", "C": "Cert", "SK": "Skills"},
        "es": {"AST": "AS-T", "AA": "AA", "AS": "AS", "C": "Cert.", "SK": "Habil."}}
FULL = {"en": {"AST": "AS-T degree", "AA": "AA degree", "AS": "AS degree"},
        "es": {"AST": "Título AS-T", "AA": "Título AA", "AS": "Título AS"}}
TOTAL = sum(len(p["awards"]) for p in P.values())

def kind_label(k, lang):
    return FULL[lang].get(k) or L(lang, "Skills certificate" if k == "SK" else "Certificate",
                                  "Certificado de habilidades" if k == "SK" else "Certificado")

def summary_chips(aw, lang):
    deg = [a for a in aw if a["kind"] in FULL["en"]]; cer = [a for a in aw if a["kind"] in ("C", "SK")]
    out = []
    if len(deg) == 1: out.append(FULL[lang][deg[0]["kind"]])
    elif deg: out.append(L(lang, f"{len(deg)} degrees", f"{len(deg)} títulos"))
    if cer: out.append(L(lang, "1 certificate" if len(cer) == 1 else f"{len(cer)} certificates",
                             "1 certificado" if len(cer) == 1 else f"{len(cer)} certificados"))
    return "".join(f"<span>{c}</span>" for c in out)

def awards_block(key, lang):
    p = P[key]; name = pv(key, "name", lang)
    en = ' lang="en"' if lang == "es" else ""
    items = "".join(f'<li><a href="{a["url"]}"><span class="pill k-{a["kind"]}">{PILL[lang][a["kind"]]}</span><span{en}>{a["name"]}</span></a></li>' for a in p["awards"])
    return (f'<details class="aw"><summary><span class="aw-chips">{summary_chips(p["awards"], lang)}</span>'
            f'<span class="aw-more"><span class="when-closed">{t("show_all", lang)}</span><span class="when-open">{t("hide", lang)}</span>'
            f'<span class="sr-only"> {t("awards_of", lang, p=name)}</span></span></summary><ul class="awlist">{items}</ul></details>')

def starts(key, lang):
    titles = pv(key, "starts", lang) if lang == "es" else None
    return [(kw, code, (titles[i] if titles else tt)) for i, (kw, code, tt) in enumerate(P[key]["starts"])]

def start_line(key, lang):
    st = starts(key, lang); with_title = len(st) == 1
    parts = [f'<a href="{SCHED}{kw}"><b>{code}</b>{" " + tt if with_title else ""}</a>' for kw, code, tt in st]
    return (f'<p class="start">{{{{FLAG}}}}<span><span class="k">{t("start_here", lang)}</span>'
            f'{(" " + t("or", lang) + " ").join(parts)}</span></p>')

# ---------- homepage cards ----------
def card(key, lang):
    p = P[key]; c = p["color"]; name = pv(key, "name", lang)
    tag = pv(key, "tag", lang) or L(lang, TAGS[c], TAGS_ES[c])
    new = f' <span class="new">{t("new", lang)}</span>' if p.get("new") else ""
    snap = pv(key, "snap", lang); snap = f'<p class="snap">{snap}</p>' if snap else ""
    links = (f'<div class="prog-links{" full" if p.get("featured") else ""}">'
             f'<a href="{p["file"]}">{t("explore", lang)}<span class="sr-only">: {name}</span> &rarr;</a>'
             f'<a href="{SCHED}{p["subj"]}">{t("classes", lang, s=p["subj"])}</a></div>')
    head = f'<a class="prog-head" href="{p["file"]}"><span class="tag">{tag}</span><h4>{name}{new}</h4></a>'
    desc = pv(key, "desc", lang)
    if p.get("featured"):
        hl = "".join(f"<li>{h}</li>" for h in pv(key, "highlights", lang))
        body = (f'<div><p>{desc}</p><ul class="list">{hl}</ul>{awards_block(key, lang)}</div>'
                f'<div class="featured-side">{start_line(key, lang)}{snap}{lead_line(key, lang)}</div>{links}')
        return f'<article class="prog a-{c} featured">{head}<div class="prog-body">{body}</div></article>'
    return (f'<article class="prog a-{c}">{head}<div class="prog-body"><p>{desc}</p>{awards_block(key, lang)}'
            f'{start_line(key, lang)}{snap}{lead_line(key, lang)}{links}</div></article>')

def programs_html(lang):
    out = []
    for gid, label, keys in GROUPS:
        label = L(lang, label, GROUPS_ES[gid])
        colors = list(dict.fromkeys(P[k]["color"] for k in keys))
        sw = "".join(f'<span class="swatch" style="background:var(--{c})" aria-hidden="true"></span>' for c in colors)
        out.append(f'<div class="group g-{gid}"><div class="group-label">{sw}<h3>{label}</h3>'
                   f'<span>{t("program_areas", lang, n=len(keys))}</span></div><div class="grid n{len(keys)}">'
                   + "".join(card(k, lang) for k in keys) + '</div></div>')
    return "\n".join(out)


def career_sources(lang):
    return "".join(f'<li><a href="{(ue if lang == "en" else us)}"{(" lang=\"en\"" if lang == "es" and ls == le else "")}>{(le if lang == "en" else ls)}</a> <span>{(de if lang == "en" else ds)}</span></li>'
                   for le, de, ue, ls, ds, us in CAREER_SOURCES)

def research_block(key, lang):
    name = pv(key, "name", lang)
    pw_label = (L(lang, f"Careers and course maps for {name}", f"Carreras y mapas de cursos de {name}") if key != "ai"
                else L(lang, "Business pathway careers and course maps", "Carreras y mapas de cursos de la ruta de Negocios"))
    pw_desc = (L(lang, "Every career Hornet Pathways matches to this program, with national pay and growth",
                 "Todas las carreras que Hornet Pathways relaciona con este programa, con salario y crecimiento nacional")
               if key != "ai" else L(lang, "The AI programs will be added to Hornet Pathways soon", "Los programas de IA se agregarán pronto a Hornet Pathways"))
    return (f'<div class="block research"><h2>{L(lang, "Research careers on your own", "Investiga carreras por tu cuenta")}</h2>'
            f'<p>{L(lang, "These free tools show what people in each field do, what they earn, and how many jobs are expected. Compare a few before you choose.", "Estas herramientas gratuitas muestran qué hacen las personas en cada área, cuánto ganan y cuántos empleos se esperan. Compara varias antes de decidir.")}</p>'
            f'<ul class="linklist"><li><a href="{PATHWAYS}{PW[key]}">{pw_label}</a> <span>{pw_desc}</span></li>{career_sources(lang)}</ul></div>')

# ---------- program pages ----------
PATHWAY = {
 "tech": ("Applied Technology, Engineering and Mathematics", "https://www.fullcoll.edu/hornet-pathways/"),
 "para": ("Public Service and Education", "https://pathways.fullcoll.edu/category/public-service-and-education/"),
 "biz": ("Business", "https://pathways.fullcoll.edu/category/business/"),
 "law": ("Business", "https://pathways.fullcoll.edu/category/business/"),
}

def program_page(key, lang):
    p = P[key]; c = p["color"]; name = pv(key, "name", lang)
    tag = pv(key, "tag", lang) or L(lang, TAGS[c], TAGS_ES[c])
    new = f' <span class="new">{t("new", lang)}</span>' if p.get("new") else ""
    st = starts(key, lang); first = st[0]
    nd = len([a for a in p["awards"] if a["kind"] in FULL["en"]]); nc = len(p["awards"]) - nd
    if lang == "en":
        aw = ", ".join(x for x in [f"{nd} degree{'s' if nd != 1 else ''}" if nd else "", f"{nc} certificate{'s' if nc != 1 else ''}" if nc else ""] if x)
    else:
        aw = ", ".join(x for x in [f"{nd} título{'s' if nd != 1 else ''}" if nd else "", f"{nc} certificado{'s' if nc != 1 else ''}" if nc else ""] if x)
    pw_name, pw_url = PATHWAY[c]
    ln, le, ld = lead_of(key)
    facts = [(t("start_here", lang), f" {t('or', lang)} ".join(f'<a href="{SCHED}{kw}"><b>{code}</b></a> {tt}' for kw, code, tt in st)),
             (L(lang, "Awards", "Títulos y certificados"), aw),
             ("Hornet Pathway", f'<a href="{pw_url}"{" lang=\"en\"" if lang == "es" else ""}>{pw_name}</a>'),
             (t("program_lead", lang), f'Prof. {ln}<br>{le}')]
    facts_html = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in facts)

    en = ' lang="en"' if lang == "es" else ""
    rows = "".join(f'<tr><td><a href="{a["url"]}"{en}>{a["name"]}</a></td><td><span class="pill{" deg" if a["kind"] in FULL["en"] else ""}">'
                   f'{kind_label(a["kind"], lang)}</span></td></tr>' for a in p["awards"])
    blocks = [f'<div class="block"><h2>{L(lang, "About the program", "Sobre el programa")}</h2>{"".join(f"<p>{x}</p>" for x in pv(key, "overview", lang))}</div>']
    if p.get("notice"):
        blocks.append(f'<div class="block notice"><p><strong>{L(lang, "Important notice.", "Aviso importante.")}</strong> {pv(key, "notice", lang)}</p></div>')
    blocks.append(f'<div class="block"><h2>{L(lang, "Choose your award", "Elige tu título o certificado")}</h2><div class="tablebox"><table>'
                  f'<thead><tr><th scope="col">{L(lang, "Award", "Título o certificado")}</th><th scope="col">{L(lang, "Type", "Tipo")}</th></tr></thead>'
                  f'<tbody>{rows}</tbody></table></div><p class="small">'
                  + L(lang, "Each award links to its official catalog page for required courses and units.",
                      "Cada título o certificado enlaza a su página oficial del catálogo, en inglés, con los cursos y unidades requeridos.") + '</p></div>')
    if p.get("events"):
        ev = "".join(f'<li><b>{n}</b> <span class="when">{w}</span><br>{d}</li>' for n, w, d in pv(key, "events", lang))
        blocks.append(f'<div class="block"><h2>{L(lang, "Events every semester", "Eventos cada semestre")}</h2><ul class="events">{ev}</ul></div>')
    if p["jobs"]:
        bach = L(lang, "Bachelor&#8217;s", "Licenciatura")
        prof = L(lang, "https://www.onetonline.org/link/summary/", "https://www.miproximopaso.org/profile/summary/")
        jr = "".join(f'<tr><td><a href="{prof}{JOB_SOC[j]}">{L(lang, JOBS[j][0], JOBS_ES[j])}</a>{f" <span class=\"pill\">{bach}</span>" if JOBS[j][3] else ""}</td>'
                     f'<td class="num">{JOBS[j][1]}</td><td class="num">{JOBS[j][2]}{L(lang, "/hr", "/hora")}</td></tr>' for j in p["jobs"])
        blocks.append(f'<div class="block"><h2>{L(lang, "Where it can lead", "Hacia dónde puede llevarte")}</h2><div class="tablebox"><table>'
                      f'<thead><tr><th scope="col">{L(lang, "Occupation", "Ocupación")}</th><th scope="col">{L(lang, "OC jobs, 2024", "Empleos en OC, 2024")}</th>'
                      f'<th scope="col">{L(lang, "Median pay", "Mediana salarial")}</th></tr></thead><tbody>{jr}</tbody></table></div><p class="small">'
                      + L(lang, "Orange County data from Lightcast, as reported in the Fullerton College Institutional Effectiveness Report 2024-25. Roles marked Bachelor&#8217;s usually require a four-year degree. ",
                          "Datos del condado de Orange de Lightcast, citados en el Informe de Efectividad Institucional de Fullerton College 2024-25. Los puestos marcados con Licenciatura normalmente requieren un título universitario de cuatro años. ")
                      + L(lang, "Each occupation links to its O*NET profile with daily tasks, skills, and national pay. ",
                            "Cada ocupación enlaza a su perfil en Mi Próximo Paso, con tareas, habilidades y salario nacional. ")
                      + (pv(key, "jobs_note", lang) or "") + '</p></div>')
    blocks.append(research_block(key, lang))
    fac = sorted(p["faculty"], key=lambda f: f["email"] != LEADS[key])
    if not any(f["email"] == LEADS[key] for f in fac):
        fac.insert(0, {"name": ln, "email": le, "role": "", "area": BY_EMAIL[le][4]})
    def frole(f):
        if f["email"] != LEADS[key]: return f["role"]
        return "Program Lead" + (" &middot; " + f["role"] if f["role"] and f["role"] != "Program Lead" else "")
    fl = "".join(person(BY_EMAIL.get(f["email"], (f["name"],))[0], frole(f), f["area"], f["email"], "",
                        BY_EMAIL.get(f["email"], ("", "", "bus"))[2], lang) for f in fac)
    blocks.append(f'<div class="block"><h2>{L(lang, "Faculty", "Profesorado")}</h2><ul class="people compact">{fl}</ul>'
                  f'<p class="small"><a href="faculty.html">{L(lang, "See all division faculty", "Ver todo el profesorado de la división")} &rarr;</a></p></div>')

    plan = [(L(lang, f"Find {first[1]} in the schedule", f"Busca {first[1]} en el horario"), SCHED + first[0]),
            (L(lang, f'All {p["subj"]} classes this term', f'Todas las clases de {p["subj"]} de este semestre'), SCHED + p["subj"])]
    if p.get("map"): plan.append((L(lang, "Program map", "Mapa del programa"), p["map"]))
    plan += [(L(lang, "Course maps on Hornet Pathways", "Mapas de cursos en Hornet Pathways"), PATHWAYS + PW[key]),
             (L(lang, "Career education counselors", "Consejeros de educación profesional"), "counselors.html"),
             (L(lang, "Apply for a certificate", "Solicita un certificado"), "forms.html")]
    if p.get("rot"):  # department course rotation, after Hornet Pathways
        plan.insert(len(plan) - 2, (L(lang, "Course rotation: when classes are offered", "Rotación de cursos: cuándo se ofrecen"), "rotation.html#" + p["rot"]))
    plan_html = "".join(f'<li><a href="{u}">{x}</a></li>' for x, u in plan)
    docs = ""
    if p.get("docs"):
        docs = (f'<div class="aside-card"><h2>{L(lang, "Program documents", "Documentos del programa")}</h2><ul>'
                + "".join(f'<li><a href="{u}"{en}>{x}</a></li>' for x, u in p["docs"]) + '</ul></div>')
    hl = "".join(f"<li>{h}</li>" for h in pv(key, "highlights", lang))
    clubmap = {c["id"]: c for c in CLUBS}
    cl = [clubmap[i] for i in p.get("clubs", []) if i in clubmap]
    clubs_card = ("" if not cl else f'<div class="aside-card"><h2>{L(lang, "Join a club", "Únete a un club")}</h2><ul>'
                  + "".join(f'<li><a href="clubs.html#{c["id"]}" lang="en">{c["name"]}</a></li>' for c in cl) + '</ul></div>')
    site = ""
    if p.get("site"):
        su, sn, sd_en, sd_es = p["site"]
        site = (f'<div class="aside-card highlight"><h2>{L(lang, "Visit the program site", "Visita el sitio del programa")}</h2>'
                f'<p class="small" style="margin:0 0 8px">{L(lang, sd_en, sd_es)}</p>'
                f'<ul><li><a href="{su}"' + ('' if lang == "en" else ' lang="en"') + f'>{sn}</a></li></ul></div>')
    rel = "".join(f'<a class="a-{P[r]["color"]}" href="{P[r]["file"]}">{pv(r, "name", lang)}<span>{pv(r, "desc", lang).split(".")[0]}.</span></a>' for r in p["related"])
    crumbs = (f'<nav class="crumbs" aria-label="{L(lang, "Breadcrumb", "Ruta de navegación")}"><a href="index.html">{t("crumb_home", lang)}</a> &rsaquo; '
              f'<a href="index.html#programs">{t("nav_programs", lang)}</a> &rsaquo; <span aria-current="page">{name}</span></nav>')

    return f'''<main id="main">
<section class="phero a-{c}" aria-labelledby="page-h">
  <div class="wrap">
    <div>
      {crumbs}
      <p class="tag">{tag}</p>
      <h1 id="page-h">{name}{new}</h1>
      <p>{pv(key, "lead", lang)}</p>
      <div class="btns">
        <a class="btn btn-primary" href="{SCHED}{first[0]}">{L(lang, f"Find {first[1]} in the schedule", f"Busca {first[1]} en el horario")}</a>
        <a class="btn btn-ghost on-color" href="#awards">{L(lang, "See degrees &amp; certificates", "Ver títulos y certificados")}</a>
      </div>
    </div>
    <section class="facts" aria-labelledby="qf"><h2 id="qf">{L(lang, "Quick facts", "Datos rápidos")}</h2><dl>{facts_html}</dl></section>
  </div>
</section>
<section class="section" aria-label="{L(lang, "Program details", "Detalles del programa")}">
  <div class="wrap two">
    <div class="prose" id="awards">{"".join(blocks)}</div>
    <section class="sidebar" aria-label="{L(lang, "Program links", "Enlaces del programa")}">
      <div class="aside-card highlight"><h2>{L(lang, "Highlights", "Lo más destacado")}</h2><ul class="ticks">{hl}</ul></div>
      {site}
      <div class="aside-card"><h2>{L(lang, "Plan your classes", "Planea tus clases")}</h2><ul>{plan_html}</ul></div>
      {clubs_card}{docs}
    </section>
  </div>
</section>
<section class="section" style="padding-top:0" aria-labelledby="rel-h">
  <div class="wrap"><h2 id="rel-h" class="rel-h">{L(lang, "Related programs", "Programas relacionados")}</h2><div class="related">{rel}</div></div>
</section>
<p class="wrap reviewed">{t("reviewed", lang)}</p>
</main>
'''

# ---------- faculty & staff ----------
def faculty_page(lang):
    staff = "".join(person(n, ti, "", e, ph, "staff", lang) for n, ti, ph, e in STAFF)
    dname = lambda k, v: L(lang, v, DEPTS_ES[k])
    radios = (f'<input type="radio" name="dept" id="d-all" checked><label for="d-all">{L(lang, "All departments", "Todos los departamentos")}</label>'
              + "".join(f'<input type="radio" name="dept" id="d-{k}"><label for="d-{k}"><i style="background:var(--{DEPT_COLOR[k]})"></i>{dname(k, v)}</label>' for k, v in DEPTS))
    hide = ",\n".join(f".dir:has(#d-{k}:checked) .dept:not(.dp-{k})" for k, _ in DEPTS)
    secs = []
    for k, v in DEPTS:
        ppl = sorted([f for f in FACULTY if f[2] == k], key=lambda f: (photo(f[0]) is None, last_name(f[0]), f[0]))
        def frole(f):
            parts = [tr_role(f[3], lang)] if f[3] else []
            if f[1] in dict((e, 1) for e in LEADS.values()):
                parts.append(t("Program Lead", lang) + ": " + ", ".join(lead_roles(f[1], lang)))
            return " &middot; ".join(parts)
        cards = "".join(person(f[0], frole(f), f[4], f[1], "", k, lang) for f in ppl if f[1] not in NO_PHOTO)
        rows = "".join(person(f[0], frole(f), f[4], f[1], "", k, lang, row=True) for f in ppl if f[1] in NO_PHOTO)
        more = (f'<h4 class="more-h">{L(lang, "More " + v + " faculty", "Más docentes de " + DEPTS_ES[k])}</h4><ul class="people-list">{rows}</ul>' if rows else "")
        n = len(ppl)
        secs.append(f'<section class="dept dp-{k}" aria-labelledby="h-{k}"><div class="group-label"><span class="swatch" style="background:var(--{DEPT_COLOR[k]})" aria-hidden="true"></span>'
                    f'<h3 id="h-{k}">{dname(k, v)}</h3><span>{n} {L(lang, "faculty", "docentes")}</span></div><ul class="people">{cards}</ul>{more}</section>')
    lead = L(lang, f"{len(FACULTY)} faculty across four departments, plus the division office team. Faculty with a photo are listed first, then everyone else, alphabetically by last name.",
             f"{len(FACULTY)} docentes en cuatro departamentos, además del equipo de la oficina de la división. Primero aparecen los docentes con foto y después los demás, en orden alfabético por apellido.")
    return f"""<style>{hide}{{display:none}}</style>
<main id="main">
<section class="hero slim"><div class="wrap"><div>
  <nav class="crumbs" aria-label="{L(lang, "Breadcrumb", "Ruta de navegación")}"><a href="index.html">{t("crumb_home", lang)}</a> &rsaquo; <span aria-current="page">{t("nav_faculty", lang)}</span></nav>
  <h1>{t("nav_faculty", lang)}</h1>
  <p class="lead">{lead}</p>
</div></div></section>
<section class="section" aria-labelledby="office-staff-h"><div class="wrap">
  <div class="section-head"><div><h2 id="office-staff-h">{L(lang, "Division office", "Oficina de la división")}</h2><p>{t("room", lang)} &middot; buscis@fullcoll.edu &middot; 714-992-7032</p></div></div>
  <ul class="people staff">{staff}</ul>
</div></section>
<section class="section dir" style="padding-top:0" aria-labelledby="fac-h"><div class="wrap">
  <div class="section-head"><div><h2 id="fac-h">{L(lang, "Faculty", "Profesorado")}</h2><p>{L(lang, "Office hours are posted in each course in Canvas.", "El horario de atención aparece en cada curso de Canvas.")}</p></div>
  <fieldset class="filter"><legend class="sr-only">{L(lang, "Show faculty by department", "Mostrar profesorado por departamento")}</legend>{radios}</fieldset></div>
  {"".join(secs)}
</div></section>
<p class="wrap reviewed">{t("reviewed", lang)}</p>
</main>
"""

# ---------- resource pages ----------
MODES = {"D": ("Day", "Diurno"), "N": ("Night", "Nocturno"), "S": ("Saturday", "Sábado"),
         "O": ("Online", "En línea"), "Y": ("Offered", "Se ofrece")}
LENGTHS = {"16-8": ("16 or 8 weeks", "16 u 8 semanas"), "8a": ("first 8 weeks", "primeras 8 semanas"),
           "8b": ("second 8 weeks", "segundas 8 semanas"), "88": ("either 8-week session", "cualquier sesión de 8 semanas")}
TERMS = {"fall": ("Fall", "Otoño"), "spring": ("Spring", "Primavera"), "summer": ("Summer", "Verano"), "winter": ("Winter", "Invierno")}

def rot_table(rows, terms, lang, caption, groups=None):
    """Course rotation table. rows: (course, title, fall, spring, summer, winter, note)."""
    idx = {"fall": 2, "spring": 3, "summer": 4, "winter": 5}
    def note(n):
        if not n: return ""
        if isinstance(n, tuple): return L(lang, n[0], n[1])
        return L(lang, n, n.replace("Formerly", "Antes"))
    allrows = [r for _, rs in groups for r in rs] if groups else rows
    has_note = any(r[6] for r in allrows)
    head = (f'<th scope="col">{L(lang, "Course", "Curso")}</th>'
            + "".join(f'<th scope="col">{L(lang, *TERMS[t])}</th>' for t in terms)
            + (f'<th scope="col">{L(lang, "Notes", "Notas")}</th>' if has_note else ""))
    ncol = 1 + len(terms) + (1 if has_note else 0)
    def cell(v):
        if not v:
            return f'<td class="off"><span aria-hidden="true">&mdash;</span><span class="sr-only">{L(lang, "Not offered", "No se ofrece")}</span></td>'
        toks = v.split() if (" " in v or ":" in v) else list(v)
        out = []
        for tk in toks:
            m, _, ln = tk.partition(":")
            out.append(L(lang, *MODES[m]) + (f' <span class="len">({L(lang, *LENGTHS[ln])})</span>' if ln else ""))
        return "<td>" + "<br>".join(out) + "</td>"
    def tr(r):
        return (f'<tr><th scope="row"><b>{r[0]}</b><br><span class="small" lang="en">{r[1]}</span></th>'
                + "".join(cell(r[idx[t]]) for t in terms)
                + (f'<td class="small">{note(r[6])}</td>' if has_note else "") + "</tr>")
    if groups:
        body = "".join(f'<tr class="grp"><th scope="colgroup" colspan="{ncol}">{g}</th></tr>' + "".join(tr(r) for r in rs) for g, rs in groups)
    else:
        body = "".join(tr(r) for r in rows)
    return (f'<div class="tablebox" role="region" tabindex="0" aria-label="{caption}"><table class="rot"><caption class="sr-only">{caption}</caption>'
            f'<thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>')

def rotation_html(lang):
    fs = ["fall", "spring"]; fss = ["fall", "spring", "summer"]; all4 = ["fall", "spring", "summer", "winter"]
    none = ", ".join(f'{c}' for c, _ in ROT.CIS_NONE)
    f4 = ["fall", "spring", "summer", "winter"]
    def nonelist(rows):
        if not rows: return ""
        return f'<p class="small">{L(lang, "Not on the current rotation", "No están en la rotación actual")}: ' + ", ".join(f"{c} ({t})" for c, t in rows) + ".</p>"
    biz = (f'<div class="block" id="business"><h2>{L(lang, "Business Management", "Gestión Empresarial")}</h2>'
      + f'<p>{L(lang, "Includes the Business, Entrepreneurship, and AI in Business courses. Many online classes run in 8-week sessions: the first or second half of the semester.", "Incluye los cursos de Negocios, Emprendimiento e IA en los Negocios. Muchas clases en línea duran 8 semanas: la primera o la segunda mitad del semestre.")}</p>'
      + rot_table(ROT.BUS_ROWS, f4, lang, L(lang, "Business course rotation", "Rotación de cursos de Negocios")) + nonelist(ROT.BUS_NONE) + '</div>'
      + f'<div class="block" id="intl"><h2>{L(lang, "International Business", "Negocios Internacionales")}</h2>'
      + rot_table(ROT.INTL_ROWS, f4, lang, L(lang, "International Business course rotation", "Rotación de cursos de Negocios Internacionales")) + '</div>'
      + f'<div class="block" id="marketing"><h2>{L(lang, "Marketing", "Mercadotecnia")}</h2>'
      + rot_table(ROT.MKT_ROWS, f4, lang, L(lang, "Marketing course rotation", "Rotación de cursos de Mercadotecnia")) + nonelist(ROT.MKT_NONE) + '</div>'
      + f'<div class="block" id="realestate"><h2>{L(lang, "Real Estate", "Bienes Raíces")}</h2>'
      + rot_table(ROT.RE_ROWS, f4, lang, L(lang, "Real Estate course rotation", "Rotación de cursos de Bienes Raíces")) + nonelist(ROT.RE_NONE) + '</div>')
    return (biz +
      f'<div class="block" id="accounting"><h2>{L(lang, "Accounting", "Contabilidad")}</h2>'
      + rot_table(ROT.ACCT_ROWS, fss, lang, L(lang, "Accounting course rotation", "Rotación de cursos de Contabilidad"))
      + f'<p class="small"><a href="accounting.html">{L(lang, "Accounting program", "Programa de Contabilidad")} &rarr;</a></p></div>'
      + f'<div class="block" id="cis"><h2>{L(lang, "Computer Information Systems", "Sistemas de Información Computacional")}</h2>'
      + f'<p>{L(lang, "The CIS department schedules CIS, Computer Gaming, and Cyber Security courses. This rotation lists fall and spring; check the class schedule for summer and winter.", "El departamento de CIS programa los cursos de CIS, Videojuegos y Ciberseguridad. Esta rotación muestra otoño y primavera; consulta el horario de clases para verano e invierno.")}</p>'
      + f'<h3 id="cis-courses">CIS</h3>' + rot_table(ROT.CIS_ROWS, fs, lang, L(lang, "CIS course rotation", "Rotación de cursos de CIS"))
      + f'<h3 id="gaming">{L(lang, "Computer Gaming", "Videojuegos")}</h3>' + rot_table(ROT.CISG_ROWS, fs, lang, L(lang, "Computer Gaming course rotation", "Rotación de cursos de Videojuegos"))
      + f'<h3 id="cyber">{L(lang, "Cyber Security", "Ciberseguridad")}</h3>' + rot_table(ROT.CYBR_ROWS, fs, lang, L(lang, "Cyber Security course rotation", "Rotación de cursos de Ciberseguridad"))
      + f'<details class="more"><summary>{L(lang, f"{len(ROT.CIS_NONE)} other CIS courses are not on the current rotation", f"Otros {len(ROT.CIS_NONE)} cursos de CIS no están en la rotación actual")}</summary>'
      + f'<p class="small">{none}. {L(lang, "Ask the division office if you need one of these courses.", "Pregunta en la oficina de la división si necesitas alguno de estos cursos.")}</p></details></div>'
      + f'<div class="block" id="paralegal"><h2>{L(lang, "Paralegal Studies", "Estudios Paralegales")}</h2>'
      + rot_table(None, all4, lang, L(lang, "Paralegal Studies course rotation", "Rotación de cursos de Estudios Paralegales"),
                  groups=[(L(lang, "Required courses", "Cursos obligatorios"), ROT.PLEG_REQUIRED), (L(lang, "Elective courses", "Cursos optativos"), ROT.PLEG_ELECTIVE)])
      + '<ul class="small">'
      + f'<li>{L(lang, "Online means fully asynchronous, with one live Zoom orientation at the start of the semester.", "En línea significa totalmente asincrónico, con una sola orientación en vivo por Zoom al inicio del semestre.")}</li>'
      + f'<li>{L(lang, "Students must take at least 9 units of legal specialty courses in live (synchronous) classes.", "Debes tomar al menos 9 unidades de cursos de especialidad legal en clases en vivo (sincrónicas).")}</li>'
      + f'<li>{L(lang, "Even and odd years refer to the calendar year of the term.", "Los años pares e impares se refieren al año calendario del semestre.")}</li></ul>'
      + f'<p class="small"><a href="paralegal.html">{L(lang, "Paralegal Studies program", "Programa de Estudios Paralegales")} &rarr;</a></p></div>'
      )

SICON_EXTRA = {
 "TikTok": '<svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M16.6 3c.3 2.3 1.6 3.8 3.9 4v3.2c-1.4.1-2.6-.3-3.9-1.1v6.1c0 4.1-3.6 6.5-7 5.6-3.9-1.1-5-6-2.4-8.6 1.1-1.1 2.6-1.6 4.3-1.4v3.3c-.8-.2-1.7-.1-2.3.4-1.3 1-.9 3.4.9 3.7 1.4.2 2.3-.7 2.3-2.4V3z"/></svg>',
 "Twitch": '<svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M5 2 3 6v14h5v3h3l3-3h4l4-4V2zm15 13-3 3h-4l-3 3v-3H6V4h14zM15 7h2v6h-2zm-5 0h2v6h-2z"/></svg>',
}

def clubs_html(lang):
    R = "" if lang == "en" else "../"
    cards = []
    for c in CLUBS:
        logo = (f'<img class="club-logo" src="{R}{c["logo"]}" alt="{c.get("logo_alt", "")}" width="96" height="96">' if c["logo"]
                else f'<div class="club-logo tile" aria-hidden="true">{c.get("initials") or initials(c["name"])}</div>')
        dl = ""
        if c["advisor"]: dl += f'<dt>{L(lang, *c.get("advisor_label", ("Advisor", "Asesor")))}</dt><dd>{c["advisor"]}</dd>'
        if c["meets"][0]: dl += f'<dt>{L(lang, "Meets", "Reuniones")}</dt><dd>{L(lang, *c["meets"])}</dd>'
        soc = "".join(f'<li><a href="{u}">{(SICON.get(n) or SICON_EXTRA[n])}<span>{n}<span class="sr-only">: {h}</span></span></a></li>' for n, h, u in c["social"])
        j_en, j_es, ju = c["join"]
        cards.append(f'''<article class="club" id="{c["id"]}" aria-labelledby="h-{c["id"]}">
<div class="club-head">{logo}<div><h2 id="h-{c["id"]}" lang="en">{c["name"]}</h2><p class="club-tag">{L(lang, *c["tag"])}</p></div></div>
<p>{L(lang, *c["about"])}</p>{('<dl class="club-dl">' + dl + '</dl>') if dl else ""}
<p class="club-join"><a class="btn btn-primary" href="{ju}">{L(lang, j_en, j_es)}</a></p>{('<ul class="club-social" aria-label="' + L(lang, "Follow", "Síguenos") + ' ' + c["name"] + '">' + soc + '</ul>') if soc else ""}
</article>''')
    why = L(lang,
      '<div class="why"><h2>Why join a club?</h2><ul><li><b>Meet your people.</b> Find classmates who share your goals and study together.</li><li><b>Build your resume.</b> Leadership roles, events, and competitions show employers and universities what you can do.</li><li><b>Connect with faculty and professionals.</b> Advisors and guest speakers open doors to internships and jobs.</li></ul><p class="small">Clubs are free and open to Fullerton College students. Most welcome students from any major.</p></div>',
      '<div class="why"><h2>¿Por qué unirte a un club?</h2><ul><li><b>Conoce a tu gente.</b> Encuentra compañeros con tus mismas metas y estudien juntos.</li><li><b>Fortalece tu currículum.</b> Los puestos de liderazgo, eventos y competencias muestran a empleadores y universidades lo que puedes hacer.</li><li><b>Conecta con profesores y profesionales.</b> Los asesores y conferencistas abren puertas a prácticas y empleos.</li></ul><p class="small">Los clubes son gratuitos y abiertos a estudiantes de Fullerton College. La mayoría acepta estudiantes de cualquier carrera.</p></div>')
    return why + '<div class="clubs">' + "".join(cards) + '</div>'

def content_page(pg, lang):
    src = pg if lang == "en" else {**pg, **PAGES_ES[pg["file"]]}
    todo = (f'<div class="todo" role="note" lang="en"><b>{t("todo", "en")}</b> {pg["todo"]}</div>' if pg["todo"] else "")
    body = (src["body"].replace("{{COUNSELORS}}", "".join(person(n, ti, "", e, "", "staff", lang) for n, ti, e in COUNSELORS))
            .replace("{{CAREER_SOURCES}}", career_sources(lang))
            .replace("{{CLUBS}}", clubs_html(lang) if "{{CLUBS}}" in src["body"] else "")
            .replace("{{ROTATION}}", rotation_html(lang) if "{{ROTATION}}" in src["body"] else "")
            .replace("{{STAFF}}", "".join(person(n, ti, "", e, ph, "staff", lang) for n, ti, ph, e in STAFF)))
    return f"""<main id="main">
<section class="hero slim"><div class="wrap"><div>
  <nav class="crumbs" aria-label="{L(lang, "Breadcrumb", "Ruta de navegación")}"><a href="index.html">{t("crumb_home", lang)}</a> &rsaquo; {src["eyebrow"]} &rsaquo; <span aria-current="page">{src["title"]}</span></nav>
  <h1>{src["title"]}</h1><p class="lead">{src["lead"]}</p>
</div></div></section>
<section class="section" aria-label="{src["title"]}"><div class="wrap">{todo}{('<div class="two"><div class="prose">' + body + '</div><section class="sidebar" aria-label="' + L(lang, "Related links", "Enlaces relacionados") + '">' + src["aside"] + '</section></div>') if src["aside"] else ('<div class="prose wide">' + body + '</div>')}</div></section>
<p class="wrap reviewed">{t("reviewed", lang)}</p>
</main>
"""

# ---------- page shell ----------
NAME_LINKS = {"Gary Graves": "https://ggraves.faculty.fullcoll.edu/"}

def link_names(html):
    out, in_a, in_raw = [], 0, False
    for tok in re.split(r"(<[^>]+>)", html):
        if tok.startswith("<"):
            tl = tok.lower()
            if tl.startswith("<a ") or tl == "<a>": in_a += 1
            elif tl.startswith("</a"): in_a = max(0, in_a - 1)
            elif tl.startswith(("<title", "<style", "<script")): in_raw = True
            elif tl.startswith(("</title", "</style", "</script")): in_raw = False
            out.append(tok)
        elif in_a or in_raw:
            out.append(tok)
        else:
            for name, url in NAME_LINKS.items():
                tok = tok.replace(name, f'<a class="namelink" href="{url}">{name}</a>')
            tok = re.sub(r"\b([\w.+-]+@(?:fullcoll\.edu|gmail\.com))\b", r'<a href="mailto:\1">\1</a>', tok)
            out.append(tok)
    return "".join(out)

css = (S / "style.css").read_text()
HEADER = (S / "header.html").read_text()
FOOTER = (S / "footer.html").read_text()
RESOURCE_FILES = {"rotation.html", "forms.html", "counselors.html", "internships.html", "study-abroad.html", "career.html", "clubs.html"}

def fill_t(html, lang):
    return re.sub(r"\{\{t:([\w ]+)\}\}", lambda m: t(m.group(1), lang), html)

def page(file, title, body, lang, desc, section=None):
    other = "es" if lang == "en" else "en"
    lang_href = ("es/" if lang == "en" else "../") + file
    cur = {"programs": "", "resources": "", "faculty": "", "contact": ""}
    if section in cur:
        cur[section] = ' aria-current="page"' if section in ("faculty", "contact") else ' aria-current="true"'
    header = HEADER
    for k, v in cur.items():
        header = header.replace("{{CUR_" + k + "}}", v)
    preview = (f'<div class="preview-bar" role="region" aria-label="{L(lang, "Preview notice", "Aviso de vista previa")}">{t("preview", lang)} '
               f'<a href="https://github.com/profgarygraves/buscis-2026-website/issues">{t("preview_issue", lang)}</a>.</div>')
    header = header.replace("{{PREVIEW}}", preview).replace("{{LANG_HREF}}", lang_href).replace("{{LANG_OTHER}}", other)
    site = L(lang, "Business &amp; CIS Division | Fullerton College", "División de Negocios y CIS | Fullerton College")
    full_title = site if file == "index.html" else f"{title} | {site}"
    en_href, es_href = (file, "es/" + file) if lang == "en" else ("../" + file, file)
    head = (f'<!doctype html>\n<html lang="{lang}"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            f'<title>{full_title}</title>\n<meta name="robots" content="noindex, nofollow">\n'
            f'<meta name="description" content="{desc}">\n'
            f'<link rel="alternate" hreflang="en" href="{en_href}"><link rel="alternate" hreflang="es" href="{es_href}">\n'
            f'{FONTS}\n<style>\n{css}\n</style>\n</head><body>\n')
    html = head + fill_t(header, lang) + body.replace("{{PROGRAMS}}", programs_html(lang)).replace("{{AWARD_TOTAL}}", str(TOTAL)) + fill_t(FOOTER, lang) + "\n</body></html>"
    html = fill_t(html, lang)
    for k, v in TOK.items():
        html = html.replace(k, v)
    assert "{{" not in html, (file, lang, re.findall(r"\{\{[^}]*\}\}", html)[:3])
    return link_names(html)

def strip_tags(s):
    return re.sub("<[^>]+>", "", s).replace("&amp;", "&")

def build():
    if OUT.exists():
        for f in OUT.rglob("*.html"): f.unlink()
    (OUT / "es").mkdir(parents=True, exist_ok=True)
    n = 0
    for lang in ("en", "es"):
        d = OUT if lang == "en" else OUT / "es"
        idx = (S / ("index.body.html" if lang == "en" else "index.body.es.html")).read_text()
        home_desc = L(lang, f"Business and Computer Information Systems Division at Fullerton College: {TOTAL} degrees and certificates in business, accounting, paralegal studies, and technology.",
                      f"División de Negocios y Sistemas de Información Computacional de Fullerton College: {TOTAL} títulos y certificados en negocios, contabilidad, estudios paralegales y tecnología.")
        (d / "index.html").write_text(page("index.html", "", idx, lang, home_desc)); n += 1
        for k, p in P.items():
            nm = strip_tags(pv(k, "name", lang))
            (d / p["file"]).write_text(page(p["file"], pv(k, "name", lang), program_page(k, lang), lang,
                                            f'{nm}{L(lang, " at Fullerton College: ", " en Fullerton College: ")}{strip_tags(pv(k, "desc", lang))}', "programs")); n += 1
        (d / "faculty.html").write_text(page("faculty.html", t("nav_faculty", lang), faculty_page(lang), lang,
            L(lang, "Faculty and staff directory for the Fullerton College Business & CIS Division.", "Directorio del profesorado y personal de la División de Negocios y CIS de Fullerton College."), "faculty")); n += 1
        for pg in PAGES:
            src = pg if lang == "en" else PAGES_ES[pg["file"]]
            sec = "resources" if pg["file"] in RESOURCE_FILES else ("contact" if pg["file"] == "contact.html" else None)
            (d / pg["file"]).write_text(page(pg["file"], src["title"], content_page(pg, lang), lang, strip_tags(src["lead"]), sec)); n += 1
    shutil.copytree(ROOT / "img", OUT / "img", dirs_exist_ok=True)
    (OUT / ".nojekyll").write_text("")
    print("built", n, "pages (English and Spanish);", TOTAL, "awards")

if __name__ == "__main__":
    build()
