import csv
from pathlib import Path


def write_csv(path, fieldnames, rows):
    """Write dictionaries to CSV using given fieldnames."""
    out_path = Path(path)
    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def format_message(company, profile):
    """Create a concise LinkedIn-style outreach message."""
    return (
        f"Hi {company} team,\n\n"
        f"My name is {profile['name']}, and I'm a {profile['school']} student studying "
        f"Finance + ITM. I recently worked as a Sales Intern at GoMaterials, where I "
        f"supported sales pipeline development and CRM execution.\n\n"
        f"I've been following {company} and would really value a short 15-minute "
        f"conversation to learn more about your team and growth journey.\n\n"
        "Thanks so much for your time!\n"
        f"{profile['name']}"
    )
