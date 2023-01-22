import os
from PyPDF2 import PdfReader

def parse_plain_text(text):
    return text.split(2*os.linesep)

def parse_pdf(path_to_file):
    lob = []
    reader = PdfReader(path_to_file)
    for p in len(reader.pages):
        page = reader.pages[p]
        lob.append(page.extract_text())
    return lob