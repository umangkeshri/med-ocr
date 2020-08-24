import os

import tabula
import camelot
import pandas as pd

class TableExtractor:
    def __init__(self, pdf_path): self.path = pdf_path

    def extract_using_tabula(self):
        dfs = tabula.read_pdf(self.path)
        return ''

    def extract_using_camelot(self):
        return ''

    def process_docs(self):
        return ''
