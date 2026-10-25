# Division people. On the live server this becomes inc/people.php.
# Photos: img/people/<slug>.jpg, 600x750 (4:5) headshot. No file -> initials tile.
# old_photo = headshot on the previous site (to download during migration); None = site showed the seal.
OLD = "https://buscis.fullcoll.edu/wp-content/uploads/"

STAFF = [  # (name, title, phone, email)
 ("Dr. Dani Wilson", "Acting Dean, Business &amp; CIS Division", "714-992-7032", "dwilson@fullcoll.edu"),
 ("Adriana Goncalves", "Administrative Assistant III", "714-732-5324", "agoncalves@fullcoll.edu"),
 ("Kelley Jones-Horwood", "Administrative Assistant II", "714-732-5568", "kjoneshorwood@fullcoll.edu"),
 ("Adrienne Williams", "Administrative Assistant I", "714-732-5323", "awilliams@fullcoll.edu"),
]

DEPTS = [("acct", "Accounting"), ("bus", "Business Management"), ("cis", "Computer Information Systems"), ("pleg", "Paralegal Studies")]

# (name, email, dept, role, area, old_photo)
FACULTY = [
 ("Brandon Tran","btran1@fullcoll.edu","acct","Department Coordinator","Financial, Managerial, Audit &amp; Assurance","2020/04/Brandon-Tran.jpg"),
 ("Xi Bai","xbai@fullcoll.edu","acct","","","2025/01/Xi-Bai-e1737142074959.jpg"),
 ("Chihwen Chen","cchen@fullcoll.edu","acct","","",None),
 ("Michael Guest","mguest@fullcoll.edu","acct","","","2024/12/M.-Guest-FC.jpg"),
 ("Randy Hoffman","rhoffman@fullcoll.edu","acct","","",None),
 ("Diana Hsueh","dhsueh@fullcoll.edu","acct","","",None),
 ("Peter Lim","plim@fullcoll.edu","acct","","",None),
 ("Ming-yin Scott","mscott1@fullcoll.edu","acct","","Financial, Managerial, and Intermediate Accounting","2020/04/Ming-Yin-Scott.jpg"),
 ("Charmaine Smith","csmith@fullcoll.edu","acct","","","2025/01/Charmaine-Smith-Headshot-High-Res_2458-scaled.jpg"),
 ("Paul St. John","pstjohn@fullcoll.edu","acct","","",None),
 ("Cindy Tran","ctran@fullcoll.edu","acct","","",None),
 ("Phat Truong","ptruong@fullcoll.edu","acct","","Financial, Managerial, Taxation, and Cost Accounting","2020/04/phat-truong-1.jpg"),

 ("Kathy Standen","kstanden@fullcoll.edu","bus","Department Coordinator","Marketing and Business Communications","2024/12/Kathy-Standen-jpeg-2.jpg"),
 ("Marcus Wilson","mwilson@fullcoll.edu","bus","Department Coordinator","Business Law, Business Economics, Introduction to Business","2020/04/Marcus-Wilson.jpg"),
 ("Gary Graves","ggraves@fullcoll.edu","bus","","Entrepreneurship and Artificial Intelligence","2026/06/Professor-Graves-blackbackground-lowres-1.png"),
 ("Richard Ghidella","rghidella@fullcoll.edu","bus","","Real Estate and Finance","2020/04/rich-ghidella.jpg"),
 ("Barry McCarthy","bmccarthy@fullcoll.edu","bus","","Management and International Business","2020/04/Barry-McCarthy.jpg"),
 ("Ali Asadi","aasadi@fullcoll.edu","bus","","Business Management and Real Estate","2023/02/ali-asadi.jpeg"),
 ("Alexandria (Brandi) Boyer","bboyer@fullcoll.edu","bus","","",None),
 ("Charles Byerly","cbyerly@fullcoll.edu","bus","","Business Management and Real Estate","2020/06/Charles-Byerly-e1593298939855.jpg"),
 ("Roberto Caudillo","rcaudillo@fullcoll.edu","bus","","",None),
 ("Erick Chan","echan@fullcoll.edu","bus","","",None),
 ("Kenneth Colby","kcolby@fullcoll.edu","bus","","",None),
 ("Maryanne Conlin","mconlin@fullcoll.edu","bus","","",None),
 ("Ross DiLeo","rdileo@fullcoll.edu","bus","","","2024/12/Ross-J-DiLeo-Pic.jpg"),
 ("Julianne Dixon","jdixon@fullcoll.edu","bus","","",None),
 ("Michael Dixon","mdixon@fullcoll.edu","bus","","","2024/12/Me.jpg"),
 ("James Downs","jdowns@fullcoll.edu","pleg","","",None),
 ("Brandon Duran","bduran@fullcoll.edu","bus","","","2026/05/Profile_Picture.png"),
 ("Timothy Durfield","tdurfield@fullcoll.edu","bus","","",None),
 ("Apollo Fraidany","afraidany@fullcoll.edu","bus","","Business Management and CIS","2022/11/Apollo.jpeg"),
 ("Eric Furlong","efurlong@fullcoll.edu","bus","","",None),
 ("Christopher Ghidella","cghidella@fullcoll.edu","bus","","",None),
 ("Devin Ghidella","dghidella@fullcoll.edu","bus","","","2023/03/ezgif.com-webp-to-jpg.jpg"),
 ("Michelle Gomez-Velazquez","mgomezvelazquez@fullcoll.edu","bus","","",None),
 ("Steve John Haddadin","shaddadin@fullcoll.edu","bus","","","2026/02/Haddadin-Steve.png"),
 ("Joseph Hines","jhines@fullcoll.edu","bus","","",None),
 ("Suzanne Jezek-Arriaga","sjezekarriaga@fullcoll.edu","bus","","",None),
 ("Kendrick Kim","kkim1@fullcoll.edu","bus","","","2020/06/Kendrick-Kim-e1593299888442.jpg"),
 ("Marwin Luminarias","mluminarias@fullcoll.edu","bus","","Marketing",None),
 ("Lambe Papoulias","lpapoulias@fullcoll.edu","bus","","","2024/12/Lambe-P-1-e1734133572797.png"),
 ("Justin Rife","jrife@fullcoll.edu","bus","","",None),
 ("Eric Rodriguez","erodriguez@fullcoll.edu","bus","","","2025/01/Eric-Rodgriguez.jpg"),
 ("K. Lee Steidel","ksteidel@fullcoll.edu","bus","","",None),
 ("Jane Troop","jtroop@fullcoll.edu","bus","","Business Management and Computer Applications",None),
 ("Rashawn Underdue","runderdue@fullcoll.edu","bus","","",None),
 ("Rajen Vurdien","rvurdien@fullcoll.edu","bus","","","2025/01/Rajen-Vurdien-scaled.jpg"),
 ("Wyeth Watnik","wwatnik@fullcoll.edu","bus","","","2020/06/Wyeth-Watnik-e1593301193438.jpg"),
 ("Kevin Webb","kwebb@fullcoll.edu","bus","","",None),
 ("Jacob Williams","jwilliams@fullcoll.edu","bus","","","2025/01/Jacob-Williams-Headshot.jpg"),
 ("Jayme Wilson","jwilson@fullcoll.edu","bus","","","2020/06/Jayme-Wilson-1-e1593301495190.jpg"),
 ("Kristine Wilson","kwilson@fullcoll.edu","bus","","",None),

 ("Brian Roach","broach@fullcoll.edu","cis","Department Coordinator","Networking and Cyber Security",None),
 ("Carlos Antunez","cantunez@fullcoll.edu","cis","","Computer Gaming","2025/01/Carlos-Atunez-scaled.jpeg"),
 ("Anna Carlin","acarlin@fullcoll.edu","cis","","Networking and Cyber Security","2020/04/Anna-Carlin.jpg"),
 ("Dale Craig","dcraig@fullcoll.edu","cis","","Networking and Game Design","2020/04/Dale-Craig.jpg"),
 ("Tyler Fitzpatrick","tfitzpatrick@fullcoll.edu","cis","","",None),
 ("Brenda Klingenmaier","bterry@fullcoll.edu","cis","","","2020/06/Brenda-Klingenmaier-e1593299299584.jpg"),
 ("Robert Konefsky","rkonefsky@fullcoll.edu","cis","","",None),
 ("Roger Long","rlong@fullcoll.edu","cis","","",None),
 ("Med Mogasemi","mmogasemi@fullcoll.edu","cis","","","2023/02/med-mogasemi.jpeg"),
 ("Kimberly Perez","kperez2@fullcoll.edu","cis","","","2023/02/kimberly-perez-scaled.jpeg"),
 ("Leonard Rosenblum","lrosenblum@fullcoll.edu","cis","","",None),
 ("Aeron Zentner","azentner@fullcoll.edu","cis","","",None),

 ("Michael Moore","mmoore1@fullcoll.edu","pleg","Program Director","Paralegal Studies","2020/12/MooreMichael-photo-e1608234518529.jpg"),
 ("Santalia Carter","scarter@fullcoll.edu","pleg","","","2022/11/Carter-Sandy-bio-pic-scaled.jpg"),
 ("Jacqueline James","jjames@fullcoll.edu","pleg","","","2022/11/Jackie.jpeg"),
 ("Douglas Lusk","dlusk@fullcoll.edu","pleg","","","2020/06/Douglas-Lusk-e1593297469137.jpg"),
 ("Owen Murphy","omurphy@fullcoll.edu","pleg","","","2023/02/owen-murphy.jpeg"),
 ("Lisa Mitts Patrick","lpatrick@fullcoll.edu","pleg","","","2025/01/Lisa-Mitts-Patrick.jpg"),
 ("Franco Torres","ftorres@fullcoll.edu","pleg","","",None),  # added from the division list, Oct 19, 2026
]

SOCIAL = [  # division accounts, from the division's social media flyer
 ("Facebook", "@fcbusinessdiv", "https://www.facebook.com/fcbusinessdiv/"),
 ("Instagram", "@fcbusiness_div", "https://www.instagram.com/fcbusiness_div/"),
 ("LinkedIn", "FC Alumni group", "https://www.linkedin.com/groups/1654377/"),
 ("YouTube", "@fullertoncollegebusiness", "https://www.youtube.com/@fullertoncollegebusiness"),
]
CLUB = "https://fullcoll.instructure.com/enroll/876ALN"

# "Find classes" links: each person's name exactly as the class schedule lists it ("Last, First").

# "Find classes" buttons. Name exactly as the class schedule lists it ("Last, First"), and the term to open:
# "" = the newest term on schedule.nocccd.edu (Winter/Spring 2027 now); "202610" = Fall 2026 for faculty not yet
# scheduled in spring. Checked against the schedule's instructor lists on October 19, 2026. Faculty not
# listed here had no classes in Fall 2026 or Winter/Spring 2027, so their card shows no button.
# Re-check each term (or, on the PHP server, read schedule.nocccd.edu/data/<term>/instructors.json daily).
SCHEDULE_NAMES = {
 "btran1@fullcoll.edu": ("Tran, Brandon", ""),
 "xbai@fullcoll.edu": ("Bai, Xi", ""),
 "cchen@fullcoll.edu": ("Chen, Chihwen", "202610"),
 "mguest@fullcoll.edu": ("Guest, Michael", ""),
 "rhoffman@fullcoll.edu": ("Hoffman, Randy", ""),
 "dhsueh@fullcoll.edu": ("Hsueh, Diana", ""),
 "plim@fullcoll.edu": ("Lim, Peter", ""),
 "mscott1@fullcoll.edu": ("Scott, Ming-yin", ""),
 "csmith@fullcoll.edu": ("Smith, Charmaine", ""),
 "pstjohn@fullcoll.edu": ("St. John, Paul", ""),
 "ctran@fullcoll.edu": ("Tran, Cindy", ""),
 "ptruong@fullcoll.edu": ("Truong, Phat", ""),
 "kstanden@fullcoll.edu": ("Standen, Kathy", ""),
 "mwilson@fullcoll.edu": ("Wilson, Marcus", ""),
 "ggraves@fullcoll.edu": ("Graves, Gary", ""),
 "rghidella@fullcoll.edu": ("Ghidella, Richard", ""),
 "bmccarthy@fullcoll.edu": ("McCarthy, Barry", ""),
 "aasadi@fullcoll.edu": ("Asadi, Ali", ""),
 "cbyerly@fullcoll.edu": ("Byerly, Charles", ""),
 "rcaudillo@fullcoll.edu": ("Caudillo, Roberto", ""),
 "echan@fullcoll.edu": ("Chan, Erick", "202610"),
 "kcolby@fullcoll.edu": ("Colby, Kenneth", ""),
 "mconlin@fullcoll.edu": ("Conlin, Maryanne", ""),
 "rdileo@fullcoll.edu": ("Dileo, Ross", ""),
 "jdixon@fullcoll.edu": ("Dixon, Julianne", ""),
 "mdixon@fullcoll.edu": ("Dixon, Michael", ""),
 "jdowns@fullcoll.edu": ("Downs, James", ""),
 "bduran@fullcoll.edu": ("Duran, Brandon", ""),
 "tdurfield@fullcoll.edu": ("Durfield, Timothy", ""),
 "afraidany@fullcoll.edu": ("Fraidany, Apollo", ""),
 "efurlong@fullcoll.edu": ("Furlong, Eric", ""),
 "cghidella@fullcoll.edu": ("Ghidella, Christopher", ""),
 "dghidella@fullcoll.edu": ("Ghidella, Devin", ""),
 "bboyer@fullcoll.edu": ("Boyer, Alexandria", ""),
 "mgomezvelazquez@fullcoll.edu": ("Gomez-Velazquez, Michelle", ""),
 "shaddadin@fullcoll.edu": ("Haddadin, Steve John", ""),
 "jhines@fullcoll.edu": ("Hines, Joseph", ""),
 "sjezekarriaga@fullcoll.edu": ("Jezek-Arriaga, Suzanne", ""),
 "kkim1@fullcoll.edu": ("Kim, Kendrick", ""),
 "mluminarias@fullcoll.edu": ("Luminarias, Marwin", "202610"),
 "jrife@fullcoll.edu": ("Rife, Justin", ""),
 "erodriguez@fullcoll.edu": ("Rodriguez, Eric", ""),
 "ksteidel@fullcoll.edu": ("Steidel, Lee", ""),
 "jtroop@fullcoll.edu": ("Troop, Jane", ""),
 "runderdue@fullcoll.edu": ("Underdue, Rashawn", ""),
 "rvurdien@fullcoll.edu": ("Vurdien, Rajen", ""),
 "wwatnik@fullcoll.edu": ("Watnik, Wyeth", ""),
 "kwebb@fullcoll.edu": ("Webb, Kevin", ""),
 "jwilliams@fullcoll.edu": ("Williams, Jacob", ""),
 "jwilson@fullcoll.edu": ("Wilson, Jayme", ""),
 "kwilson@fullcoll.edu": ("Wilson, Kristine", ""),
 "broach@fullcoll.edu": ("Roach, Brian", ""),
 "cantunez@fullcoll.edu": ("Antunez, Carlos", ""),
 "acarlin@fullcoll.edu": ("Carlin, Anna", ""),
 "dcraig@fullcoll.edu": ("Craig, Dale", ""),
 "tfitzpatrick@fullcoll.edu": ("Fitzpatrick, Tyler", "202610"),
 "bterry@fullcoll.edu": ("Klingenmaier, Brenda", ""),
 "rkonefsky@fullcoll.edu": ("Konefsky, Robert", ""),
 "rlong@fullcoll.edu": ("Long, Roger", ""),
 "mmogasemi@fullcoll.edu": ("Mogasemi, Med", ""),
 "kperez2@fullcoll.edu": ("Perez, Kimberly", ""),
 "lrosenblum@fullcoll.edu": ("Rosenblum, Leonard", ""),
 "azentner@fullcoll.edu": ("Zentner, Aeron", ""),
 "mmoore1@fullcoll.edu": ("Moore, Michael", ""),
 "scarter@fullcoll.edu": ("Carter, Santalia", ""),
 "jjames@fullcoll.edu": ("James, Jacqueline", ""),
 "dlusk@fullcoll.edu": ("Lusk, Douglas", ""),
 "omurphy@fullcoll.edu": ("Murphy, Owen", ""),
 "lpatrick@fullcoll.edu": ("Patrick, Lisa", ""),
}

# LinkedIn profiles faculty asked to show on their card (by email). Use the public profile URL, no query string.
LINKEDIN = {
 "jdixon@fullcoll.edu": "https://www.linkedin.com/in/julie-dixon-16978835/",
 "ggraves@fullcoll.edu": "https://www.linkedin.com/in/garygraves/",
 "runderdue@fullcoll.edu": "https://www.linkedin.com/in/rashawnunderdue/",
 "sjezekarriaga@fullcoll.edu": "https://www.linkedin.com/in/suzanne-jezek-arriaga-b4304b21/",
 "jrife@fullcoll.edu": "https://www.linkedin.com/in/taxrife/",
 "azentner@fullcoll.edu": "https://www.linkedin.com/in/aeronzentner/",
 "kwebb@fullcoll.edu": "https://www.linkedin.com/in/kevin-webb-1275037/",
 "echan@fullcoll.edu": "https://www.linkedin.com/in/erick-chan/",
 "mconlin@fullcoll.edu": "https://www.linkedin.com/in/maryanneconlin/",
 "ksteidel@fullcoll.edu": "https://www.linkedin.com/in/leesteidel/",
}

# Faculty who asked not to show a photo. They appear in a simple list under their department
# ("More ... faculty") instead of a photo card. Add an email here to move someone to the list.
NO_PHOTO = {
 "jtroop@fullcoll.edu",
}
