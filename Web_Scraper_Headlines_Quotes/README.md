# Web Scraper for Headlines & Quotes

InternCircle Python Programming Task 5.

## Features
- Scrapes quotes and authors from `quotes.toscrape.com`
- Scrapes book titles from `books.toscrape.com`
- Uses HTTP requests and BeautifulSoup HTML selectors
- Saves output as JSON or plain text
- Handles network and file errors
- Writes results into an automatically created `output` folder

## Requirements
- Python 3.x
- `requests`
- `beautifulsoup4`

## Install dependencies
```bash
python -m pip install -r requirements.txt
```

## Run
```bash
python web_scraper.py
```

Choose a scraper, then choose JSON or plain text output.

## Responsible Use
This is an educational demo using practice websites intended for scraping exercises. Check website terms and robots.txt before scraping any site. Use reasonable request rates and do not collect private or restricted data.
