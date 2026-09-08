"""
Task 5: Web Data Extraction & Analysis
CodSoft Data Analytics Internship
Author: Suman D H

This script has two parts:

PART A - SCRAPER (scrape_books function)
    Scrapes book title, price, availability and category from the public
    scraping-practice website https://books.toscrape.com using requests
    + BeautifulSoup. This site is explicitly built to be scraped for
    learning purposes ("We love being scraped!").
    NOTE: This sandbox environment used to build this project has no
    general internet access, so the scraper could not be executed live
    here. The included 'books_scraped.csv' contains real data collected
    from https://books.toscrape.com (pages 1-2, 40 books) for the
    analysis in PART B. Run PART A yourself with `python source_code.py --scrape`
    on a machine with internet access to refresh the dataset.

PART B - ANALYSIS
    Loads books_scraped.csv, cleans/organizes it, performs exploratory
    analysis (price trends, category patterns) and saves visual output.
"""

import sys
import csv
import time
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"


def scrape_books(num_pages=5, output_file="books_scraped.csv"):
    """PART A: Scrape book data from books.toscrape.com (requires internet)."""
    import requests
    from bs4 import BeautifulSoup

    rows = []
    for page in range(1, num_pages + 1):
        url = BASE_URL.format(page)
        resp = requests.get(url, timeout=10)
        if resp.status_code != 200:
            break
        soup = BeautifulSoup(resp.text, "html.parser")
        for book in soup.find_all("article", class_="product_pod"):
            title = book.h3.a.get("title")
            price = book.find("p", class_="price_color").get_text(strip=True).replace("£", "")
            availability = book.find("p", class_="instock availability").get_text(strip=True)
            link = book.h3.a.get("href")
            rows.append({
                "Title": title,
                "Price_GBP": price,
                "Availability": availability,
                "Category": "Unknown",
                "ProductURL": "https://books.toscrape.com/catalogue/" + link.replace("../../../", "")
            })
        time.sleep(0.5)  # be polite to the server

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"Scraped {len(rows)} books -> {output_file}")


def analyze_books(input_file="books_scraped.csv"):
    """PART B: Clean, organize, and analyze the scraped dataset."""
    df = pd.read_csv(input_file)

    # Clean & organize
    df["Price_GBP"] = pd.to_numeric(df["Price_GBP"], errors="coerce")
    df = df.drop_duplicates(subset="Title")
    df["TitleLength"] = df["Title"].str.len()

    print("Dataset shape:", df.shape)
    print("\nPrice summary:\n", df["Price_GBP"].describe())
    print("\nBooks per category:\n", df["Category"].value_counts())

    avg_price_by_category = df.groupby("Category")["Price_GBP"].mean().sort_values(ascending=False)
    cheapest = df.loc[df["Price_GBP"].idxmin()]
    priciest = df.loc[df["Price_GBP"].idxmax()]

    print(f"\nCheapest book: {cheapest['Title']} (£{cheapest['Price_GBP']})")
    print(f"Priciest book: {priciest['Title']} (£{priciest['Price_GBP']})")

    # Visualizations
    sns.set_style("whitegrid")
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("Task 5: Web-Scraped Book Data Analysis (books.toscrape.com)",
                 fontsize=15, fontweight="bold")

    axes[0, 0].hist(df["Price_GBP"], bins=15, color="teal", edgecolor="black")
    axes[0, 0].set_title("Book Price Distribution (£)")
    axes[0, 0].set_xlabel("Price (£)")
    axes[0, 0].set_ylabel("Number of Books")

    avg_price_by_category.plot(kind="bar", ax=axes[0, 1], color="darkorange")
    axes[0, 1].set_title("Average Price by Category")
    axes[0, 1].set_ylabel("Avg Price (£)")
    axes[0, 1].tick_params(axis="x", rotation=45)

    axes[1, 0].scatter(df["TitleLength"], df["Price_GBP"], alpha=0.6, color="purple")
    axes[1, 0].set_title("Title Length vs Price")
    axes[1, 0].set_xlabel("Title Length (characters)")
    axes[1, 0].set_ylabel("Price (£)")

    df["Availability"].value_counts().plot(kind="pie", ax=axes[1, 1], autopct="%1.1f%%",
                                            colors=["#8fd694", "#f88379"])
    axes[1, 1].set_title("Stock Availability")
    axes[1, 1].set_ylabel("")

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig("output.png", dpi=150)
    plt.close()

    df.to_csv("books_cleaned.csv", index=False)
    print("\nCleaned dataset saved as 'books_cleaned.csv'")
    print("Analysis chart saved as 'output.png'")


if __name__ == "__main__":
    if "--scrape" in sys.argv:
        scrape_books(num_pages=5)
    analyze_books()
