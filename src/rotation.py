# Course rotations: which semesters each course is usually offered. Semesters only, no years,
# so the page stays current. Update from each department's rotation file when it changes.
# Row: (course, title, fall, spring, summer, winter, note)
# Modes: D = day, N = night, S = Saturday, O = online, Y = offered (format not listed)
# Notes are (English, Spanish).

ACCT_ROWS = [
 ("ACCT 100 F", "Accounting for Small Business", "Y", "Y", "", "", ""),
 ("ACCT 101A F", "Financial Accounting", "Y", "Y", "Y", "", ""),
 ("ACCT 101B F", "Managerial Accounting", "Y", "Y", "Y", "", ""),
 ("ACCT 107 F", "Computerized Accounting with QuickBooks", "Y", "Y", "Y", "", ""),
 ("ACCT 110 F", "Payroll Accounting", "", "Y", "", "", ""),
 ("ACCT 201A F", "Intermediate Accounting", "Y", "", "", "", ""),
 ("ACCT 201B F", "Intermediate Accounting", "", "Y", "", "", ""),
 ("ACCT 202 F", "Introduction to Cost Accounting", "", "Y", "", "", ""),
 ("ACCT 203 F", "Auditing", "Y", "", "", "", ""),
 ("ACCT 204 F", "Analysis of Financial Statements", "", "Y", "", "", ""),
 ("ACCT 205 F", "Ethics in Accounting", "Y", "", "", "", ""),
 ("ACCT 220 F", "Individual Income Tax", "Y", "", "", "", ""),
 ("ACCT 230 F", "Excel for Accounts", "", "Y", "", "", ""),
 ("ACCT 250 F", "Forensics Accounting", "Y", "", "", "", ""),
 ("ACCT 295 F", "Accounting Internships", "Y", "Y", "", "", ""),
]

SUB = ("May require a paid subscription to a third-party website", "Puede requerir una suscripción de pago a un sitio web externo")
PLEG_REQUIRED = [
 ("PLEG 101 F", "Introduction to Paralegal Studies", "NO", "NO", "", "", ""),
 ("PLEG 104 F", "Introduction to Legal Research and Terminology", "N", "N", "", "", SUB),
 ("PLEG 105 F", "Introduction to Legal Writing", "N", "N", "", "", ""),
 ("PLEG 116 F", "Law Office Technology", "O", "O", "O", "", SUB),
 ("PLEG 201 F", "Civil Litigation I", "N", "N", "", "", ""),
 ("PLEG 202 F", "Civil Litigation II", "N", "N", "", "", ""),
 ("PLEG 221 F", "Paralegal Ethics", "NO", "NO", "", "O", ""),
 ("PLEG 223 F", "Advanced Legal Research and Writing", "N", "N", "", "", SUB),
]
PLEG_ELECTIVE = [
 ("PLEG 203 F", "Tort Law", "", "N", "N", "", ("Spring in even years; summer in odd years", "Primavera en años pares; verano en años impares")),
 ("PLEG 204 F", "Family Law", "", "N", "", "", ("Spring in odd years", "Primavera en años impares")),
 ("PLEG 205 F", "Probate, Wills, and Trusts", "", "N", "", "", ("Spring in even years", "Primavera en años pares")),
 ("PLEG 208 F", "Workers' Compensation Law", "", "", "N", "", ("Summer in even years", "Verano en años pares")),
 ("PLEG 209 F", "Criminal Law and Procedure", "N", "N", "", "", ("Spring in odd years; fall in even years", "Primavera en años impares; otoño en años pares")),
 ("PLEG 210 F", "Paralegal Internship", "N", "N", "", "", ("Fall and spring only", "Solo otoño y primavera")),
 ("PLEG 211 F", "Real Property Law and Procedure (with RE 102 F)", "O", "O", "", "", ("Spring in odd years", "Primavera en años impares")),
 ("PLEG 213 F", "Employment and Labor Law", "", "", "N", "", ("Summer in even years", "Verano en años pares")),
 ("PLEG 214 F", "Contract Law and Procedure (with BUS 245 F)", "N", "", "", "", ("Fall in odd years", "Otoño en años impares")),
 ("PLEG 215 F", "Electronic Discovery and Software Application", "", "", "O", "", ("Every summer. " + SUB[0], "Cada verano. " + SUB[1])),
 ("PLEG 217 F", "Immigration Law", "NS", "", "", "", ("Fall in odd years", "Otoño en años impares")),
 ("PLEG 222 F", "Alternative Dispute Resolution", "", "N", "", "", ("Spring in even years", "Primavera en años pares")),
 ("PLEG 225 F", "Law Office Management", "NO", "", "N", "", ("Summer in odd years; fall in even years", "Verano en años impares; otoño en años pares")),
 ("PLEG 226 F", "Constitutional Law", "N", "", "", "", ("Every fall", "Cada otoño")),
]

# From the CIS course rotation (Fall and Spring columns). The source lists no summer or winter terms.
CIS_ROWS=[('CIS 100 F', 'Introduction to Personal Computers', 'DNO', 'DNO', '', '', ''), ('CIS 103 F', 'Computer Keyboarding', 'O', 'O', '', '', ''), ('CIS 106 F', 'Beginning Spreadsheet (MS Excel)', 'O', 'O', '', '', ''), ('CIS 107 F', 'Intro to Operating Systems', 'O', 'O', '', '', ''), ('CIS 111 F', 'Intro to Information Systems', 'DNO', 'DO', '', '', ''), ('CIS 113 F', 'Intro to Big Data Analytics', 'O', 'O', '', '', ''), ('CIS 120 F', 'Project Management', 'O', 'O', '', '', ''), ('CIS 123 F', 'Beginning Word Processing', 'O', 'O', '', '', ''), ('CIS 152 F', 'Web Design', 'D', 'D', '', '', ''), ('CIS 154 F', 'JavaScript Programming I', 'O', 'O', '', '', ''), ('CIS 157 F', 'Web Design II', 'O', 'O', '', '', ''), ('CIS 180 F', 'Intro to Networking Concepts', 'DO', 'DO', '', '', ''), ('CIS 181 F', 'Computer Certification Preparation I', 'O', 'O', '', '', ''), ('CIS 182 F', 'Computer Certification Preparation II', 'O', '', '', '', ''), ('CIS 201 F', 'Introduction to Python Programming', 'DNO', 'DNO', '', '', ''), ('CIS 213 F', 'Python for Data Analytics', 'O', 'O', '', '', ''), ('CIS 215 F', 'Excel for Data Analytics and Big Data', 'O', 'O', '', '', ''), ('CIS 226 F', 'Java Programming I', 'DN', 'DN', '', '', ''), ('CIS 235 F', 'Intro to Cloud Computing', 'O', 'O', '', '', ''), ('CIS 237 F', 'Cloud Computing Architecture', 'O', 'O', '', '', ''), ('CIS 238 F', 'Cloud Computing Database', 'D', 'D', '', '', ''), ('CIS 290 F', 'Linux/Unix Operating System', 'D', 'D', '', '', ''), ('CIS 295 F', 'Computer Information Systems Internship', 'O', 'O', '', '', ''), ('CIS 298 F', 'Advanced Computer Topics', 'D', 'D', '', '', '')]
CISG_ROWS=[('CISG 100 F', 'Intro to Computer Game Design', 'DO', 'DO', '', '', ''), ('CISG 101 F', 'Advanced Computer Game Design', 'O', 'O', '', '', ''), ('CISG 103 F', 'History of Video Games', 'D', 'D', '', '', ''), ('CISG 105 F', 'Intro to AR/VR', 'D', 'D', '', '', ''), ('CISG 110 F', 'Intro to Prog for Computer Games', 'O', 'O', '', '', ''), ('CISG 112 F', 'Foundations of Game Engine Programming', 'O', 'O', '', '', ''), ('CISG 150 F', 'Apple SWIFT Programming 1 Explorations', 'D', 'D', '', '', ''), ('CISG 185 F', 'Artificial Intelligence in Game Prog', 'N', 'N', '', '', ''), ('CISG 191 F', 'Electronic Sports (eSports) I Beginning', 'DN', 'DN', '', '', ''), ('CISG 192 F', 'Electronic Sports (eSports) II Intermediate', 'DN', 'DN', '', '', ''), ('CISG 193 F', 'Electronic Sports (eSports) III Advanced', 'N', 'N', '', '', '')]
CYBR_ROWS=[('CYBR 100 F', 'Cyber Hygiene', 'DO', 'DO', '', '', 'Formerly CIS 109 F'), ('CYBR 106 F', 'Intro to Cyber Security', 'DO', 'DO', '', '', 'Formerly CIS 160 F'), ('CYBR 206 F', 'Ethical Hacking', 'D', 'D', '', '', 'Formerly CIS 171 F'), ('CYBR 210 F', 'Network Security', 'D', 'D', '', '', 'Formerly CIS 183 F'), ('CYBR 220 F', 'Intro to Incident Response', 'O', 'O', '', '', 'Formerly CIS 165 F'), ('CYBR 230 F', 'Scripting Fundamentals', 'D', 'D', '', '', 'Formerly CIS 222 F'), ('CYBR 260 F', 'Cloud Security', 'O', 'O', '', '', ''), ('CYBR 290 F', 'Management of Information Security', 'O', 'D', '', '', 'Formerly CIS 166 F')]
CIS_NONE=[('CIS 102 F', 'Introduction to Open Source Software'), ('CIS 104 F', 'Presentation Graphics'), ('CIS 124 F', 'Advanced Word Processing'), ('CIS 130 F', 'Systems Analysis and Design'), ('CIS 142 F', 'Database I'), ('CIS 148 F', 'Intro to Personal Computer Communications'), ('CIS 149 F', 'Internet Entertainment'), ('CIS 150 F', 'Introduction to the Internet'), ('CIS 153 F', 'Business Web Graphics'), ('CIS 155 F', 'Web Page Multimedia Design I'), ('CIS 159 F', 'Introduction to XML'), ('CIS 176 F', 'Web Page Layout with CMS'), ('CIS 177 F', 'Web Design III'), ('CIS 200 F', 'Fundamentals of Computer Programming'), ('CIS 205 F', 'Advanced Spreadsheet - MS Excel'), ('CIS 210 F', 'Advanced Python Programming'), ('CIS 212 F', 'Robotic Programming'), ('CIS 217 F', 'Visual Basic Programming I'), ('CIS 219 F', 'Visual Basic Programming II'), ('CIS 220 F', 'Web Server Programming'), ('CIS 221 F', 'Intro to C# Programming'), ('CIS 223 F', 'Programming in C++'), ('CIS 227 F', 'Advanced C# Programming'), ('CIS 228 F', 'Java Programming II'), ('CIS 229 F', 'XML Programming'), ('CIS 230 F', 'PHP and MySQL Programming'), ('CIS 240 F', 'Intro to Mobile Applications'), ('CIS 242 F', 'Databases II'), ('CIS 255 F', 'Web Page Multimedia Design II'), ('CIS 270 F', 'SQL Server Administration'), ('CIS 280 F', 'Introduction to Oracle: SQL and PL/SQL'), ('CIS 281 F', 'Introduction to Networking Hardware'), ('CIS 285 F', 'Windows Server'), ('CIS 286 F', 'Web Server Management'), ('CIS 287 F', 'Exchange Server'), ('CIS 289 F', 'Windows Active Directory'), ('CISG 151 F', 'Apple SWIFT Programming 2 Fundamentals'), ('CISG 152 F', 'Apple SWIFT Programming 3 Data Collections'), ('CISG 160 F', 'C# for Game Programming'), ('CISG 170 F', 'Java for Game Programming'), ('CISG 175 F', 'Multimedia for Game Programming'), ('CISG 182 F', 'DirectX Graphics Programming'), ('CISG 190 F', 'Prog Multi-User Online Games'), ('CYBR 233 F', 'Application Security')]
