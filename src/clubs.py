# Division-supported student clubs and honor societies, shown on clubs.html.
# Each club: id (page anchor), name, logo (img/clubs/..., optional), tag (en, es), about (en, es),
# advisor, meets (en, es), join (label en, label es, url or "mailto:"), social [(network, handle, url)].
# Add a club by copying a block. Leave a field empty ("" or None) to hide it.
CLUB_CANVAS = "https://fullcoll.instructure.com/enroll/876ALN"

CLUBS = [
 dict(id="hornet-business-club", name="Hornet Business Club", logo=None,
      tag=("For every Business and Accounting student", "Para todos los estudiantes de Negocios y Contabilidad"),
      about=("The division's club for all Business and Accounting majors, now including the former Accounting Society. Join the club's Canvas space for news, events, speakers, and opportunities across the division.",
             "El club de la división para todos los estudiantes de Negocios y Contabilidad, que ahora incluye a la antigua Sociedad de Contabilidad (Accounting Society). Únete a su espacio en Canvas para recibir noticias, eventos, conferencistas y oportunidades."),
      advisor="", meets=("", ""),
      join=("Join in Canvas", "Únete en Canvas", CLUB_CANVAS), social=[]),
 dict(id="esports", name="Esports Club", logo="img/clubs/esports.jpg", logo_alt="Fullerton College Phantoms esports logo",
      tag=("Fullerton College Phantoms", "Fullerton College Phantoms"),
      about=("Play, compete, and connect with other gamers at every skill level. Represent Fullerton College as the FC Phantoms, and pair the club with the Computer Gaming program's eSports courses (CISG 191, 192, and 193).",
             "Juega, compite y conecta con otros gamers de cualquier nivel. Representa a Fullerton College como los FC Phantoms y combina el club con los cursos de eSports del programa de Videojuegos (CISG 191, 192 y 193)."),
      advisor="Carlos Antunez",
      meets=("Every other Wednesday, 3:30 to 7:30 p.m., starting the third week of the semester",
             "Cada dos miércoles, de 3:30 a 7:30 p.m., a partir de la tercera semana del semestre"),
      join=("Sign up for the club", "Inscríbete en el club", "https://docs.google.com/forms/d/1ggsNake6Rxvwjc6Mc_24uHG06FBzrOMunbo0JzyGkT0/viewform"),
      social=[("Instagram", "@fcesports_club", "https://www.instagram.com/fcesports_club/"),
              ("TikTok", "@fcesports.club", "https://www.tiktok.com/@fcesports.club"),
              ("YouTube", "@fcesports_club", "https://www.youtube.com/@fcesports_club"),
              ("Twitch", "fcesports_club", "https://www.twitch.tv/fcesports_club")]),
 dict(id="lex", name="Lambda Epsilon Chi (LEX)", logo=None, initials="LEX",
      tag=("Paralegal Studies honor society", "Sociedad de honor de Estudios Paralegales"),
      about=("The national honor society in paralegal studies of the American Association for Paralegal Education. Inductees receive a certificate, a lapel pin, and a stole to wear at graduation, and LEX offers a scholarship each semester. Paralegal Studies students with at least 18 units of PLEG courses and a cumulative GPA of 3.5 or higher may be eligible.",
             "La sociedad nacional de honor en estudios paralegales de la American Association for Paralegal Education. Los integrantes reciben un certificado, un pin y una estola para la graduación, y LEX ofrece una beca cada semestre. Pueden ser elegibles los estudiantes de Estudios Paralegales con al menos 18 unidades de cursos PLEG y un promedio acumulado de 3.5 o más."),
      advisor="", meets=("", ""),
      join=("Email to ask how to apply", "Escribe para saber cómo solicitar", "mailto:FCParalegalStudies@fullcoll.edu"), social=[]),
]
