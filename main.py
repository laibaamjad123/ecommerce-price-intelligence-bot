from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.books_page import BooksPage
from database.db_handler import DatabaseHandler
from reports.excel_reporter import ExcelReporter
from utils.logger import logger

def clean_price(price_text):
    return float(price_text.replace("£", "").strip())

def main():
    logger.info("🚀 E-Commerce Price Intelligence Bot Started!")
    
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    
    db = DatabaseHandler()
    page = BooksPage(driver)
    
    total_books = 0
    current_page = 1
    
    try:
        while True:
            logger.info(f"Scraping page {current_page}...")
            page.open(current_page)
            
            titles = page.get_titles()
            prices = page.get_prices()
            ratings = page.get_ratings()
            
            for title, price, rating in zip(titles, prices, ratings):
                try:
                    db.insert_book(
                        title=title.get_attribute("title"),
                        price=clean_price(price.text),
                        rating=rating.get_attribute("class").replace("star-rating ", ""),
                        category="Books"
                    )
                    total_books += 1
                except Exception as e:
                    logger.error(f"Error inserting book: {e}")
                    continue
            
            logger.info(f"Page {current_page} done — {len(titles)} books scraped!")
            
            if page.has_next_page():
                current_page += 1
            else:
                logger.info("Last page reached!")
                break
        
        logger.info(f"✅ Total books scraped: {total_books}")
        
        logger.info("Generating Excel report...")
        books = db.get_all_books()
        stats = db.get_price_stats()
        rating_summary = db.get_rating_summary()
        
        reporter = ExcelReporter()
        reporter.create_report(books, stats, rating_summary)
        
        logger.info("🎉 Bot finished successfully!")
        logger.info(f"📊 Total books: {total_books}")
        logger.info(f"💰 Average price: £{stats[1]}")
        logger.info(f"📁 Report saved to: output/books_report.xlsx")

    except Exception as e:
        logger.error(f"Bot crashed: {e}")

    finally:
        driver.quit()
        db.close()
        logger.info("Browser and database closed!")

if __name__ == "__main__":
    main()