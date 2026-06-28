import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
import os
from utils.logger import logger

class ExcelReporter:
    def __init__(self):
        os.makedirs("output", exist_ok=True)
        self.wb = openpyxl.Workbook()
        
    def _style_header(self, cell):
        cell.font = Font(bold=True, color="FFFFFF", size=12)
        cell.fill = PatternFill("solid", fgColor="2E86AB")
        cell.alignment = Alignment(horizontal="center")

    def create_report(self, books, stats, rating_summary):
        # Sheet 1 - All Books
        ws1 = self.wb.active
        ws1.title = "All Books"
        headers = ["ID", "Title", "Price (£)", "Rating", "Category", "Scraped At"]
        
        for col, header in enumerate(headers, 1):
            cell = ws1.cell(row=1, column=col, value=header)
            self._style_header(cell)
        
        for row, book in enumerate(books, 2):
            for col, value in enumerate(book, 1):
                ws1.cell(row=row, column=col, value=value)
        
        # Auto fit columns
        for col in range(1, len(headers) + 1):
            ws1.column_dimensions[get_column_letter(col)].width = 25

        # Sheet 2 - Price Analysis
        ws2 = self.wb.create_sheet("Price Analysis")
        price_headers = ["Total Books", "Avg Price (£)", "Min Price (£)", "Max Price (£)"]
        
        for col, header in enumerate(price_headers, 1):
            cell = ws2.cell(row=1, column=col, value=header)
            self._style_header(cell)
        
        for col, value in enumerate(stats, 1):
            ws2.cell(row=2, column=col, value=value)
        
        for col in range(1, 5):
            ws2.column_dimensions[get_column_letter(col)].width = 20

        # Sheet 3 - Rating Summary
        ws3 = self.wb.create_sheet("Rating Summary")
        rating_headers = ["Rating", "Total Books"]
        
        for col, header in enumerate(rating_headers, 1):
            cell = ws3.cell(row=1, column=col, value=header)
            self._style_header(cell)
        
        for row, item in enumerate(rating_summary, 2):
            for col, value in enumerate(item, 1):
                ws3.cell(row=row, column=col, value=value)
        
        for col in range(1, 3):
            ws3.column_dimensions[get_column_letter(col)].width = 20

        # Save
        path = "output/books_report.xlsx"
        self.wb.save(path)
        logger.info(f"Professional Excel report saved: {path}")