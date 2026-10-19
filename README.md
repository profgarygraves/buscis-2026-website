# Business & CIS Division Website (2026 redesign)

Redesign of the Fullerton College Business & Computer Information Systems Division website, currently at [buscis.fullcoll.edu](https://buscis.fullcoll.edu).

**Live design preview:** https://profgarygraves.github.io/buscis-2026-website/

This preview is for faculty and staff review. It is not the official site.

## How to give feedback

- **Email** Prof. Gary Graves at ggraves@fullcoll.edu with the page name and what to change.
- **GitHub users:** [open an issue](https://github.com/profgarygraves/buscis-2026-website/issues) for each page or topic.
- **Program leads:** please check your program page for start courses, awards, highlights, faculty, and contacts. See [CHECKLIST.md](CHECKLIST.md) for open items.

## What's in the preview

| Page | File |
|---|---|
| Homepage: programs, Start Here path, student resources | `index.html` |
| 11 program pages | `business.html`, `entrepreneurship.html`, `ai-in-business.html`, `marketing.html`, `international-business.html`, `real-estate.html`, `accounting.html`, `paralegal.html`, `cis.html`, `cyber-security.html`, `computer-gaming.html` |
| Faculty & Staff directory | `faculty.html` |
| Student resources | `forms.html`, `counselors.html`, `internships.html`, `study-abroad.html`, `career.html`, `clubs.html` |
| Contact & hours | `contact.html` |

## Design principles

- Follows the [Fullerton College brand standards](https://www.fullcoll.edu/communications/brand/): Stinger Blue, Hornet Yellow, and the secondary palette; Century Gothic with an Open Sans fallback.
- Compact header with a link back to fullcoll.edu, plus the official FC footer.
- Programs come first: each has a Start Here course, linked degrees and certificates, a program lead, and Orange County career data.
- Low maintenance: no news feed. Course requirements link to the official catalog, and class links go to the live schedule, which always opens the current term.
- Built with HTML and CSS only. No JavaScript is required.

## How the site is built

Content lives in data files, so most updates are a one-line edit:

| File | What it holds | Becomes on the live server |
|---|---|---|
| `src/programs.py` | Programs, awards, start courses, careers, program leads | `inc/programs.php` |
| `src/people.py` | Faculty, staff, division social accounts | `inc/people.php` |
| `src/pages.py` | Student resource pages | individual `.php` pages |
| `src/header.html`, `src/footer.html` | Shared header and FC footer | `inc/header.php`, `inc/footer.php` |
| `src/style.css` | All styles | `css/style.css` |
| `img/people/` | Headshots, 600x750, named `first-last.jpg` | same |

To rebuild the preview after an edit:

```
python3 build.py --site     # writes the GitHub Pages preview to docs/
```

The live division server supports HTML, PHP, and CSS only, so the final version will use PHP includes in place of this build step.

## Headshot standard

Portrait 4:5, delivered at 1200x1500 and published at 600x750, shoulders up, plain gray background. Name the file `first-last.jpg` to match the directory, and it appears automatically on the next build. Faculty without a photo show their initials on their department color.
