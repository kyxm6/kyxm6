import requests
from bs4 import BeautifulSoup

from utils import write_csv


QUERY = "business internship Toronto"
URL = "https://ca.indeed.com/jobs"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/123.0.0.0 Safari/537.36"
    )
}


def scrape_jobs(limit=30):
    params = {"q": QUERY, "l": "Toronto, ON"}
    response = requests.get(URL, params=params, headers=HEADERS, timeout=20)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    jobs = []

    for card in soup.select("div.job_seen_beacon"):
        title_tag = card.select_one("h2.jobTitle a")
        company_tag = card.select_one("span.companyName")

        if not title_tag or not company_tag:
            continue

        title = title_tag.get_text(strip=True)
        company = company_tag.get_text(strip=True)
        href = title_tag.get("href", "")
        link = f"https://ca.indeed.com{href}" if href.startswith("/") else href

        jobs.append({"company": company, "role_title": title, "link": link})
        if len(jobs) >= limit:
            break

    return jobs


if __name__ == "__main__":
    rows = []
    try:
        rows = scrape_jobs(limit=30)
    except Exception as exc:
        print(f"Warning: could not scrape Indeed ({exc}). Writing empty jobs.csv.")

    write_csv("jobs.csv", ["company", "role_title", "link"], rows)
    print(f"Saved {len(rows)} rows to jobs.csv")
