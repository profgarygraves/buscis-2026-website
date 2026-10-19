# Spanish versions of the resource pages in pages.py, keyed by file name.
# Form and office names that only exist in English keep lang="en". Needs review by a fluent speaker.
from pages import DYN, UP, linklist

PAGES_ES = {
 "forms.html": dict(title="Formularios y solicitudes", eyebrow="Recursos estudiantiles",
  lead="Cambia tu carrera, solicita un certificado, pide sustituir un requisito o impugna un prerrequisito. Un consejero puede ayudarte a elegir el formulario correcto.",
  body=f"""
<div class="block"><h2>Cambia tu carrera</h2>
<p>¿Quieres estudiar un programa de Negocios o CIS? Actualiza tu carrera con Admisiones y Registros para que tu consejero, tu plan educativo y tu ruta de <span lang="en">Hornet Pathways</span> coincidan con tu meta. Elige el título o certificado exacto que planeas obtener; las páginas de programas de este sitio enlazan a cada uno en el catálogo.</p>
<ul class="linklist"><li><a href="https://admissions.fullcoll.edu/major-changes/">Cambiar mi carrera (<span lang="en">Change My Major</span>)</a> <span>Admisiones y Registros, formulario en inglés</span></li></ul></div>
<div class="block"><h2>Certificados</h2>
<p>Las solicitudes de certificados de Negocios y CIS las procesa la Unidad de Evaluaciones de Admisiones y Registros. Presenta tu solicitud solo cuando hayas terminado todas tus clases y se hayan publicado tus calificaciones finales.</p>
<ul class="linklist"><li><a href="https://dynamicforms.ngwebsolutions.com/Submit/Page?form=0dbbf09f-d7bb-4ff3-8ef5-71ccd1684947&amp;section=1147703&amp;page=734430&amp;token=Jqj9sXaialUHA2W2lXQ4K9AxYxFg-ciqpJBfSzPChjE">Solicitud de certificado de la División de Negocios y CIS</a> <span>Formulario en inglés</span></li>
<li><a href="{DYN}2bdcb592-f1de-45c1-aa14-4a0fc2fd5128">Petición para sustituir requisitos de certificado, División de Negocios y CIS</a> <span>Formulario en inglés</span></li></ul>
<p class="small">Preguntas sobre un certificado que ya solicitaste: evaluations@fullcoll.edu</p></div>
<div class="block"><h2>Títulos y graduación</h2>
<p>Las solicitudes de título y las fechas límite de graduación las maneja Admisiones y Registros.</p>
<ul class="linklist"><li><a href="https://admissions.fullcoll.edu/graduation/">Información y fechas límite de graduación</a> <span>Admisiones y Registros</span></li>
<li><a href="{DYN}e5b6c9e9-ebe1-479d-8fad-5051dbf0942c">Petición para sustituir requisitos de título y graduación</a> <span>Admisiones y Registros</span></li></ul></div>
<div class="block"><h2>Otros formularios</h2>
<ul class="linklist"><li><a href="{DYN}fed01d56-e084-4723-987e-a41811c1b9a3">Petición para repetir un curso</a> <span>Admisiones y Registros</span></li>
<li><a href="{DYN}b3c28569-bd33-44b3-b8b3-2bb215721352">Formulario para impugnar un prerrequisito o correquisito</a> <span>Admisiones y Registros</span></li></ul></div>""",
  aside="""<div class="aside-card"><h2>Ayuda con los formularios</h2><p class="small" style="margin:0 0 8px">Te recomendamos mucho reunirte primero con un consejero.</p><ul><li><a href="counselors.html">Consejeros de educación profesional</a></li></ul></div>"""),

 "counselors.html": dict(title="Consejeros", eyebrow="Recursos estudiantiles",
  lead="Los consejeros de educación profesional ayudan a los estudiantes de Negocios y CIS a crear un plan educativo, elegir un certificado o título, y planear su transferencia o su ingreso al trabajo.",
  body="""<div class="block"><h2>Consejeros de educación profesional</h2>
<ul class="people compact">{{COUNSELORS}}</ul>
<p><a class="btn btn-primary" href="{{ESARS}}">Haz una cita de consejería</a></p></div>
<div class="block"><h2>Horario de consejería de educación profesional</h2>
<div class="tablebox"><table><thead><tr><th>Día</th><th>Horario</th></tr></thead><tbody>
<tr><td>Lunes</td><td class="num">1 a 5 p.m.</td></tr><tr><td>Martes</td><td class="num">8 a.m. a 6 p.m.</td></tr>
<tr><td>Miércoles</td><td class="num">1 a 5 p.m.</td></tr><tr><td>Jueves</td><td class="num">8 a.m. a 5 p.m.</td></tr>
<tr><td>Viernes</td><td class="num">1 a 5 p.m.</td></tr></tbody></table></div>
<p class="small">Horario publicado para la primavera de 2026; puede cambiar.</p></div>""",
  aside="""<div class="aside-card"><h2>Más consejería</h2><ul>
<li><a href="https://counseling.fullcoll.edu/appointments/">Citas en el Centro de Consejería</a></li>
<li><a href="https://counseling.fullcoll.edu/hours-and-location/">Horario y ubicación del Centro de Consejería</a></li>
<li><a href="https://www.fullcoll.edu/hornet-pathways/">Mapas de programas de <span lang="en">Hornet Pathways</span></a></li>
<li><a href="https://admissions.fullcoll.edu/degreeworks-faq/">Conoce <span lang="en">DegreeWorks</span> (en inglés)</a></li></ul></div>"""),

 "internships.html": dict(title="Prácticas profesionales", eyebrow="Más allá del salón",
  lead="Obtén créditos universitarios mientras trabajas con un empleador local en un puesto relacionado con tu programa. Cuentan tanto los puestos pagados como los no pagados.",
  body=f"""<div class="block"><h2>Cursos de prácticas profesionales</h2>
<div class="tablebox"><table><thead><tr><th>Curso</th><th>Título</th><th>Unidades</th></tr></thead><tbody>
<tr><td><a href="https://schedule.nocccd.edu/?college=2&amp;keyword=BUS295"><b>BUS 295 F</b></a></td><td>Prácticas en negocios</td><td class="num">2 a 4</td></tr>
<tr><td><a href="https://schedule.nocccd.edu/?college=2&amp;keyword=CIS295"><b>CIS 295 F</b></a></td><td>Prácticas en sistemas de información computacional</td><td class="num">2 a 4</td></tr>
<tr><td><a href="https://schedule.nocccd.edu/?college=2&amp;keyword=PLEG210"><b>PLEG 210 F</b></a></td><td>Prácticas paralegales</td><td class="num">2</td></tr>
</tbody></table></div></div>
<div class="block"><h2>Unidades y horas de trabajo</h2>
<div class="tablebox"><table><thead><tr><th>Unidades</th><th>Horas de trabajo requeridas (además del curso)</th></tr></thead><tbody>
<tr><td class="num">2</td><td class="num">54 horas</td></tr><tr><td class="num">3</td><td class="num">108 horas</td></tr><tr><td class="num">4</td><td class="num">162 horas</td></tr></tbody></table></div>
<p class="small">Los créditos siguen el Título 5 del Código de Regulaciones de California. Puedes hacer más de una práctica mientras estés inscrito.</p></div>
<div class="block"><h2>Cómo empezar</h2>
<ol class="numbered"><li>Únete al espacio de Canvas de prácticas de la División de Negocios o llena el formulario de interés para estudiantes.</li>
<li>Inscríbete en BUS 295 F o CIS 295 F, según tu certificado o título.</li>
<li>Se te asigna un asesor del profesorado que te ayuda a cumplir los requisitos de la práctica.</li></ol>
<p>Debes ser estudiante inscrito de Fullerton College en la División de Negocios y haber completado cursos en el college.</p></div>""",
  aside=f"""<div class="aside-card highlight"><h2>Estudiantes</h2><ul>
<li><a href="https://fullcoll.instructure.com/enroll/FHDJDC">Únete al espacio de Canvas de prácticas</a></li>
<li><a href="https://forms.gle/ftybLC3G4PkHvWg26">Formulario de interés para estudiantes</a></li>
<li><a href="{UP}2020/05/001-BUS-CIS-Internship-student-brochure.pdf">Folleto para estudiantes (PDF en inglés)</a></li></ul></div>
<div class="aside-card"><h2>Empleadores</h2><ul>
<li><a href="https://forms.gle/GSSc6mFLR5vVfEsy5">Formulario de interés para empleadores</a></li>
<li><a href="{UP}2020/05/005-BUS-CIS-Internship-Employers-brochure.pdf">Folleto para empleadores (PDF en inglés)</a></li></ul></div>
<div class="aside-card"><h2>Contactos</h2><ul class="contacts">
<li><b>Negocios</b><span>Prof. Gary Graves, ggraves@fullcoll.edu</span></li>
<li><b>CIS y Ciberseguridad</b><span>Prof. Anna Carlin, acarlin@fullcoll.edu</span></li>
<li><b>Paralegal</b><span>Prof. Michael Moore, mmoore1@fullcoll.edu</span></li></ul></div>"""),

 "study-abroad.html": dict(title="Estudios en el extranjero", eyebrow="Más allá del salón",
  lead="Obtén unidades de Fullerton College mientras vives y aprendes en Florencia, Italia, en el otoño de 2028.",
  body="""<div class="block"><a href="https://studyabroad.fullcoll.edu/"><img class="flyer" src="../img/florence-2028.jpg" width="1400" height="933" alt="Estudia historia del arte, negocios y bienestar en Florencia, Italia, otoño de 2028. Visita studyabroad.fullcoll.edu." lang="es"></a></div>
<div class="block"><h2>Florencia, Italia: otoño de 2028</h2>
<p>Pasa un semestre de 13 semanas en <b>Florencia, Italia</b>, estudiando historia del arte, negocios y bienestar. El programa lo dirige el profesor Gary Graves de Fullerton College con la profesora Silvie Grote de Cypress College. Obtienes unidades de Fullerton College que cuentan para la educación general, tu carrera y la transferencia.</p>
<p class="notice" role="note"><b>Importante:</b> Este programa está pendiente de la aprobación de la Junta de Síndicos (<span lang="en">Board of Trustees</span>). Los cursos aún no son definitivos y pueden cambiar.</p>
<p><a class="btn btn-primary" href="https://studyabroad.fullcoll.edu/">Solicita o pregunta en studyabroad.fullcoll.edu</a></p></div>
<div class="block"><h2>Cursos planeados</h2>
<h3>Historia del arte y negocios, con el profesor Gary Graves</h3>
<div class="tablebox"><table><thead><tr><th scope="col">Curso</th><th scope="col">Título</th><th scope="col">Unidades</th><th scope="col">Área de GE de FC</th><th scope="col">Transferible a</th></tr></thead><tbody><tr><th scope="row"><a href="https://catalog.nocccd.edu/search/?caturl=%2Ffullerton-college&amp;search=BUS+240+F">BUS 240 F</a></th><td><span lang="en">Legal Environment of Business</span><br><span class="small">Honores disponible</span></td><td>3</td><td>4</td><td>CSU</td></tr><tr><th scope="row"><a href="https://catalog.nocccd.edu/search/?caturl=%2Ffullerton-college&amp;search=ARTH+155+F">ARTH 155 F</a></th><td><span lang="en">Western Art History: 15th to 21st Century</span><br><span class="small">Honores disponible</span></td><td>3</td><td>3</td><td>CSU</td></tr><tr><th scope="row"><a href="https://catalog.nocccd.edu/search/?caturl=%2Ffullerton-college&amp;search=BUS+211+F">BUS 211 F</a></th><td><span lang="en">Personal Critical Reasoning and Writing for Business Management</span><br><span class="small">Honores disponible</span></td><td>3</td><td>1B</td><td>CSU</td></tr><tr><th scope="row"><a href="https://catalog.nocccd.edu/search/?caturl=%2Ffullerton-college&amp;search=ARTH+100+F">ARTH 100 F</a></th><td><span lang="en">Introduction to Visual Culture</span><br><span class="small">Honores disponible</span></td><td>3</td><td>3</td><td>CSU</td></tr><tr><th scope="row"><a href="https://catalog.nocccd.edu/search/?caturl=%2Ffullerton-college&amp;search=BUS+185+F">BUS 185 F</a></th><td><span lang="en">Creativity Matters!</span></td><td>3</td><td>7</td><td>CSU</td></tr></tbody></table></div>
<h3>Salud y bienestar, con la profesora Silvie Grote</h3>
<div class="tablebox"><table><thead><tr><th scope="col">Curso</th><th scope="col">Título</th><th scope="col">Unidades</th><th scope="col">Área de GE de FC</th><th scope="col">Transferible a</th></tr></thead><tbody><tr><th scope="row"><a href="https://catalog.nocccd.edu/search/?caturl=%2Ffullerton-college&amp;search=PE+235+F">PE 235 F</a></th><td><span lang="en">First Aid, CPR, and Safety Education</span></td><td>3</td><td>—</td><td>CSU y UC</td></tr><tr><th scope="row"><a href="https://catalog.nocccd.edu/search/?caturl=%2Ffullerton-college&amp;search=HED+140+F">HED 140 F</a></th><td><span lang="en">Health Science</span></td><td>3</td><td>5</td><td>CSU y UC</td></tr><tr><th scope="row"><a href="https://catalog.nocccd.edu/search/?caturl=%2Ffullerton-college&amp;search=PE+121+F">PE 121 F</a></th><td><span lang="en">Walking for Fitness</span></td><td>1</td><td>7</td><td>CSU; UC limita el crédito</td></tr><tr><th scope="row"><a href="https://catalog.nocccd.edu/search/?caturl=%2Ffullerton-college&amp;search=PE+243+F">PE 243 F</a></th><td><span lang="en">Stress Management</span></td><td>3</td><td>7</td><td>CSU; UC limita el crédito</td></tr></tbody></table></div>
<p class="small">Las áreas de GE son para el título AA/AS de Fullerton College. ARTH 100 F y ARTH 155 F también cumplen el área 3 de Cal-GETC. Pregunta a un consejero cómo encaja cada curso en tu plan educativo.</p></div>
<div class="block"><h2>Cómo pagar tus estudios en el extranjero</h2>
<p>¿No sabes cómo pagarlo? Toma <a href="https://catalog.nocccd.edu/search/?caturl=%2Ffullerton-college&amp;search=BUS+186+F">BUS 186 F, <span lang="en">Funding Special Projects and New Ventures</span></a>. Aprenderás a encontrar becas y subvenciones para estudiar en el extranjero, organizar una campaña de financiamiento colectivo, presentar tu proyecto y hacer un presupuesto. La ayuda financiera también puede aplicarse a programas aprobados; pregunta en la oficina de Ayuda Financiera.</p>
<ul class="linklist"><li><a href="https://iefa.org/">IEFA: <span lang="en">International Education Financial Aid</span></a> <span>Búsqueda de becas (en inglés)</span></li>
<li><a href="https://studyabroad.state.gov/">Departamento de Estado de EE. UU.: estudios en el extranjero</a> <span>Planeación y seguridad (en inglés)</span></li>
<li><a href="https://financialaid.fullcoll.edu/">Ayuda Financiera de Fullerton College</a></li></ul></div>
<div class="block"><h2>Quién puede solicitar</h2>
<p>Los programas anteriores requerían al menos 12 unidades de trabajo universitario, incluido English 100 (College Writing) o su equivalente con C o más, un promedio (GPA) de 2.5 o más y una edad mínima de 18 años. Consulta en <a href="https://studyabroad.fullcoll.edu/">studyabroad.fullcoll.edu</a> los requisitos de este programa.</p></div>""",
  aside="""<div class="aside-card highlight"><h2>Oficina de Estudios en el Extranjero</h2><ul>
<li><a href="https://studyabroad.fullcoll.edu/">studyabroad.fullcoll.edu</a></li>
<li><a href="https://www.instagram.com/fcstudyabroad/">@fcstudyabroad en Instagram</a></li>
<li>studyabroad@fullcoll.edu</li></ul></div>
<div class="aside-card"><h2>Más sobre el programa</h2><ul>
<li><a href="https://ggraves.faculty.fullcoll.edu/study-abroad.html">Florencia 2028 en el sitio del profesor Graves</a> (en inglés)</li>
<li><a href="https://catalog.nocccd.edu/search/?caturl=%2Ffullerton-college&amp;search=BUS+186+F">BUS 186 F: cómo financiar tu viaje</a></li>
<li><a href="counselors.html">Reúnete con un consejero</a></li></ul></div>"""),

 "career.html": dict(title="Recursos profesionales", eyebrow="Más allá del salón",
  lead="Encuentra empleos y prácticas en Handshake, recibe comentarios sobre tu currículum, investiga carreras y vístete para la entrevista, con ayuda gratuita del Centro de Carreras de Fullerton College.",
  body="""<div class="block" id="jobs"><h2>Encuentra empleo en <span lang="en">Handshake</span></h2>
<p><span lang="en">Handshake</span> es la plataforma de empleos y prácticas profesionales de Fullerton College. Busca empleos y prácticas dentro y fuera del campus, conéctate con empleadores e inscríbete en ferias y eventos de empleo.</p>
<ol class="numbered"><li>Ve a <a href="https://fullcoll.joinhandshake.com/login">fullcoll.joinhandshake.com</a>.</li><li>Elige <b lang="en">Login using your Student ID</b>.</li><li>Inicia sesión con tu cuenta de estudiante de Fullerton College, el mismo usuario y contraseña de myGateway.</li><li>Completa tu perfil y sube tu currículum para que los empleadores te encuentren.</li></ol>
<p><a class="btn btn-primary" href="https://fullcoll.joinhandshake.com/login">Entra a <span lang="en">Handshake</span></a></p>
<p class="small">¿Es tu primera vez en <span lang="en">Handshake</span>? El Centro de Carreras ofrece un seminario web gratuito, <span lang="en">Handshake 101 Job Search</span>. Consulta las fechas en el <a href="https://careercenter.fullcoll.edu/calendar/">calendario del Centro de Carreras</a>.</p></div>
<div class="block" id="resume"><h2>Ayuda con tu currículum y carta de presentación</h2>
<ul class="linklist"><li><a href="https://fullcoll.joinhandshake.com/login"><span lang="en">Handshake Resume Optimizer</span></a> <span>Comentarios inmediatos sobre tu currículum; la principal recomendación del Centro de Carreras</span></li>
<li><a href="https://careercenter.fullcoll.edu/resume/">Guía de currículum y carta de presentación</a> <span>Plantillas, consejos y el seminario web <span lang="en">Resume and Cover Letter 101</span> (en inglés)</span></li>
<li><a href="https://forms.office.com/r/T1XCq0cEpB">Formulario de admisión del Centro de Carreras</a> <span>Pide ayuda individual con tu currículum o tu búsqueda de empleo (en inglés)</span></li></ul></div>
<div class="block" id="research"><h2>Investiga carreras</h2>
<p>Antes de elegir un programa, investiga las carreras a las que lleva: qué hacen las personas cada día, cuánto ganan y si los empleos están creciendo. Estas herramientas gratuitas son un buen punto de partida.</p>
<ul class="linklist">{{CAREER_SOURCES}}</ul></div>
<div class="block" id="explore"><h2>¿No sabes qué carrera te conviene?</h2>
<p>El Centro de Carreras puede ayudarte a elegir una carrera y un camino profesional. Estos recursos están en inglés.</p>
<ul class="linklist"><li><a href="https://careercenter.fullcoll.edu/exploration-experience/"><span lang="en">Career Exploration Experience</span></a> <span>Seis pasos con un consejero de carreras que terminan en tu plan educativo</span></li>
<li><a href="https://careercenter.fullcoll.edu/superstrong-journey/"><span lang="en">SuperStrong Journey</span></a> <span>Una evaluación de intereses y un plan para estudiantes de primer año</span></li>
<li><a href="https://nocccd.lightcastcc.com/?radius=&amp;region=Orange%20County"><span lang="en">Career Coach</span></a> <span>Empleos y salarios del condado de Orange, y los programas que llevan a ellos</span></li>
<li><a href="https://fullcoll.candidcareer.com/"><span lang="en">Candid Career</span></a> <span>Videos cortos de personas que describen su trabajo</span></li>
<li><a href="https://whatcanidowiththismajor.com/"><span lang="en">What Can I Do With This Major?</span></a> <span>Caminos profesionales por carrera</span></li>
<li><a href="https://careercenter.fullcoll.edu/courses/">Cursos de orientación profesional</a> <span>Obtén unidades mientras planeas tu carrera</span></li></ul></div>
<div class="block" id="closet"><h2 lang="en">Career Closet</h2>
<p>Elige ropa y accesorios profesionales gratis para entrevistas, ferias de empleo y el trabajo. Los estudiantes inscritos en al menos media unidad reciben puntos cada semestre para canjear por artículos que se quedan. Visita el edificio 2000, salón 2026, de lunes a jueves.</p>
<p><a href="https://careercenter.fullcoll.edu/career-closet/">Horario y detalles del <span lang="en">Career Closet</span> (en inglés) &rarr;</a></p></div>""",
  aside="""<div class="aside-card highlight"><h2>Centro de Carreras</h2>
<p class="small" style="margin:0 0 8px">Edificio 2000, salón 2027<br>714-992-7121<br>Lun–jue 9 a.m.–6 p.m., vie 9 a.m.–1 p.m.</p><ul>
<li><a href="https://fullcoll.joinhandshake.com/login">Entrar a <span lang="en">Handshake</span></a></li>
<li><a href="https://careercenter.fullcoll.edu/">Sitio web del Centro de Carreras</a></li>
<li><a href="https://careercenter.fullcoll.edu/calendar/">Talleres y seminarios web</a></li>
<li><a href="https://fullcoll.instructure.com/enroll/WHKEJW">Centro de Carreras en Canvas</a></li>
<li><a href="https://forms.office.com/r/T1XCq0cEpB">Pide ayuda (formulario de admisión)</a></li></ul></div>
<div class="aside-card"><h2>Gana experiencia</h2><ul><li><a href="internships.html">Prácticas profesionales con créditos</a></li></ul></div>"""),

 "clubs.html": dict(title="Clubes estudiantiles", eyebrow="Más allá del salón",
  lead="Conoce a estudiantes de tu área, escucha a empleadores y fortalece tu currículum en los clubes y la sociedad de honor de la división.",
  body="""<div class="block"><h2 lang="en">Hornet Business Club</h2>
<p>El club de la división para todos los estudiantes de Negocios y CIS. Únete al espacio del club en Canvas para recibir noticias, eventos y oportunidades.</p>
<p><a class="btn btn-primary" href="{{CLUB}}">Únete al <span lang="en">Hornet Business Club</span></a></p></div>
<div class="block"><h2>Sociedad de Contabilidad <span lang="en">(Accounting Society)</span></h2>
<p>El centro de contactos de negocios de Fullerton College, para estudiantes que planean transferirse a una UC, una CSU u otra universidad. Los miembros hacen contactos con actividades de trabajo en equipo, escuchan a conferencistas que cuentan cómo consiguieron empleo en firmas contables, empresas o el gobierno, y sirven a la comunidad, desde empacar alimentos para familias necesitadas hasta escribir cartas a personas mayores en asilos.</p>
<p>Para unirte, escribe a fullcollacctsociety@gmail.com y la mesa directiva del club te agregará a la lista de correo.</p></div>
<div class="block"><h2 lang="en">Lambda Epsilon Chi</h2>
<p>Lambda Epsilon Chi (LEX) es la sociedad nacional de honor en estudios paralegales de la <span lang="en">American Association for Paralegal Education</span>. Los integrantes reciben un certificado, un pin y una estola para usar en la graduación. La sociedad de honor también ofrece una beca cada semestre.</p>
<p>Pueden ser elegibles los estudiantes de Estudios Paralegales que hayan completado al menos 18 unidades de cursos PLEG con un promedio acumulado de 3.5 o más. Escribe a FCParalegalStudies@fullcoll.edu para saber cómo y cuándo solicitar.</p></div>""",
  aside="""<div class="aside-card highlight"><h2>Únete</h2><ul>
<li><a href="{{CLUB}}"><span lang="en">Hornet Business Club</span> (Canvas)</a></li>
<li>Sociedad de Contabilidad: fullcollacctsociety@gmail.com</li>
<li>LEX: FCParalegalStudies@fullcoll.edu</li></ul></div>"""),

 "contact.html": dict(title="Contacto y horario", eyebrow="Oficina de la división",
  lead="Visita, llama o escribe a la oficina de la División de Negocios y CIS. Te ayudaremos a encontrar a la persona indicada.",
  body="""<div class="block"><h2>Oficina de la división</h2>
<div class="tablebox"><table><tbody>
<tr><th scope="row">Ubicación</th><td>Edificio 300, suite 314<br>321 E. Chapman Ave., Fullerton, CA 92832</td></tr>
<tr><th scope="row">Sala de conferencias</th><td>Edificio 300, salón 325</td></tr>
<tr><th scope="row">Teléfono</th><td>714-992-7032</td></tr>
<tr><th scope="row">Correo electrónico</th><td>buscis@fullcoll.edu</td></tr></tbody></table></div></div>
<div class="block" id="hours"><h2>Horario de oficina</h2>
<div class="tablebox"><table><thead><tr><th>Periodo</th><th>Lunes a jueves</th><th>Viernes</th></tr></thead><tbody>
<tr><td>Otoño y primavera</td><td class="num">8 a.m. a 7 p.m.</td><td class="num">8 a.m. a 5 p.m.</td></tr>
<tr><td>Verano</td><td class="num">8 a.m. a 5 p.m.</td><td>Cerrado</td></tr></tbody></table></div>
<p class="small">Cerrado en los días feriados del campus. Consulta el <a href="https://www.nocccd.edu/events-calendars/academic-calendar">calendario académico</a>.</p></div>
<div class="block"><h2>Horario de atención del profesorado</h2>
<p>Cada profesor publica su horario de atención y su información de contacto en el programa del curso y en Canvas. Encuentra el correo de cualquier profesor en el <a href="faculty.html">directorio del profesorado</a>.</p></div>
<div class="block"><h2>Dirección y personal de la división</h2><ul class="people compact">{{STAFF}}</ul></div>""",
  aside="""<div class="aside-card highlight"><h2>Sigue a la división</h2><ul class="soc">{{SOCIAL_LIST}}</ul></div>
<div class="aside-card"><h2>Enlaces rápidos</h2><ul><li><a href="faculty.html">Directorio del profesorado</a></li><li><a href="counselors.html">Consejeros</a></li><li><a href="forms.html">Formularios y solicitudes</a></li></ul></div>"""),

 "accessibility.html": dict(title="Accesibilidad", eyebrow="Sobre este sitio",
  lead="La División de Negocios y CIS quiere que todos los estudiantes, familias y visitantes puedan usar este sitio web, incluidas las personas que usan tecnología de asistencia.",
  body="""<div class="block"><h2>Nuestro compromiso</h2>
<p>Este sitio está diseñado para cumplir las Pautas de Accesibilidad para el Contenido Web (WCAG) 2.1, nivel AA, el estándar que usan los colleges comunitarios de California para cumplir con la ADA y la Sección 508.</p></div>
<div class="block"><h2>Lo que hacemos</h2>
<ul>
<li>Todas las páginas funcionan solo con el teclado, y el primer elemento es un enlace para saltar al contenido.</li>
<li>El texto y los controles cumplen el contraste de color de WCAG en los temas claro y oscuro.</li>
<li>Las páginas usan encabezados, regiones y etiquetas claras para que los lectores de pantalla puedan recorrerlas.</li>
<li>Las páginas se adaptan a pantallas pequeñas y a un zoom de hasta 400 por ciento sin desplazamiento horizontal.</li>
<li>El contenido en movimiento se puede pausar, y la animación se detiene si tu dispositivo está configurado para reducir el movimiento.</li>
<li>Cada página está disponible en inglés y en español, y el idioma de la página está marcado para los lectores de pantalla.</li>
</ul></div>
<div class="block"><h2>Contenido al que enlazamos</h2>
<p>Algunas páginas enlazan a herramientas de otras oficinas, como el horario de clases, el catálogo, los formularios en línea y Canvas. Algunos documentos de los programas son archivos PDF. Si alguno te resulta difícil de usar, comunícate con nosotros y te daremos la información en otro formato.</p></div>
<div class="block"><h2>Reporta un problema</h2>
<p>Si algo en este sitio no funciona para ti, dinos en qué página y qué pasó. Responderemos en un plazo de cinco días hábiles.</p>
<ul><li>Correo electrónico: buscis@fullcoll.edu</li><li>Teléfono: 714-992-7032</li><li>Visítanos: Edificio 300, suite 314</li></ul></div>""",
  aside="""<div class="aside-card highlight"><h2>Servicios de Apoyo para Discapacidades</h2><p class="small" style="margin:0 0 8px">Para adaptaciones en clases y exámenes, comunícate con Servicios de Apoyo para Discapacidades (DSS) de Fullerton College.</p><ul><li><a href="https://dss.fullcoll.edu/">Disability Support Services (DSS)</a></li></ul></div>
<div class="aside-card"><h2>Opciones de visualización</h2><p class="small" style="margin:0">Usa los botones de tema en la parte superior de cualquier página para elegir claro, oscuro o la configuración de tu dispositivo. Tu elección se recuerda en este dispositivo.</p></div>"""),
}
