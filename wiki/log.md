# Wiki Log

Chronological record of wiki operations.

## [2026-05-18] organize | GitHub projects and other category
- Created wiki/github-projects.md with summary of 8 GitHub repositories
- Documented: BudgetTool, DeltaDash, DeltaVision, EvolutionSimSite
- Documented: PersonalWebsite, RoADashboard, SeeStar-AstroStat-2.0, TheAncientWorld
- Organized 'other' category (133 files → 51 files)
- Created 8 new specific categories with 82 files:
  - history-us-politics: 14 files (wars, politics, immigration)
  - ballistics-armor: 9 files (standards, protection materials)
  - job-application: 17 files (cover letters, offers, applications)
  - lab-coursework: 12 files (lab manuals, coursework)
  - literature-humanities: 8 files (ethics, literature, philosophy)
  - materials-science: 13 files (polymers, material properties)
  - physics-research: 4 files (experiments, research papers)
  - chemical-engineering: 5 files (transport, separation processes)
- Created organization script: organize_other_category.py
- Updated other.md to reference new categories

## [2026-05-18] enhance | CASCADE.md schema updated
- Completely rewrote CASCADE.md with comprehensive guidelines
- Added raw-sources/ directory structure documentation
- Detailed INGEST, QUERY, LINT operations
- Added chat conversation processing guidelines
- Added automation examples (morning briefing, call transcripts)
- Documented page conventions and categorization guidelines
- Added troubleshooting section
- Added tips and tricks section
- Added "Why This Works" explanation
- Made it a living document for co-evolution

## [2026-05-18] setup | Chat conversation integration
- Created raw-sources/ directory structure
- Created raw-sources/chatgpt/ for ChatGPT exports
- Created raw-sources/claude/ for Claude exports
- Created raw-sources/README.md with integration guide
- Created chatgpt/TEMPLATE.md for manual conversation saves
- Created Scripts/automation/process_chat_conversations.py
- Added chat integration section to daily-tasks.md

## [2026-05-18] init | Wiki structure created
- Created wiki/ folder
- Created CASCADE.md schema file
- Initialized wiki/index.md and wiki/log.md

## [2026-05-18] ingest | Bulk processing of junk_drawer/
- Processed 2 markdown files from junk_drawer/
- Extracted text from 912 PDF files using pdftotext
- Categorized files into 15 categories:
  - academic-homework: 184 files
  - academic-lecture: 98 files
  - academic-exam: 75 files
  - other: 260 files
  - academic-syllabus: 33 files
  - academic-lab: 30 files
  - personal-resume: 18 files
  - personal-application: 12 files
  - personal-academic: 10 files
  - technical-safety: 13 files
  - legal-document: 8 files
  - research-paper: 6 files
  - financial-document: 5 files
  - media-transcript: 1 file
  - empty: 158 files (skipped)
- Created 753 wiki pages for non-empty files
- Created 14 category pages
- Updated wiki/index.md with 769 total pages
- Total sources processed: 914 files (2 markdown + 912 PDF)

## [2026-05-18] concept | Created concept/entity pages
- Analyzed all wiki pages for recurring entities and concepts
- Created 24 concept/entity pages:
  - SiC (271 references)
  - DOE (295 references)
  - North Carolina State University (159 references)
  - Chemical Engineering (88 references)
  - NCSU (114 references)
  - LEAN (95 references)
  - Wolfspeed (21 references)
  - MSA (13 references)
  - Process Engineering (13 references)
  - Doble W Servicios (14 references)
  - Silicon Carbide (21 references)
  - Chemical Vapor Deposition (14 references)
  - CVD (11 references)
  - Statistical Process Control (9 references)
  - SPC (9 references)
  - Design of Experiment (12 references)
  - Measurement Systems Analysis (7 references)
  - Fourier Transform Infrared Spectrometer (7 references)
  - Material Science Engineering (18 references)
  - Process Change Review Boards (7 references)
  - PCRB (7 references)
  - Gauge Repeatability and Reproducibility (3 references)
  - GR&R (7 references)
  - BEE Educated (15 references)
- Updated wiki/index.md with 793 total pages

## [2026-05-18] reorganization | Cleaned up and reorganized wiki
- Analyzed 260 files in 'other' category
- Deleted 102 unwanted files (gaming, photography presets, corrupted, empty)
- Reclassified files into improved categories:
  - academic-homework: 268 files (previously misclassified)
  - academic-lecture: 245 files (previously misclassified)
  - academic-lab: 28 files (previously misclassified)
  - research-paper: 13 files (dedicated category for research)
  - other: 206 files (remaining miscellaneous)
  - academic-syllabus: 2 files
  - technical-safety: 12 files
  - personal-resume: 18 files
  - personal-academic: 9 files
  - financial-document: 8 files
- Cleared old wiki pages and rebuilt with new categorization
- Created 809 wiki pages across 10 categories
- Updated wiki/index.md with 837 total pages
- Research papers now clearly separated from other content

## [2026-05-18] ingest | Google Drive files added
- Unpacked 3 zip files from Google Drive to junk_drawer/
- Deleted zip files after extraction
- Extracted text from 26/27 new PDFs (1 file corrupted)
- New content includes:
  - DeltaV business documents (24 PDFs)
  - College academic files (1 PDF)
  - Additional materials from subdirectories
- Rebuilt wiki with new content:
  - academic-homework: 271 files (+3)
  - academic-lab: 31 files (+3)
  - academic-lecture: 247 files (+2)
  - research-paper: 14 files (+1)
  - other: 222 files (+16)
- Created 835 wiki pages across 10 categories
- Updated wiki/index.md with 859 total pages (+22)

## [2026-05-18] reorganization | Further improved categorization
- Analyzed remaining 'other' category (222 files) for better organization
- Improved categorization logic with new patterns:
  - Added philosophy/ethics paper category
  - Better lab report detection (lab#, lab report, reactor, heat exchanger)
  - ChE312 course materials categorization
  - Personal document detection (travel itineraries, personal notes)
  - Business document detection (senior design, company documents)
- Reclassified files from 'other' into better categories:
  - academic-homework: 260 files (-11 from other)
  - academic-lab: 49 files (+27 from other)
  - academic-lecture: 120 files (+19 from other)
  - academic-paper: 12 files (new category)
  - business-document: 6 files (+2 from other)
  - personal-document: 24 files (+4 from other)
  - textbook: 10 files (+2 from other)
  - research-paper: 6 files (+1 from other)
  - other: 159 files (-63 from improved categorization)
- Deleted 61 corrupted/empty files
- Deleted 15 date-based documents (_MM_DD_YYYY format)
- Rebuilt wiki with 759 pages across 15 categories
- Updated wiki/index.md with 827 total files

## [2026-05-18] reorganization | Work category and final cleanup
- Created work category structure for job application materials:
  - work-wolfspeed: 4 files (Wolfspeed-specific documents)
  - work-deltav: 12 files (DeltaV/ASP/DeltaV International documents)
  - work-general: 22 files (general job applications, cover letters)
  - work-academic: 20 files (personal academic papers from work)
- Deleted 4 duplicate files (kept latest versions)
- Renamed 6 merged PDFs to reflect content
- Reclassified files into work categories from 'other':
  - work-wolfspeed: 4 files (new category)
  - work-deltav: 12 files (new category)
  - work-general: 22 files (new category)
  - work-academic: 20 files (new category)
  - other: 135 files (-24 from work categorization)
- Rebuilt wiki with 749 pages across 18 categories
- Updated wiki/index.md with 831 total files
- Total organization improvements:
  - Deleted 76 unwanted files (61 corrupted + 15 date-based)
  - Deleted 4 duplicate files
  - Renamed 6 merged PDFs
  - Created 4 new work categories
  - Reduced 'other' category from 222 to 135 files (-87 files)

## [2026-05-18] ingest | GitHub repositories integrated
- Cloned 8 public repositories from Gonhog-Creator:
  - DeltaDash
  - RoADashboard
  - DeltaVision
  - PersonalWebsite
  - BudgetTool
  - EvolutionSimSite
  - SeeStar-AstroStat-2.0 (fork)
  - TheAncientWorld
- Filtered and processed GitHub content:
  - Processed 950 code and documentation files
  - Skipped 5766 images and binary files
  - Skipped 6 large files (>5MB)
  - Skipped 120 other files
  - Extracted text from 800 files
- Created github-code category for all GitHub content
- Updated categorization logic to handle code files and directory paths
- Rebuilt wiki with 1689 pages across 19 categories
  - github-code: 940 files (new category)
- Updated wiki/index.md with 1524 total files
- Knowledge base now includes complete GitHub codebase while remaining lean and efficient

## [2026-05-18] optimization | Storage cleanup and textbook removal
- Analyzed junk_drawer storage (1.3G total)
- Identified textbooks as largest storage contributor (~300M+)
- Removed 7 duplicate textbooks:
  - Materials-Textbook-8th-Edition (4 duplicates, 82M saved)
  - Chemical Reactions and Chemical Reactors (1 duplicate, 24M saved)
  - Transport Processes and Separation Process Principles (1 duplicate, 20M saved)
  - Understanding Process Dynamics and Control (1 duplicate, 15M saved)
- Removed Health and Exercise Wellbeing textbook (56M)
- Total space saved: 198M
- Removed 10 GitHub build/cache files earlier
- Rebuilt wiki with 1671 pages across 19 categories
  - textbook: 5 files (down from 11)
  - github-code: 930 files (down from 940)
  - other: 133 files (down from 135)
- Updated wiki/index.md with 1521 total files
- Knowledge base now significantly more optimized and storage-efficient
