# Open items before launch

Last updated: October 19, 2026. Check items off as they are confirmed.

## A. Facts to verify

### People and roles
- [ ] Program leads carried over from the 2023 brochure: Marcus Wilson (Business), Barry McCarthy (International Business), Richard Ghidella (Real Estate), Brandon Tran (Accounting), Michael Moore (Paralegal), Anna Carlin (Cyber Security)
- [x] Confirmed leads: Gary Graves (Entrepreneurship, AI in Business), Marwin Luminarias (Marketing), Brian Roach (CIS), Carlos Antunez (Computer Gaming)
- [ ] Department coordinators: Kathy Standen and Marcus Wilson (Business Management), Brandon Tran (Accounting), Brian Roach (CIS); Michael Moore is Paralegal Studies Program Director (confirmed October 20)
- [x] Faculty names now match the official class schedule (October 19): Kathy Standen, Julianne Dixon, Kristine Wilson, Leonard Rosenblum, Santalia Carter, Brenda Klingenmaier, Steve John Haddadin, Richard Ghidella, Marwin Luminarias
- [x] Faculty roster checked against the division's faculty list (October 19): 72 faculty listed
  - Removed 11 who are not on the division list and have no classes in Fall 2026 or Spring 2027: Pascual, Snow, Oates, Reid, West, Collar, Douglas, Kazerooni, Woolridge, Yi, Peikes
  - Added Franco Torres (Paralegal); moved James Downs to Paralegal
  - Removed Aleksandra Uchlik, no longer with the division (October 24); 71 faculty listed
- [ ] Teaching but not on the division list; keep? Barry McCarthy (International Business lead), Kenneth Colby, Ross DiLeo, Justin Rife
- [ ] Joel Salcedo (full-time in another division, teaches BUS): list him?
- [ ] Franco Torres: add a "Find classes" button once he appears on the schedule
- [x] Names follow the class schedule, not HR (decided October 19): Marwin Luminarias, Rajen Vurdien, Robert Konefsky. Use the schedule name for anyone added later. Exceptions at the person's request: K. Lee Steidel, Alexandria (Brandi) Boyer (October 25)
- [x] Laura Melella removed from the CIS page (October 19)
- [ ] Jane Troop: Business Management (directory) or CIS (old CIS page)?
- [ ] Dean Dr. Dani Wilson: direct phone line? (new gray-background photo added October 19)
- [ ] Paralegal coordinator phone: (714) 992-7208
- [x] Counselors page: Counseling Center hours from counseling.fullcoll.edu, DegreeWorks link added (October 19)
- [ ] Counselors (Barajas, Castillo, Nguyen, Skiles): confirm the list is current

### Office
- [x] Location: Building 300, Division Office Suite 314; Conference Room 325 (confirmed October 19)
- [ ] Office hours: Mon–Thu 8 a.m.–7 p.m., Fri 8 a.m.–5 p.m.; summer Mon–Thu 8 a.m.–5 p.m., closed Friday

### Program details
- [ ] Start Here courses: BUS 100, BUS 180/181, BUS 256, MKT 100/151, BUS 131, RE 101, ACCT 100/101A, PLEG 101, CIS 100/111, CYBR 106 (corrected from CIS 160, October 19), CISG 100
- [ ] Claims carried over from the old site:
  - [ ] Accounting courses count toward the 24 accounting units required for the CPA exam
  - [ ] Real Estate covers the coursework for the CA salesperson and broker licenses
  - [ ] Cyber Security's CAE-CD designation is still current
  - [ ] Game Programming Skills Certificate is not eligible for financial aid
  - [ ] Digital Marketing Certificate is fully online and 19 units
  - [ ] AI unit counts: Foundations 12; Certificate and AS 21–23
  - [ ] Paralegal transfer agreements with National University and University of La Verne
- [ ] Each program lead reviews the highlights and short descriptions on their card and program page

### Resources and links
- [x] Division Clubs page rebuilt as club cards from `src/clubs.py` (October 22); Esports Club added (advisor Carlos Antunez)
- [x] Moot Court Club added (October 25, from Michael Moore)
- [x] Hornet Business Club advisors: Marwin Luminarias and Diana Hsueh (October 26)
- [ ] Club details still needed: Hornet Business Club meeting times
- [x] Accounting Society merged into the Hornet Business Club; removed from the clubs page (October 23)
- [ ] LEX contact: FCParalegalStudies@fullcoll.edu
- [ ] Internship contacts (Graves, Carlin, Moore), both Google Forms, and the Canvas space are current
- [x] Career page now uses Handshake (replaced FC Career Connect, the NACE job board, and VMock, which the Career Center no longer lists) (October 19)
- [ ] Career Center: confirm Handshake sign-in steps and Career Closet details are current each year
- [ ] LinkedIn "FC Alumni" group is the right one to link

## B. Content needed
- [x] Study Abroad: Florence 2028 flyer, planned courses, pending-approval notice, BUS 186 F funding, links to studyabroad.fullcoll.edu (October 19)
- [ ] Study Abroad: add cost and application dates when set; remove the pending-approval notice after the Board approves; update courses when final
- [ ] Headshots for 11 faculty (59 of 71 done; Jane Troop asked for no photo):
  - Accounting: Chen, Hoffman
  - Business Management: Boyer, Colby, C. Ghidella, Gomez-Velazquez, Hines
  - CIS: Fitzpatrick, Long
  - Paralegal: Downs, Torres
- [ ] Headshots of the counselors: Olivia Barajas done (October 19); still need Castillo, Nguyen, Skiles
- [ ] Official Business & CIS Division wordmark from Campus Communications
- [ ] Photos of students and campus, one per program page
- [ ] Optional: one student quote per program

## C. Content gaps: decide whether to add
- [ ] Transfer & FAQ section explaining AS-T vs. AA (can be adapted from the old FAQ page)
- [ ] CIS concentration details: Networking, Programming, Web Design, Computer Technician, Office Applications
- [ ] Which programs can be finished fully online
- [ ] Scholarships and tutoring links
- [ ] Dual enrollment for high school students
- [ ] Employer and partner page: advisory boards, hiring partners
- [x] Spanish versions of every page (added October 19; needs review, see section E)
- [ ] Confirm these old pages can be dropped: New certificates (2020), New courses, CAE notice, Business City field trip, NASA JPL internship, Late-start internship, RE 103 and MKT 208 promos, Buzzy blog, Typing Test, draft faculty page

## D. Technical
- [x] "Find classes" button on the 69 faculty cards with classes in Fall 2026 or Winter/Spring 2027 (October 19). Fall-only faculty open Fall 2026.
- [ ] Each new term: refresh `SCHEDULE_NAMES` in `src/people.py` (or have PHP read the schedule's instructors.json daily)
- [x] "Change My Major" link on the home page (Start here step 1 and Plan your classes) and the Forms page (October 19)
- [ ] Redirect file (`web.config`) so old addresses go to the new pages
- [ ] Copy seven documents from the old WordPress server into `/docs`: three course rotations (Accounting, CIS, Paralegal), the CPA worksheet, the FCAP flyer, and both internship brochures
- [ ] Convert the build to PHP: `header.php`, `footer.php`, `programs.php`, `people.php`
- [ ] Confirm with IT that PHP is enabled on the IIS server and which version; get FTP access
- [ ] Browser-tab icon (an approved FC mark), social-share image, 404 page, footer search box
- [ ] Ask Campus Communications whether division sites must include the college analytics tag
- [ ] Full link check before launch
- [x] Automated accessibility audit: axe-core, all 42 pages, light and dark: 0 issues; 320px reflow: pass

## G. Career information
- [x] Every program page links each occupation to O*NET (Spanish pages: Mi Próximo Paso) and lists free career research tools
- [x] Each program links to its own Hornet Pathways page for course maps and the full career list
- [ ] AI in Business is not on Hornet Pathways yet; update its link in `src/programs.py` (`PW`) when it is added
- [ ] Optional: once a year, import program details from Pathways (units, terms to degree, learning outcomes) and let program leads pick which careers to feature

## E. Spanish version
- [ ] Review by a fluent Spanish speaker (faculty, staff, or the college's translation service), especially program descriptions and the Paralegal legal notice
- [ ] Confirm the informal "tú" voice fits the college's style, or switch to "usted"
- [ ] Ask Campus Communications whether the college has approved Spanish terms for program names
- [ ] Official degree and certificate names stay in English (they match the catalog); confirm this is the preferred approach

## F. Accessibility (ADA, WCAG 2.1 AA)
- [ ] Manual screen reader test with NVDA (Windows) and VoiceOver (Mac/iPhone); DSS may be able to help
- [ ] Linked PDFs (course rotations, CPA worksheet, FCAP flyer, internship brochures) must be tagged and accessible, or replaced with web pages
- [ ] Any future photos need alt text; any video needs captions
- [ ] Confirm the accessibility statement's five-business-day response time and contact
- [ ] Ask Campus Communications whether the college has an official accessibility statement or web accessibility contact to link

## H. Future enhancements
- [x] Faculty who prefer no photo are listed as text under their department (`NO_PHOTO` in `src/people.py`); Jane Troop (October 25). After this weekend, move anyone still without a photo there too
- [x] LinkedIn link on faculty cards (October 21): add each person to `LINKEDIN` in `src/people.py` as links come in
- [ ] "Get the KSAs" section on each program page: the knowledge, skills, and abilities students gain from the program's courses, and how they lead to jobs (requested October 19; waiting on CurricUNET)
  - Source: course student learning outcomes (SLOs) from CurricUNET
  - Match each skill to the program's target jobs using the O*NET knowledge, skills, and abilities lists already linked on each program page
  - Start with the Workforce Pell candidates: Real Estate Sales, Entrepreneurship Skills, Business Data Analytics, AI Foundations
- [x] Course Rotation page (rotation.html), semesters only, no years (October 20): Accounting, CIS (with Computer Gaming and Cyber Security), Paralegal; linked from the home page and each of those program pages
  - Source files: Accounting (9/30/25), CIS spreadsheet (Spring 2026 and Fall 2026 columns), Paralegal (eff. 02/2026); data lives in `src/rotation.py`
- [x] Business Management, International Business, Marketing, and Real Estate rotations added (October 20, from the rotation revised 8/21/26), with 8-week session details; linked from those program pages plus Entrepreneurship and AI in Business
- [ ] Not on the Business rotation: BUS 187 F, BUS 246 F, RE 207 F (listed under their tables). Confirm
- [ ] CIS rotation lists no summer or winter terms; 44 CIS courses have no planned semester (shown in a collapsed list). Confirm with CIS
- [ ] Accounting: list the courses that count toward the CPA exam's 24 accounting units (faculty suggestion, October 20)
  - The Accounting page already says all FC accounting courses count and links the CPA worksheet PDF; need the course list from the Accounting department
