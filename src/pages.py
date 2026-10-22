# Resource pages migrated from the previous buscis.fullcoll.edu site (Oct 2026).
# Each page: file, title, lead, body (HTML), aside (HTML), todo (shown as an "update needed" note in the prototype).
DYN = "https://dynamicforms.ngwebsolutions.com/casAuthentication.ashx?InstID=dae388ce-3f17-4cbd-a756-80e1bc01327c&amp;targetURL=https%3a%2f%2fdynamicforms.ngwebsolutions.com%2fSubmit%2fStart%2f"
ESARS = "https://esars.fullcoll.edu/esars/Career_Education_Counseling/eSARS.asp?WCI=Init&amp;WCE=Settings"
UP = "https://buscis.fullcoll.edu/wp-content/uploads/"  # TODO: copy files into /docs before launch

def linklist(items):
    return '<ul class="linklist">' + "".join(f'<li><a href="{u}">{t}</a>{(" <span>" + d + "</span>") if d else ""}</li>' for t, u, d in items) + "</ul>"

PAGES = [
 dict(file="rotation.html", title="Course Rotation", eyebrow="Student resources",
  lead="See which semesters each course is usually offered, so you can plan ahead. Some courses run only once a year, or every other year.",
  body="""<p class="notice" role="note">Rotations are planned and can change. Always confirm in the <a href="https://schedule.nocccd.edu/?college=2">class schedule</a> before you register, and plan your semesters with a <a href="counselors.html">counselor</a> or in <a href="https://admissions.fullcoll.edu/degreeworks-faq/">DegreeWorks</a>.</p>
<nav class="jump" aria-label="Jump to"><ul><li><a href="#business">Business</a></li><li><a href="#intl">International Business</a></li><li><a href="#marketing">Marketing</a></li><li><a href="#realestate">Real Estate</a></li><li><a href="#accounting">Accounting</a></li><li><a href="#cis">CIS</a></li><li><a href="#gaming">Computer Gaming</a></li><li><a href="#cyber">Cyber Security</a></li><li><a href="#paralegal">Paralegal Studies</a></li></ul></nav>
{{ROTATION}}""",
  aside="",
  todo=""),

 dict(file="forms.html", title="Forms &amp; Applications", eyebrow="Student resources",
  lead="Change your major, apply for a certificate, petition to substitute a requirement, or challenge a prerequisite. A counselor can help you choose the right form.",
  body=f"""
<div class="block"><h2>Change your major</h2>
<p>Want to major in a Business or CIS program? Update your major with Admissions &amp; Records so your counselor, education plan, and Hornet Pathway match your goal. Pick the exact degree or certificate you plan to earn; the program pages on this site link to each one in the catalog.</p>
{linklist([("Change My Major", "https://admissions.fullcoll.edu/major-changes/", "Admissions &amp; Records")])}</div>
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
<div class="block"><h2>Counseling Center hours</h2>
<div class="tablebox"><table><thead><tr><th>Day</th><th>Hours</th></tr></thead><tbody>
<tr><td>Monday</td><td class="num">8 a.m. to 5 p.m.</td></tr><tr><td>Tuesday</td><td class="num">8 a.m. to 6 p.m.</td></tr>
<tr><td>Wednesday</td><td class="num">8 a.m. to 6 p.m.</td></tr><tr><td>Thursday</td><td class="num">8 a.m. to 5 p.m.</td></tr>
<tr><td>Friday</td><td class="num">8 a.m. to noon</td></tr>
<tr><td>Select Saturdays</td><td class="num">9 a.m. to 1 p.m., remote only</td></tr></tbody></table></div>
<p class="small">Hours are subject to change. Drop-in (general information) sign-ups close at least 30 minutes before the end of the day. See <a href="https://counseling.fullcoll.edu/hours-and-location/">Counseling Center hours and location</a> for Saturday dates.</p></div>""",
  aside="""<div class="aside-card"><h2>More counseling</h2><ul>
<li><a href="https://counseling.fullcoll.edu/appointments/">Counseling Center appointments</a></li>
<li><a href="https://counseling.fullcoll.edu/hours-and-location/">Counseling Center hours and location</a></li>
<li><a href="https://www.fullcoll.edu/hornet-pathways/">Hornet Pathways program maps</a></li>
<li><a href="https://admissions.fullcoll.edu/degreeworks-faq/">Learn about DegreeWorks</a></li></ul></div>""",
  todo=""),

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
  lead="Earn Fullerton College units while you live and learn in Florence, Italy, in Fall 2028.",
  body=f"""<div class="block"><a href="https://studyabroad.fullcoll.edu/"><img class="flyer" src="img/florence-2028.jpg" width="1400" height="933" alt="Study Art History, Business, and Wellness in Florence, Italy, Fall 2028. Visit studyabroad.fullcoll.edu."></a></div>
<div class="block"><h2>Florence, Italy: Fall 2028</h2>
<p>Spend a 13-week semester in <b>Florence, Italy</b>, studying art history, business, and wellness. The program is led by Professor Gary Graves of Fullerton College with Professor Silvie Grote of Cypress College. You earn Fullerton College units that count toward general education, your major, and transfer.</p>
<p class="notice" role="note"><b>Please note:</b> This program is pending Board of Trustees approval. Courses have not been finalized and are subject to change.</p>
<p><a class="btn btn-primary" href="https://studyabroad.fullcoll.edu/">Apply or ask questions at studyabroad.fullcoll.edu</a></p></div>
<div class="block"><h2>Planned courses</h2>
<h3>Art history and business, with Professor Gary Graves</h3>
<div class="tablebox"><table><thead><tr><th scope="col">Course</th><th scope="col">Title</th><th scope="col">Units</th><th scope="col">FC GE area</th><th scope="col">Transfers to</th></tr></thead><tbody><tr><th scope="row"><a href="https://catalog.nocccd.edu/search/?caturl=%2Ffullerton-college&amp;search=BUS+240+F">BUS 240 F</a></th><td><span lang="en">Legal Environment of Business</span><br><span class="small">Honors available</span></td><td>3</td><td>4</td><td>CSU</td></tr><tr><th scope="row"><a href="https://catalog.nocccd.edu/search/?caturl=%2Ffullerton-college&amp;search=ARTH+155+F">ARTH 155 F</a></th><td><span lang="en">Western Art History: 15th to 21st Century</span><br><span class="small">Honors available</span></td><td>3</td><td>3</td><td>CSU</td></tr><tr><th scope="row"><a href="https://catalog.nocccd.edu/search/?caturl=%2Ffullerton-college&amp;search=BUS+211+F">BUS 211 F</a></th><td><span lang="en">Personal Critical Reasoning and Writing for Business Management</span><br><span class="small">Honors available</span></td><td>3</td><td>1B</td><td>CSU</td></tr><tr><th scope="row"><a href="https://catalog.nocccd.edu/search/?caturl=%2Ffullerton-college&amp;search=ARTH+100+F">ARTH 100 F</a></th><td><span lang="en">Introduction to Visual Culture</span><br><span class="small">Honors available</span></td><td>3</td><td>3</td><td>CSU</td></tr><tr><th scope="row"><a href="https://catalog.nocccd.edu/search/?caturl=%2Ffullerton-college&amp;search=BUS+185+F">BUS 185 F</a></th><td><span lang="en">Creativity Matters!</span></td><td>3</td><td>7</td><td>CSU</td></tr></tbody></table></div>
<h3>Health and wellness, with Professor Silvie Grote</h3>
<div class="tablebox"><table><thead><tr><th scope="col">Course</th><th scope="col">Title</th><th scope="col">Units</th><th scope="col">FC GE area</th><th scope="col">Transfers to</th></tr></thead><tbody><tr><th scope="row"><a href="https://catalog.nocccd.edu/search/?caturl=%2Ffullerton-college&amp;search=PE+235+F">PE 235 F</a></th><td><span lang="en">First Aid, CPR, and Safety Education</span></td><td>3</td><td>—</td><td>CSU, UC</td></tr><tr><th scope="row"><a href="https://catalog.nocccd.edu/search/?caturl=%2Ffullerton-college&amp;search=HED+140+F">HED 140 F</a></th><td><span lang="en">Health Science</span></td><td>3</td><td>5</td><td>CSU, UC</td></tr><tr><th scope="row"><a href="https://catalog.nocccd.edu/search/?caturl=%2Ffullerton-college&amp;search=PE+121+F">PE 121 F</a></th><td><span lang="en">Walking for Fitness</span></td><td>1</td><td>7</td><td>CSU; UC limits credit</td></tr><tr><th scope="row"><a href="https://catalog.nocccd.edu/search/?caturl=%2Ffullerton-college&amp;search=PE+243+F">PE 243 F</a></th><td><span lang="en">Stress Management</span></td><td>3</td><td>7</td><td>CSU; UC limits credit</td></tr></tbody></table></div>
<p class="small">GE areas are for the Fullerton College AA/AS degree. ARTH 100 F and ARTH 155 F also meet Cal-GETC Area 3. Ask a counselor how each course fits your education plan.</p></div>
<div class="block"><h2>Paying for study abroad</h2>
<p>Not sure how to pay for it? Take <a href="https://catalog.nocccd.edu/search/?caturl=%2Ffullerton-college&amp;search=BUS+186+F">BUS 186 F, Funding Special Projects and New Ventures</a>. You will learn to find grants and scholarships for study abroad, run a crowdfunding campaign, pitch your project, and build a budget. Financial aid may also apply to approved programs; ask the Financial Aid office.</p>
{linklist([("IEFA: International Education Financial Aid", "https://iefa.org/", "Scholarship search"),
           ("U.S. Department of State: Study Abroad", "https://studyabroad.state.gov/", "Planning and safety"),
           ("Fullerton College Financial Aid", "https://financialaid.fullcoll.edu/", "")])}</div>
<div class="block"><h2>Who can apply</h2>
<p>Past programs required at least 12 units of college work, including English 100 (College Writing) or the equivalent with a C or better, a GPA of 2.5 or higher, and a minimum age of 18. Check <a href="https://studyabroad.fullcoll.edu/">studyabroad.fullcoll.edu</a> for the requirements of this program.</p></div>""",
  aside="""<div class="aside-card highlight"><h2>Study Abroad office</h2><ul>
<li><a href="https://studyabroad.fullcoll.edu/">studyabroad.fullcoll.edu</a></li>
<li><a href="https://www.instagram.com/fcstudyabroad/">@fcstudyabroad on Instagram</a></li>
<li>studyabroad@fullcoll.edu</li></ul></div>
<div class="aside-card"><h2>More about the program</h2><ul>
<li><a href="https://ggraves.faculty.fullcoll.edu/study-abroad.html">Florence 2028 on Professor Graves's site</a></li>
<li><a href="https://catalog.nocccd.edu/search/?caturl=%2Ffullerton-college&amp;search=BUS+186+F">BUS 186 F: funding your trip</a></li>
<li><a href="counselors.html">Meet with a counselor</a></li></ul></div>""",
  todo=""),

 dict(file="career.html", title="Career Resources", eyebrow="Beyond class",
  lead="Find jobs and internships on Handshake, get feedback on your resume, research careers, and dress for the interview, with free help from the Fullerton College Career Center.",
  body="""<div class="block" id="jobs"><h2>Find jobs on Handshake</h2>
<p>Handshake is Fullerton College's job and internship platform. Search on- and off-campus jobs and internships, connect with employers, and sign up for career fairs and events.</p>
<ol class="numbered"><li>Go to <a href="https://fullcoll.joinhandshake.com/login">fullcoll.joinhandshake.com</a>.</li><li>Choose <b>Login using your Student ID</b>.</li><li>Sign in with your Fullerton College student login, the same username and password you use for myGateway.</li><li>Complete your profile and upload your resume so employers can find you.</li></ol>
<p><a class="btn btn-primary" href="https://fullcoll.joinhandshake.com/login">Log in to Handshake</a></p>
<p class="small">New to Handshake? The Career Center runs a free Handshake 101 Job Search webinar. See the <a href="https://careercenter.fullcoll.edu/calendar/">Career Center calendar</a> for dates.</p></div>
<div class="block" id="resume"><h2>Resume and cover letter help</h2>
<ul class="linklist"><li><a href="https://fullcoll.joinhandshake.com/login">Handshake Resume Optimizer</a> <span>Instant feedback on your resume; the Career Center's top recommendation</span></li>
<li><a href="https://careercenter.fullcoll.edu/resume/">Resume &amp; Cover Letter guide</a> <span>Templates, tips, and the Resume and Cover Letter 101 webinar</span></li>
<li><a href="https://forms.office.com/r/T1XCq0cEpB">Career Center intake form</a> <span>Ask for one-on-one help with your resume or job search</span></li></ul></div>
<div class="block" id="research"><h2>Research careers</h2>
<p>Before you choose a program, look up the careers it leads to: what people do all day, what they earn, and whether jobs are growing. These free tools are a good place to start.</p>
<ul class="linklist">{{CAREER_SOURCES}}</ul></div>
<div class="block" id="explore"><h2>Not sure what career fits?</h2>
<p>The Career Center can help you choose a major and a career path.</p>
<ul class="linklist"><li><a href="https://careercenter.fullcoll.edu/exploration-experience/">Career Exploration Experience</a> <span>Six steps with a career counselor, ending in your education plan</span></li>
<li><a href="https://careercenter.fullcoll.edu/superstrong-journey/">SuperStrong Journey</a> <span>An interest assessment and plan for first-year students</span></li>
<li><a href="https://nocccd.lightcastcc.com/?radius=&amp;region=Orange%20County">Career Coach</a> <span>Orange County jobs, pay, and the programs that lead to them</span></li>
<li><a href="https://fullcoll.candidcareer.com/">Candid Career</a> <span>Short videos of people describing their jobs</span></li>
<li><a href="https://whatcanidowiththismajor.com/">What Can I Do With This Major?</a> <span>Career paths by major</span></li>
<li><a href="https://careercenter.fullcoll.edu/courses/">Career counseling courses</a> <span>Earn units while you plan your career</span></li></ul></div>
<div class="block" id="closet"><h2>Career Closet</h2>
<p>Pick out free professional clothing and accessories for interviews, career fairs, and work. Students enrolled in at least half a unit get points each semester to spend on items they keep. Visit Building 2000, Room 2026, Monday to Thursday.</p>
<p><a href="https://careercenter.fullcoll.edu/career-closet/">Career Closet hours and details &rarr;</a></p></div>""",
  aside="""<div class="aside-card highlight"><h2>Career Center</h2>
<p class="small" style="margin:0 0 8px">Building 2000, Room 2027<br>714-992-7121<br>Mon–Thu 9 a.m.–6 p.m., Fri 9 a.m.–1 p.m.</p><ul>
<li><a href="https://fullcoll.joinhandshake.com/login">Handshake login</a></li>
<li><a href="https://careercenter.fullcoll.edu/">Career Center website</a></li>
<li><a href="https://careercenter.fullcoll.edu/calendar/">Workshops and webinars</a></li>
<li><a href="https://fullcoll.instructure.com/enroll/WHKEJW">Career Center in Canvas</a></li>
<li><a href="https://forms.office.com/r/T1XCq0cEpB">Ask for help (intake form)</a></li></ul></div>
<div class="aside-card"><h2>Get experience</h2><ul><li><a href="internships.html">Internships for credit</a></li></ul></div>""",
  todo=""),

 dict(file="clubs.html", title="Division Clubs", eyebrow="Beyond class",
  lead="Student clubs and honor societies supported by Business &amp; CIS faculty. Meet students who share your interests, build your resume, and have fun along the way.",
  body="""{{CLUBS}}
<p class="small">Club advisors: to add or update your club, email <a href="mailto:ggraves@fullcoll.edu">Gary Graves</a> with its name, advisor, meeting times, sign-up link, social accounts, and logo.</p>""",
  aside="",
  todo=""),

 dict(file="contact.html", title="Contact &amp; Hours", eyebrow="Division office",
  lead="Stop by, call, or email the Business &amp; CIS Division office. We will point you to the right person.",
  body="""<div class="block"><h2>Division office</h2>
<div class="tablebox"><table><tbody>
<tr><th scope="row">Location</th><td>Building 300, Suite 314<br>321 E. Chapman Ave., Fullerton, CA 92832</td></tr>
<tr><th scope="row">Conference room</th><td>Building 300, Room 325</td></tr>
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
  todo=""),

 dict(file="accessibility.html", title="Accessibility", eyebrow="About this site",
  lead="The Business &amp; CIS Division wants every student, family member, and visitor to be able to use this website, including people who use assistive technology.",
  body="""<div class="block"><h2>Our commitment</h2>
<p>This website is designed to meet the Web Content Accessibility Guidelines (WCAG) 2.1 at Level AA, the standard used for ADA and Section 508 compliance at California community colleges.</p></div>
<div class="block"><h2>What we do</h2>
<ul>
<li>Every page works with a keyboard alone, and a "Skip to content" link appears first.</li>
<li>Text and controls meet WCAG color contrast in light and dark themes.</li>
<li>Pages use clear headings, landmarks, and labels so screen readers can move through them.</li>
<li>Pages reflow on small screens and at up to 400 percent zoom without sideways scrolling.</li>
<li>Moving content can be paused, and animation stops if your device is set to reduce motion.</li>
<li>Each page is available in English and Spanish, and the page language is marked for screen readers.</li>
</ul></div>
<div class="block"><h2>Content we link to</h2>
<p>Some pages link to tools run by other offices, such as the class schedule, the college catalog, online forms, and Canvas. Some program documents are PDF files. If any of these is hard for you to use, contact us and we will provide the information in another format.</p></div>
<div class="block"><h2>Report a problem</h2>
<p>If something on this site does not work for you, tell us the page and what happened. We will respond within five business days.</p>
<ul><li>Email: buscis@fullcoll.edu</li><li>Phone: 714-992-7032</li><li>Visit: Building 300, Suite 314</li></ul></div>""",
  aside="""<div class="aside-card highlight"><h2>Disability Support Services</h2><p class="small" style="margin:0 0 8px">For classroom and testing accommodations, contact Fullerton College Disability Support Services.</p><ul><li><a href="https://dss.fullcoll.edu/">Disability Support Services (DSS)</a></li></ul></div>
<div class="aside-card"><h2>Display options</h2><p class="small" style="margin:0">Use the theme buttons at the top of any page to choose light, dark, or your device's setting. Your choice is remembered on this device.</p></div>""",
  todo="Confirm the five-business-day response time, and ask Campus Communications whether the college has an official accessibility statement to link to."),
]

COUNSELORS = [  # (name, title, email)
 ("Olivia Barajas, M.S.", "Career Education Counselor", "obarajas@fullcoll.edu"),
 ("Lovrina Castillo", "Career Education Counselor", "lcastillo2@fullcoll.edu"),
 ("Field Nguyen, M.S.", "Career Education Counselor", "fdo@fullcoll.edu"),
 ("Pamela Skiles, M.S.", "Career Education Counselor", "pskiles1@fullcoll.edu"),
]
