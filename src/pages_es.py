# Spanish versions of the resource pages in pages.py, keyed by file name.
# Form and office names that only exist in English keep lang="en". Needs review by a fluent speaker.
from pages import DYN, UP, linklist

PAGES_ES = {
 "forms.html": dict(title="Formularios y solicitudes", eyebrow="Recursos estudiantiles",
  lead="Solicita un certificado, pide sustituir un requisito o impugna un prerrequisito. Un consejero puede ayudarte a elegir el formulario correcto.",
  body=f"""
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
<li><a href="https://counseling.fullcoll.edu/">Citas en el Centro de Consejería</a></li>
<li><a href="https://counseling.fullcoll.edu/hours-and-location/">Horario y ubicación del Centro de Consejería</a></li>
<li><a href="https://www.fullcoll.edu/hornet-pathways/">Mapas de programas de <span lang="en">Hornet Pathways</span></a></li></ul></div>"""),

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
  lead="Obtén unidades de Fullerton College mientras vives y aprendes en otro país, en cursos impartidos por profesores de FC.",
  body="""<div class="block"><h2>Próximamente: Florencia, Italia</h2>
<p>Fullerton College planea un semestre de estudios en <b>Florencia, Italia</b>, para el <b>otoño de 2028</b>, dirigido por el profesor Gary Graves con Silvie Grote de Cypress College. Aquí se publicarán los cursos, los costos y las fechas de solicitud.</p></div>
<div class="block"><h2>Quién puede solicitar</h2>
<p>Los programas anteriores requerían al menos 12 unidades de trabajo universitario, incluido English 100 (College Writing) o su equivalente con C o más, un promedio (GPA) de 2.5 o más y una edad mínima de 18 años. Consulta con la oficina de Estudios en el Extranjero los requisitos de cada programa.</p></div>
<div class="block"><h2>Planea con tiempo</h2>
<p>Reúnete con un consejero para incluir los cursos en el extranjero en tu plan educativo, y empieza pronto tu plan de financiamiento.</p></div>""",
  aside="""<div class="aside-card highlight"><h2>Oficina de Estudios en el Extranjero</h2><ul>
<li><a href="https://studyabroad.fullcoll.edu/">Estudios en el extranjero de Fullerton College</a></li>
<li><a href="https://www.instagram.com/fcstudyabroad/">@fcstudyabroad en Instagram</a></li>
<li>studyabroad@fullcoll.edu</li></ul></div>
<div class="aside-card"><h2>Planea tu semestre</h2><ul><li><a href="counselors.html">Reúnete con un consejero</a></li></ul></div>"""),

 "career.html": dict(title="Recursos profesionales", eyebrow="Más allá del salón",
  lead="Encuentra empleo, recibe comentarios sobre tu currículum y vístete para la entrevista, con herramientas gratuitas para estudiantes de Fullerton College.",
  body="""<div class="block" id="connect"><h2 lang="en">FC Career Connect</h2>
<p>Busca empleos en la bolsa de trabajo de NACE, sube tu currículum y tu carta de presentación, conéctate con empleadores y profesores, y consulta ejemplos de currículums y cartas.</p>
<ol class="numbered"><li>Inicia sesión en <a href="https://mg.nocccd.edu">myGateway</a>.</li><li>Abre la pestaña <span lang="en">Student</span>.</li><li>En <span lang="en">Student Links</span>, selecciona FCCareerConnect.</li><li>Completa tu perfil.</li></ol>
<p class="small">Preguntas: Jennifer Merchant, jmerchant@fullcoll.edu</p></div>
<div class="block" id="vmock"><h2>Revisión de currículum con VMock</h2>
<p>Recibe comentarios inmediatos y detallados sobre tu currículum con el servicio VMock del Centro de Carreras.</p>
<ol class="numbered"><li>Ve a <a href="https://www.vmock.com/nocccd">vmock.com/nocccd</a>.</li><li>Elige <span lang="en">Continue with University ID</span>.</li><li>Inicia sesión con tu usuario y contraseña de myGateway.</li></ol></div>
<div class="block"><h2 lang="en">Career Closet</h2>
<p>El <span lang="en">Career Closet</span>, con ropa profesional gratuita para entrevistas y el trabajo, ahora forma parte del Centro de Carreras de Fullerton College.</p></div>""",
  aside="""<div class="aside-card highlight"><h2>Centro de Carreras</h2><ul>
<li><a href="https://careercenter.fullcoll.edu/">Centro de Carreras de Fullerton College</a></li>
<li><a href="https://fullcoll-csm.symplicity.com/">Bolsa de trabajo de NACE</a></li>
<li><a href="https://www.vmock.com/nocccd">VMock</a></li></ul></div>
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
<tr><th scope="row">Ubicación</th><td>Edificio 300, salón 325<br>321 E. Chapman Ave., Fullerton, CA 92832</td></tr>
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
<ul><li>Correo electrónico: buscis@fullcoll.edu</li><li>Teléfono: 714-992-7032</li><li>Visítanos: Edificio 300, salón 325</li></ul></div>""",
  aside="""<div class="aside-card highlight"><h2>Servicios de Apoyo para Discapacidades</h2><p class="small" style="margin:0 0 8px">Para adaptaciones en clases y exámenes, comunícate con Servicios de Apoyo para Discapacidades (DSS) de Fullerton College.</p><ul><li><a href="https://dss.fullcoll.edu/">Disability Support Services (DSS)</a></li></ul></div>
<div class="aside-card"><h2>Opciones de visualización</h2><p class="small" style="margin:0">Usa los botones de tema en la parte superior de cualquier página para elegir claro, oscuro o la configuración de tu dispositivo. Tu elección se recuerda en este dispositivo.</p></div>"""),
}
