from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger

class BooksPage:
    URL = "https://books.toscrape.com/catalogue/page-{}.html"
    
    TITLES = (By.CSS_SELECTOR, "h3 a")
    PRICES = (By.CSS_SELECTOR, "p.price_color")
    RATINGS = (By.CSS_SELECTOR, "p.star-rating")
    CATEGORIES = (By.CSS_SELECTOR, "ul.nav-list li a")
    NEXT_BTN = (By.CSS_SELECTOR, "li.next a")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def open(self, page=1):
        self.driver.get(self.URL.format(page))
        self.wait.until(EC.presence_of_element_located(self.TITLES))
        logger.info(f"Page {page} opened!")
    
    def get_titles(self):
        return self.driver.find_elements(*self.TITLES)
    
    def get_prices(self):
        return self.driver.find_elements(*self.PRICES)
    
    def get_ratings(self):
        return self.driver.find_elements(*self.RATINGS)
    
    def has_next_page(self):
        try:
            self.driver.find_element(*self.NEXT_BTN)
            return True
        except:
            return False