from botcity.document_processing import *
import os
from pathlib import Path
import pandas as pd

current_dir, _DUMMY = os.path.split(os.path.abspath(__file__))

def read_pdf(file_path):
    reader = PDFReader()
    parser = reader.read_file(file_path)

    _date = parser.get_first_entry("Date:")
    date = parser.read(_date, 1.333333, -2.444444, 3.222222, 4.222222)
    print("Date: ", date)

    _bill_to = parser.get_first_entry("Bill to:")
    bill_to = parser.read(_bill_to, 1.170213, -2.555556, 3.170213, 4.888889)
    print("Bill To: ", bill_to)

    _contact = parser.get_first_entry("Contact:")
    contact = parser.read(_contact, 1.242424, -1.444444, 3.833333, 3.222222)
    print("Contact: ", contact)
    
    _balance_due = parser.get_first_entry("Balance due:")
    balance_due = parser.read(_balance_due, 1.091603, -2.272727, 1.351145, 4.272727)
    print("Balance due: ", balance_due)
    
    extracted_data = [date, bill_to, contact, balance_due]

    return extracted_data

if __name__ == '__main__':

    docs_directory = os.path.join(current_dir, "docs")
    pdf_files = Path(docs_directory).glob('*.pdf')
    
    files_data = []

    for pdf_file in pdf_files:
        pdf_directory, pdf_name = os.path.split(pdf_file)
        print(pdf_name, '\n')
        pdf_data = read_pdf(pdf_file)
        print('\n')
        files_data.append(pdf_data)

    df = pd.DataFrame(files_data, columns=['date', 'bill_to', 'contact', 'balance_due'])
    df.to_csv(os.path.join(docs_directory, "pdf_data.csv"), sep=',', index=False)
