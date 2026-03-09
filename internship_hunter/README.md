# Internship Hunter

A very lightweight command-line Python project for internship discovery and networking outreach.

## 1) Setup

```bash
cd internship_hunter
python -m pip install -r requirements.txt
```

## 2) Generate your files

```bash
python jobs.py
python startups.py
python outreach.py
```

This creates:

- `jobs.csv` → internship leads (company, role title, link)
- `startups.csv` → startup target list
- `outreach.txt` → ready-to-send networking messages

## 3) How to actually use this to start applying

### A. Build your job list (`jobs.csv`)

1. Open `jobs.csv` in Excel/Google Sheets.
2. Add columns:
   - `status` (Not started / Applied / Interview / Rejected)
   - `date_applied`
   - `resume_version`
   - `notes`
3. Apply to roles with the best fit first (finance, sales, operations, growth, GTM internships).
4. Track every application immediately after submitting.

> Note: Indeed may occasionally block scraping (HTTP 403). If that happens, `jobs.csv` can be empty. Re-run later, or manually add internships from LinkedIn/Wellfound/company career pages into the same CSV format.

### B. Start networking (`outreach.txt`)

1. Open `outreach.txt`.
2. For each company section, copy the message and slightly personalize 1 line:
   - why that company
   - why that team
   - a recent product/company update
3. Send messages to recruiters, analysts, associates, and recent grads on LinkedIn.
4. Goal: 5–10 outreach messages/day.

### C. Weekly cadence that works

- **Mon/Wed/Fri**: source new roles and apply (target 5–15/week)
- **Daily**: send outreach + follow-ups
- **Weekly**: review tracker and double down on companies that reply

### D. Quick personalization template (recommended)

Use this before sending each note:

- "I noticed `<company signal/news>` and found it really interesting because `<1 sentence reason>`."

Even one personalized line improves reply rates.

## What each script does

- `jobs.py`
  - Searches Indeed for **"business internship Toronto"**
  - Extracts company, role title, and link
  - Saves up to ~30 results to `jobs.csv`

- `startups.py`
  - Writes a built-in list of Toronto startups and growth companies
  - Saves to `startups.csv` with `company` and `industry`

- `outreach.py`
  - Reads `startups.csv`
  - Generates a short LinkedIn-style outreach message for each company using Kyam's profile
  - Saves all messages to `outreach.txt`

- `utils.py`
  - Contains helper functions for CSV writing and message formatting
