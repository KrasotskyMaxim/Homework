"""contains functions for converting these news files to a pdf file"""

from fpdf import FPDF
from rss_package import log


class PDF(FPDF):

    """Class for creating a pdf file and adding news to it"""

    def __init__(self, news, path, channel_title):
        super().__init__()
        self.news = news
        self.path = path
        self.channel_title = channel_title

    @log.log_decorator
    def create_pdf(self):
        """adds a page to the pdf file with font and news"""
        self.add_page()
        self.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
        self.set_font('DejaVu', '', 12)
        self.set_auto_page_break(auto=True, margin=15)
        self.cell(0, 5, self.channel_title, align="C", border=True, ln=True)
        for item in self.news:
            self.multi_cell(0, 5, f"Title: {item['title']}", border=True)
            self.ln()
            self.cell(0, 10, f"PubDate: {item['pubdate']}")
            self.ln()
            self.multi_cell(0, 5, f"Description: {item['description']}")
            self.ln()
            self.cell(0, 5, "Link (press)", link=item['link'], ln=True)
            self.cell(0, 10, "Image (press)", link=item['image'], ln=True)

        self.output(self.path)
        print("\nSuccessful write to pdf!\n")
        return True
