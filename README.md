# Flipkart E-commerce Product Scraper

A Python-based web scraping project for extracting e-commerce product information using Selenium.

## Features

✓ Selenium automation

✓ Product URL extraction
✓ Pagination
✓ Dynamic content handling
✓ Product information extraction
✓ Excel/CSV export
✓ Data cleaning
✓ Error handling

## Technologies

- Python
- Selenium
- Pandas
- XPath
- OpenPyXL

## Data Fields

The scraper extracts:

- Product Name
- Brand
- Price
- Rating
- Product URL

## Project Workflow

Flipkart Search Page
↓
Pagination
↓
Product URLs
↓
Product Pages
↓
Data Extraction
↓
Data Cleaning
↓
Duplicate Removal
↓
Pandas DataFrame
↓
Excel

## Installation

Create a virtual environment:

python -m venv .venv

Activate:

Windows:

.venv\Scripts\activate

Install packages:

pip install -r requirements.txt

## Run

python FlipKart_Project.py

## Output

The scraped data is saved as:

data/[Flipkart_Data_Extract_Final.xlsx](https://github.com/TkdnGit/flipkart-ecommerce-scraper/blob/main/Flipkart_Data_Extract_Final.xlsx "Flipkart_Data_Extract_Final.xlsx")

## Error Handling

The scraper uses try/except blocks so individual extraction failures do not stop the entire scraping process.

## Disclaimer

This project is intended for educational and portfolio purposes. Users should respect the target website's terms of service and applicable laws.
