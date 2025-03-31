from PyPDF2 import PdfReader
from .base_loader import BaseLoader

class PDFLoader(BaseLoader):
    def load(self, file_path):
        with open(file_path, "rb") as f:
            reader = PdfReader(f)
            text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
        return text