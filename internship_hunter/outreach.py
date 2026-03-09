import csv
from pathlib import Path

from utils import format_message


PROFILE = {
    "name": "Kyam Alarakhia",
    "school": "McGill University (BCom Finance + ITM)",
}


def read_startups(path="startups.csv"):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


if __name__ == "__main__":
    startups = read_startups("startups.csv")
    lines = []

    for row in startups:
        company = row["company"]
        lines.append(f"=== {company} ===")
        lines.append(format_message(company, PROFILE))
        lines.append("")

    Path("outreach.txt").write_text("\n".join(lines), encoding="utf-8")
    print(f"Saved outreach messages for {len(startups)} companies to outreach.txt")
