# Task 5 - Web Data Extraction & Analysis

**Internship:** Data Analytics Virtual Internship
**Organization:** CodSoft
**Intern Name:** Suman D H
**Internship ID:** BY26RY233444
**Internship Duration:** 25 August 2026 to 25 September 2026
**Date:** 25/08/2026

## Objective
Collect data from a publicly available website using Python (BeautifulSoup),
extract structured product information, clean/organize it into a dataset,
perform exploratory analysis, and export the results.

## Data source
[books.toscrape.com](https://books.toscrape.com) - a public sandbox website
built specifically for practicing web scraping ("We love being scraped!").

## Files in this folder
| File | Description |
|---|---|
| `source_code.py` | Contains both the scraper (`scrape_books`) and the analysis (`analyze_books`) logic. |
| `books_scraped.csv` | Real data collected from books.toscrape.com (title, price, availability, category, product URL for 40 books). |
| `books_cleaned.csv` | Output: cleaned/organized dataset after processing. |
| `output.png` | Output: 4-panel analysis chart (price distribution, avg price by category, title length vs price, stock availability). |
| `requirements.txt` | Python dependencies required to run the script. |

## What the script does
**Part A - Scraper:** Uses `requests` + `BeautifulSoup` to fetch book
listing pages from books.toscrape.com and extract title, price, and
availability for each book (run with `python source_code.py --scrape`
on a machine with internet access to refresh `books_scraped.csv`).

**Part B - Analysis:** Loads `books_scraped.csv`, cleans it (numeric price
conversion, duplicate removal), and analyzes:
- Price distribution across all books
- Average price by category
- Relationship between book title length and price
- Stock availability breakdown

## How to run
```bash
pip install -r requirements.txt

# Re-scrape fresh data (requires internet access):
python source_code.py --scrape

# Just run the analysis on the included dataset:
python source_code.py
```

## Bonus
The scraping step is already automated in `scrape_books()` and results are
exported to CSV, matching the bonus objective of automating the scrape and
exporting results.

---
*Submitted as part of the CodSoft Data Analytics Internship.*
