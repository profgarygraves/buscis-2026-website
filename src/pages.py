# Resource pages migrated from the previous buscis.fullcoll.edu site (Oct 2026).
# Each page: file, title, lead, body (HTML), aside (HTML), todo (shown as an "update needed" note in the prototype).
DYN = "https://dynamicforms.ngwebsolutions.com/casAuthentication.ashx?InstID=dae388ce-3f17-4cbd-a756-80e1bc01327c&amp;targetURL=https%3a%2f%2fdynamicforms.ngwebsolutions.com%2fSubmit%2fStart%2f"
ESARS = "https://esars.fullcoll.edu/esars/Career_Education_Counseling/eSARS.asp?WCI=Init&amp;WCE=Settings"
UP = "https://buscis.fullcoll.edu/wp-content/uploads/"  # TODO: copy files into /docs before launch

def linklist(items):
    return '<ul class="linklist">' + "".join(f'<li><a href="{u}">{t}</a>{(" <span>" + d + "</span>") if d else ""}</li>' for t, u, d in items) + "</ul>"

PAGES = [
 dict(file="forms.html", title="Forms &amp; Applications", eyebrow="Student resources",
  lead="Apply for a certificate, petition to substitute a requirement, or challenge a prerequisite. A counselor can help you choose the right form.",
  body=f"""
<div class="block"><h2>Certificates</h2>
<p>Business and CIS certificate applications are processed by the Evaluations Unit in Admissions &amp; Records. Apply only after all of your classes are complete and final grades are posted.</p>
{linklist([("BUS &amp; CIS Division Certificate Application", "https://dynamicforms.ngwebsolutions.com/Submit/Page?form=0dbbf09f-d7bb-4ff3-8ef5-71ccd1684947&amp;section=1147703&amp;page=734430&amp;token=Jqj9sXaialUHA2W2lXQ4K9AxYxFg-ciqpJBfSzPChjE", ""),
           ("Petition to Substitute Certificate Requirements, BUS &amp; CIS Division", DYN+"2bdcb592-f1de-45c1-aa14-4a0fc2fd5128", "")])}
<p class="small">Questions about a certificate you applied for: evaluations@fullcoll.edu</p></div>
<div class="block"><h2>Degrees and graduation</h2>
<p>Degree applications and graduation deadlines are handled by Admissions &amp; Records.</p>
{linklist([("Graduation information and deadlines", "https://admissions.fullcoll.edu/graduation/", "Admissions &amp; Records"),
           ("Petition to Substitute Degree and Graduation Requirements", DYN+"e5b6c9e9-ebe1-479d-8fad-5051dbf0942c", "Admissions &amp; Records")])}</div>
<div class="block"><h2>Other forms</h2>
{linklist([("Petition to Repeat a Course", DYN+"fed01d56-e084-4723-987e-a41811c1b9a3", "Admissions &amp; Records"),
           ("Prerequisite/Corequisite Challenge Form", DYN+"b3c28569-bd33-44b3-b8b3-2bb215721352", "Admissions &amp; Records")])}</div>""",
  aside="""<div class="aside-card"><h2>Get help with forms</h2><p class="small" style="margin:0 0 8px">Meeting with a counselor first is strongly recommended.</p><ul><li><a href="counselors.html">Career education counselors</a></li></ul></div>""",
  todo=""),

 dict(file="counselors.html", title="Counselors", eyebrow="Student resources",
  lead="Career education counselors help Business and CIS students build an education plan, choose a certificate or degree, and plan for transfer or work.",
  body="""<div class="block"><h2>Career education counselors</h2>
<ul class="people compact">{{COUNSELORS}}</ul>
<p><a class="btn btn-primary" href="{{ESARS}}">Book a counseling appointment</a></p></div>
<div class="block"><h2>Career education counseling hours</h2>
<div class="tablebox"><table><thead><tr><th>Day</th><th>Hours</th></tr></thead><tbody>
<tr><td>Monday</td><td class="num">1 to 5 p.m.</td></tr><tr><td>Tuesday</td><td class="num">8 a.m. to 6 p.m.</td></tr>
<tr><td>Wednesday</td><td class="num">1 to 5 p.m.</td></tr><tr><td>Thursday</td><td class="num">8 a.m. to 5 p.m.</td></tr>
<tr><td>Friday</td><td class="num">1 to 5 p.m.</td></tr></tbody></table></div>
<p class="small">Hours posted for Spring 2026 and subject to change.</p></div>""",
  aside="""<div class="aside-card"><h2>More counseling</h2><ul>
<li><a href="https://counseling.fullcoll.edu/">Counseling Center appointments</a></li>
<li><a href="https://counseling.fullcoll.edu/hours-and-location/">Counseling Center hours and location</a></li>
<li><a href="https://www.fullcoll.edu/hornet-pathways/">Hornet Pathways program maps</a></li></ul></div>""",
  todo="Confirm the current counselor list and Fall 2026 hours. An older page also listed Jennika Celo."),

 dict(file="internships.html", title="Internships", eyebrow="Beyond class",
  lead="Earn college credit while you work with a local employer in a job related to your program. Paid and unpaid positions both count.",
  body=f"""<div class="block"><h2>Internship courses</h2>
<div class="tablebox"><table><thead><tr><th>Course</th><th>Title</th><th>Units</th></tr></thead><tbody>
<tr><td><a href="https://schedule.nocccd.edu/?college=2&amp;keyword=BUS295"><b>BUS 295 F</b></a></td><td>Business Internship</td><td class="num">2 to 4</td></tr>
<tr><td><a href="https://schedule.nocccd.edu/?college=2&amp;keyword=CIS295"><b>CIS 295 F</b></a></td><td>Computer Information Systems Internship</td><td class="num">2 to 4</td></tr>
<tr><td><a href="https://schedule.nocccd.edu/?college=2&amp;keyword=PLEG210"><b>PLEG 210 F</b></a></td><td>Paralegal Internship</td><td class="num">2</td></tr>
</tbody></table></div></div>
<div class="block"><h2>Units and work hours</h2>
<div class="tablebox"><table><thead><tr><th>Units</th><th>Work hours required (plus the course)</th></tr></thead><tbody>
<tr><td class="num">2</td><td class="num">54 hours</td></tr><tr><td class="num">3</td><td class="num">108 hours</td></tr><tr><td class="num">4</td><td class="num">162 hours</td></tr></tbody></table></div>
<p class="small">Credit follows Title 5 of the California Code of Regulations. You may take more than one internship while enrolled.</p></div>
<div class="block"><h2>How to get started</h2>
<ol class="numbered"><li>Join the Business Division Internship Canvas space, or fill out the student interest form.</li>
<li>Enroll in BUS 295 F or CIS 295 F, depending on your certificate or degree.</li>
<li>You are assigned a faculty advisor who helps you complete the internship requirements.</li></ol>
<p>You must be a registered Fullerton College student in the Business Division who has completed coursework at the college.</p></div>""",
  aside=f"""<div class="aside-card highlight"><h2>Students</h2><ul>
<li><a href="https://fullcoll.instructure.com/enroll/FHDJDC">Join the Internship Canvas space</a></li>
<li><a href="https://forms.gle/ftybLC3G4PkHvWg26">Student interest form</a></li>
<li><a href="{UP}2020/05/001-BUS-CIS-Internship-student-brochure.pdf">Student brochure (PDF)</a></li></ul></div>
<div class="aside-card"><h2>Employers</h2><ul>
<li><a href="https://forms.gle/GSSc6mFLR5vVfEsy5">Employer interest form</a></li>
<li><a href="{UP}2020/05/005-BUS-CIS-Internship-Employers-brochure.pdf">Employer brochure (PDF)</a></li></ul></div>
<div class="aside-card"><h2>Contacts</h2><ul class="contacts">
<li><b>Business</b><span>Prof. Gary Graves, ggraves@fullcoll.edu</span></li>
<li><b>CIS and Cyber Security</b><span>Prof. Anna Carlin, acarlin@fullcoll.edu</span></li>
<li><b>Paralegal</b><span>Prof. Michael Moore, mmoore1@fullcoll.edu</span></li></ul></div>""",
  todo=""),

 dict(file="study-abroad.html", title="Study Abroad", eyebrow="Beyond class",
  lead="Earn Fullerton College units while you live and learn in another country, in courses taught by FC faculty.",
  body="""<div class="block"><h2>Coming up: Florence, Italy</h2>
<p>A Fullerton College study abroad semester in <b>Florence, Italy</b> is planned for <b>Fall 2028</b>, led by Professor Gary Graves with Silvie Grote of Cypress College. Courses, costs, and application dates will be posted here.</p></div>
<div class="block"><h2>Who can apply</h2>
<p>Past programs required at least 12 units of college work, including English 100 (College Writing) or the equivalent with a C or better, a GPA of 2.5 or higher, and a minimum age of 18. Check the Study Abroad office for the requirements of each program.</p></div>
<div class="block"><h2>Plan ahead</h2>
<p>Meet with a counselor to fit study abroad courses into your education plan, and start your funding plan early.</p></div>""",
  aside="""<div class="aside-card highlight"><h2>Study Abroad office</h2><ul>
<li><a href="https://studyabroad.fullcoll.edu/">Fullerton College Study Abroad</a></li>
<li><a href="https://www.instagram.com/fcstudyabroad/">@fcstudyabroad on Instagram</a></li>
<li>studyabroad@fullcoll.edu</li></ul></div>
<div class="aside-card"><h2>Plan your semester</h2><ul><li><a href="counselors.html">Meet with a counselor</a></li></ul></div>""",
  todo="The old page still describes Seville, Spring 2023. Please supply Florence 2028 details (courses, cost, dates, interest form)."),

 dict(file="career.html", title="Career Resources", eyebrow="Beyond class",
  lead="Find jobs, get feedback on your resume, and dress for the interview, with free tools for Fullerton College students.",
  body="""<div class="block" id="connect"><h2>FC Career Connect</h2>
<p>Search jobs on the NACE job board, upload your resume and cover letter, connect with employers and faculty, and browse sample resumes and cover letters.</p>
<ol class="numbered"><li>Log in to <a href="https://mg.nocccd.edu">myGateway</a>.</li><li>Open the Student tab.</li><li>Under Student Links, select FCCareerConnect.</li><li>Complete your profile.</li></ol>
<p class="small">Questions: Jennifer Merchant, jmerchant@fullcoll.edu</p></div>
<div class="block" id="vmock"><h2>VMock resume review</h2>
<p>Get instant, detailed feedback on your resume through the Career Center's VMock service.</p>
<ol class="numbered"><li>Go to <a href="https://www.vmock.com/nocccd">vmock.com/nocccd</a>.</li><li>Choose Continue with University ID.</li><li>Sign in with your myGateway ID and password.</li></ol></div>
<div class="block"><h2>Career Closet</h2>
<p>The Career Closet, with free professional clothing for interviews and work, is now part of the Fullerton College Career Center.</p></div>""",
  aside="""<div class="aside-card highlight"><h2>Career Center</h2><ul>
<li><a href="https://careercenter.fullcoll.edu/">Fullerton College Career Center</a></li>
<li><a href="https://fullcoll-csm.symplicity.com/">NACE job board</a></li>
<li><a href="https://www.vmock.com/nocccd">VMock</a></li></ul></div>
<div class="aside-card"><h2>Get experience</h2><ul><li><a href="internships.html">Internships for credit</a></li></ul></div>""",
  todo=""),

 dict(file="clubs.html", title="Student Clubs", eyebrow="Beyond class",
  lead="Meet students in your field, hear from employers, and build your resume through the division's clubs and honor society.",
  body="""<div class="block"><h2>Hornet Business Club</h2>
<p>The division's club for all Business and CIS students. Join the club's Canvas space to get news, events, and opportunities.</p>
<p><a class="btn btn-primary" href="{{CLUB}}">Join the Hornet Business Club</a></p></div>
<div class="block"><h2>Accounting Society</h2>
<p>The business networking center of Fullerton College, for students planning to transfer to a UC, CSU, or other university. Members network through team-building activities, hear guest speakers describe how they landed jobs at accounting firms and corporate or government employers, and serve the community, from packing food for neighbors in need to writing letters to seniors in nursing homes.</p>
<p>To join, email fullcollacctsociety@gmail.com and the club board will add you to the mailing list.</p></div>
<div class="block"><h2>Lambda Epsilon Chi (Paralegal Honor Society)</h2>
<p>Lambda Epsilon Chi (LEX) is the national honor society in paralegal studies of the American Association for Paralegal Education. Inductees receive a certificate, a lapel pin, and a stole to wear at graduation. The honor society also offers a scholarship each semester.</p>
<p>Paralegal Studies students who have completed at least 18 units of PLEG courses with a cumulative GPA of 3.5 or higher may be eligible. Email FCParalegalStudies@fullcoll.edu to learn how and when to apply.</p></div>""",
  aside="""<div class="aside-card highlight"><h2>Join</h2><ul>
<li><a href="{{CLUB}}">Hornet Business Club (Canvas)</a></li>
<li>Accounting Society: fullcollacctsociety@gmail.com</li>
<li>LEX: FCParalegalStudies@fullcoll.edu</li></ul></div>""",
  todo="Add faculty advisors and meeting times for each club."),

 dict(file="contact.html", title="Contact &amp; Hours", eyebrow="Division office",
  lead="Stop by, call, or email the Business &amp; CIS Division office. We will point you to the right person.",
  body="""<div class="block"><h2>Division office</h2>
<div class="tablebox"><table><tbody>
<tr><th scope="row">Location</th><td>Building 300, Room 325<br>321 E. Chapman Ave., Fullerton, CA 92832</td></tr>
<tr><th scope="row">Phone</th><td>714-992-7032</td></tr>
<tr><th scope="row">Email</th><td>buscis@fullcoll.edu</td></tr></tbody></table></div></div>
<div class="block" id="hours"><h2>Office hours</h2>
<div class="tablebox"><table><thead><tr><th>Term</th><th>Monday to Thursday</th><th>Friday</th></tr></thead><tbody>
<tr><td>Fall and spring</td><td class="num">8 a.m. to 7 p.m.</td><td class="num">8 a.m. to 5 p.m.</td></tr>
<tr><td>Summer</td><td class="num">8 a.m. to 5 p.m.</td><td>Closed</td></tr></tbody></table></div>
<p class="small">Closed on campus holidays. See the <a href="https://www.nocccd.edu/events-calendars/academic-calendar">academic calendar</a>.</p></div>
<div class="block"><h2>Faculty office hours</h2>
<p>Each instructor posts office hours and contact information in the syllabus and Canvas course. Find any instructor's email in the <a href="faculty.html">faculty directory</a>.</p></div>
<div class="block"><h2>Division leadership and staff</h2><ul class="people compact">{{STAFF}}</ul></div>""",
  aside="""<div class="aside-card highlight"><h2>Follow the division</h2><ul class="soc">{{SOCIAL_LIST}}</ul></div>
<div class="aside-card"><h2>Quick links</h2><ul><li><a href="faculty.html">Faculty directory</a></li><li><a href="counselors.html">Counselors</a></li><li><a href="forms.html">Forms &amp; applications</a></li></ul></div>""",
  todo="The old Contact page lists Building 300, Suite 314. I used Room 325 as you told me; please confirm."),
]

COUNSELORS = [  # (name, title, email)
 ("Olivia Barajas, M.S.", "Career Education Counselor", "obarajas@fullcoll.edu"),
 ("Lovrina Castillo", "Career Education Counselor", "lcastillo2@fullcoll.edu"),
 ("Field Nguyen, M.S.", "Career Education Counselor", "fdo@fullcoll.edu"),
 ("Pamela Skiles, M.S.", "Career Education Counselor", "pskiles1@fullcoll.edu"),
]
