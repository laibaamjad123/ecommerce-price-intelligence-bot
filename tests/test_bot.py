import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.books_page import BooksPage

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def books_page(driver):
    return BooksPage(driver)

def test_page_opens(books_page):
    books_page.open(1)
    assert "Books" in books_page.driver.title
    print("✅ Page opened successfully!")

def test_books_found(books_page):
    books_page.open(1)
    titles = books_page.get_titles()
    assert len(titles) == 20
    print(f"✅ {len(titles)} books found!")

def test_prices_found(books_page):
    books_page.open(1)
    prices = books_page.get_prices()
    assert len(prices) == 20
    print(f"✅ {len(prices)} prices found!")

def test_has_next_page(books_page):
    books_page.open(1)
    assert books_page.has_next_page() == True
    print("✅ Next page button found!")

def test_last_page(books_page):
    books_page.open(50)
    assert books_page.has_next_page() == False
    print("✅ Last page confirmed!")