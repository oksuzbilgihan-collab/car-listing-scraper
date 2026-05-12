# Car Listing Scraper

This is a beginner-friendly web scraping practice project built with Python, BeautifulSoup, and Pandas.

The script reads a saved HTML file, extracts car listing information, and exports the data to an Excel file.

## Extracted Data

- Car brand/title
- Model/trim
- Price
- Listing link

## Technologies Used

- Python
- BeautifulSoup
- Pandas
- OpenPyXL

## Project Files

- `scraper.py` → Main Python script
- `sample_truecar.html` → Saved sample HTML file used for parsing
- `car_listing.xlsx` → Output Excel file

## Important Note

During testing, the live website returned `403/captcha` responses.  
Because of this, the project uses a saved HTML file instead of sending repeated live requests.

This project helped me practice:

- Reading local HTML files
- Parsing HTML with BeautifulSoup
- Using `.find()`, `.find_all()`, `.text`, and `.get("href")`
- Cleaning extracted text
- Storing data in a list
- Creating a Pandas DataFrame
- Exporting data to Excel

## Output

The final output is an Excel file containing car listing data.