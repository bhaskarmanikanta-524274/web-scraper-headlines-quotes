"""
Web Scraper for Headlines & Quotes
InternCircle Python Programming Task 5

Uses requests and BeautifulSoup to collect headlines or quotes from
public pages. Always follow a website's terms and robots.txt.
"""

import json
from datetime import datetime
from pathlib import Path

import requests
from bs4 import BeautifulSoup

OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

# Public demo pages intended for practice.
SOURCES = {
    "quotes": "https://quotes.toscrape.com/",
    "books": "https://books.toscrape.com/",
}


def fetch_page(url):
    """Download a page and return parsed HTML."""
    headers = {"User-Agent": "StudentPracticeScraper/1.0 (educational project)"}
    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")


def scrape_quotes():
    """Extract quotes and authors from the Quotes to Scrape practice website."""
    soup = fetch_page(SOURCES["quotes"])
    results = []
    for item in soup.select("div.quote"):
        quote = item.select_one("span.text")
        author = item.select_one("small.author")
        if quote:
            results.append({
                "quote": quote.get_text(" ", strip=True),
                "author": author.get_text(" ", strip=True) if author else "Unknown",
            })
    return results


def scrape_book_titles():
    """Extract titles from the Books to Scrape practice website."""
    soup = fetch_page(SOURCES["books"])
    results = []
    for item in soup.select("article.product_pod h3 a"):
        title = item.get("title") or item.get_text(" ", strip=True)
        results.append({"title": title})
    return results


def save_results(results, filename, format_choice):
    """Save scraped results as JSON or plain text."""
    output_path = OUTPUT_DIR / filename
    if format_choice == "1":
        with output_path.open("w", encoding="utf-8") as file:
            json.dump(results, file, indent=2, ensure_ascii=False)
    else:
        with output_path.open("w", encoding="utf-8") as file:
            for index, item in enumerate(results, start=1):
                if "quote" in item:
                    file.write(f"{index}. {item['quote']} — {item['author']}\n")
                else:
                    file.write(f"{index}. {item['title']}\n")
    return output_path


def main():
    print("=" * 44)
    print("      WEB SCRAPER: QUOTES & TITLES")
    print("=" * 44)
    print("1. Scrape quotes and authors")
    print("2. Scrape book titles")
    choice = input("Choose a scraper (1-2): ").strip()

    if choice == "1":
        label = "quotes"
        filename_base = "quotes"
        scrape_function = scrape_quotes
    elif choice == "2":
        label = "book titles"
        filename_base = "book_titles"
        scrape_function = scrape_book_titles
    else:
        print("Invalid choice.")
        return

    print("\nOutput format:")
    print("1. JSON")
    print("2. Plain text")
    format_choice = input("Choose format (1-2): ").strip()
    if format_choice not in {"1", "2"}:
        print("Invalid format.")
        return

    try:
        results = scrape_function()
        if not results:
            print("No results found. The website layout may have changed.")
            return
        extension = "json" if format_choice == "1" else "txt"
        output_path = save_results(
            results, f"{filename_base}_{datetime.now():%Y%m%d_%H%M%S}.{extension}",
            format_choice
        )
        print(f"\nSuccessfully scraped {len(results)} {label}.")
        print(f"Saved results to: {output_path}")
    except requests.RequestException as error:
        print(f"Network/request error: {error}")
    except OSError as error:
        print(f"File error: {error}")


if __name__ == "__main__":
    main()
