from utils import write_csv


STARTUPS = [
    {"company": "Wealthsimple", "industry": "Fintech"},
    {"company": "Clearco", "industry": "E-commerce financing"},
    {"company": "Koho", "industry": "Fintech"},
    {"company": "BenchSci", "industry": "Healthtech / AI"},
    {"company": "Neo Financial", "industry": "Fintech"},
    {"company": "Ada", "industry": "Customer service AI"},
    {"company": "Float Financial", "industry": "Fintech"},
    {"company": "Borrowell", "industry": "Fintech"},
    {"company": "StackAdapt", "industry": "Adtech"},
    {"company": "Clutch", "industry": "Fintech"},
]


if __name__ == "__main__":
    write_csv("startups.csv", ["company", "industry"], STARTUPS)
    print(f"Saved {len(STARTUPS)} rows to startups.csv")
