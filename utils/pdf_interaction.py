import os
import re

import PyPDF2


def sort_key(filename):
    # Extract the number after 'Izvod br.' from the filename using regular expression
    match = re.search(r'Izvod br\. (\d+)', filename)
    if match:
        return int(match.group(1))
    return 0


def merge_pdfs(directory, output):
    pdf_writer = PyPDF2.PdfFileWriter()

    # List all files in the directory
    files = os.listdir(directory)
    print(files)
    # Filter out all non-PDF files
    # Sort the files based on the numeric part of the filename
    sorted_pdf_files = sorted(files, key=sort_key)
    print(sorted_pdf_files)

    for pdf in sorted_pdf_files:
        try:
            filepath = os.path.join(directory, pdf)
            pdf_reader = PyPDF2.PdfFileReader(filepath)
            for page in range(pdf_reader.getNumPages()):
                pdf_writer.addPage(pdf_reader.getPage(page))
        except Exception as e:
            print(f"Error processing {pdf}: {e}")

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)


if __name__ == '__main__':
    # Directory containing PDFs
    directory = '/Users/kirillkozlov/PycharmProjects/profitero/Bank_Statements/bills/'
    # Output file name
    output = 'merged.pdf'
    merge_pdfs(directory, output)
