# Open items before launch

Last updated: October 18, 2026. Check items off as they are confirmed.

## A. Facts to verify

### People and roles
- [ ] Program leads carried over from the 2023 brochure: Marcus Wilson (Business), Barry McCarthy (International Business), Richard Ghidella (Real Estate), Brandon Tran (Accounting), Michael Moore (Paralegal), Anna Carlin (Cyber Security)
- [x] Confirmed leads: Gary Graves (Entrepreneurship, AI in Business), Marwin Luminarias (Marketing), Brian Roach (CIS), Carlos Antunez (Computer Gaming)
- [ ] Department coordinators: Kathy Standen and Marcus Wilson (Business Management), Brandon Tran (Accounting), Brian Roach (CIS), Michael Moore (Paralegal)
- [ ] Name spellings: Kathleen or Kathy Standen; Richard or Rich Ghidella; Marwin Luminarias
- [ ] Faculty roster (81 names from the old directory): remove anyone who has left and add new hires
- [ ] Laura Melella appears on the old CIS page but not in the directory. Include her?
- [ ] Jane Troop: Business Management (directory) or CIS (old CIS page)?
- [ ] Dean Dr. Dani Wilson: direct phone line? A larger photo with a gray background?
- [ ] Paralegal coordinator phone: (714) 992-7208
- [ ] Counselors (Barajas, Castillo, Nguyen, Skiles) and Fall hours

### Office
- [ ] Location: Building 300, Room 325 (the old site said Suite 314)
- [ ] Office hours: Mon–Thu 8 a.m.–7 p.m., Fri 8 a.m.–5 p.m.; summer Mon–Thu 8 a.m.–5 p.m., closed Friday

### Program details
- [ ] Start Here courses: BUS 100, BUS 180/181, BUS 256, MKT 100/151, BUS 131, RE 101, ACCT 100/101A, PLEG 101, CIS 100/111, CIS 160, CISG 100
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
- [ ] Club advisors and meeting times
- [ ] Is the Accounting Society still active at fullcollacctsociety@gmail.com?
- [ ] LEX contact: FCParalegalStudies@fullcoll.edu
- [ ] Internship contacts (Graves, Carlin, Moore), both Google Forms, and the Canvas space are current
- [ ] Career Connect contact: Jennifer Merchant
- [ ] LinkedIn "FC Alumni" group is the right one to link

## B. Content needed
- [ ] Study Abroad: Florence 2028 courses, cost, dates, interest form
- [ ] Headshots for 38 faculty:
  - Accounting: Chen, Hoffman, Lim, Pascual, St. John, C. Tran, Uchlik
  - Business Management: Boyer, Caudillo, Chan, Colby, Conlin, J. Dixon, Downs, Durfield, Furlong, C. Ghidella, Gomez-Velazquez, Hines, Jezek-Arriaga, Reid, Rife, Steidel, Troop, Underdue, Webb, K. Wilson
  - CIS: Roach, Collar, Douglas, Fitzpatrick, Kazerooni, Konefsky, Long, Rosenblum, Yi, Zentner
  - Paralegal: Peikes
- [ ] Headshots of the four counselors
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
- [ ] Spanish versions of key pages (later phase)
- [ ] Confirm these old pages can be dropped: New certificates (2020), New courses, CAE notice, Business City field trip, NASA JPL internship, Late-start internship, RE 103 and MKT 208 promos, Buzzy blog, Typing Test, draft faculty page

## D. Technical
- [ ] Redirect file (`web.config`) so old addresses go to the new pages
- [ ] Copy seven documents from the old WordPress server into `/docs`: three course rotations (Accounting, CIS, Paralegal), the CPA worksheet, the FCAP flyer, and both internship brochures
- [ ] Convert the build to PHP: `header.php`, `footer.php`, `programs.php`, `people.php`
- [ ] Confirm with IT that PHP is enabled on the IIS server and which version; get FTP access
- [ ] Browser-tab icon (an approved FC mark), social-share image, 404 page, footer search box
- [ ] Ask Campus Communications whether division sites must include the college analytics tag
- [ ] Full link check and accessibility pass before launch
