# 🤖 E-Commerce Price Intelligence Bot

A professional-grade Python automation bot that automatically scrapes 1000+ books from 50 pages, stores data in SQLite database, and generates a professional 3-sheet Excel report.

## 🛠️ Tools & Technologies
- Python 3.14
- Selenium + WebDriver Manager
- SQLite Database
- openpyxl (Professional Excel Reports)
- Logging (Activity Tracking)
- Pytest (Automated Testing)
- Page Object Model (POM Architecture)

## ✨ Features
- ✅ Scrapes 1000 books from 50 pages automatically
- ✅ Stores all data in SQL database with timestamps
- ✅ Generates 3-sheet professional Excel report
- ✅ Full logging with timestamps
- ✅ Crash-proof with Exception Handling
- ✅ Professional POM architecture
- ✅ Automated test suite with Pytest

## 📁 Project Structure
ecommerce_bot/
├── pages/          # Page Object Model
├── utils/          # Logger
├── database/       # SQLite Handler
├── reports/        # Excel Reporter
├── tests/          # Pytest Test Suite
├── output/         # Generated Reports
├── logs/           # Activity Logs
└── main.py         # Main Bot

## 📊 Output
- All Books Sheet — 1000 books with ID, Title, Price, Rating, Category, Timestamp
- Price Analysis Sheet — Total, Average, Min, Max prices
- Rating Summary Sheet — Books count by rating

## ▶️ How to Run
pip install -r requirements.txt
python main.py

## 🔗 Connect
github.com/laibaamjad123
