import os

from utils.email_interaction import download_pdf_attachments
from utils.pdf_interaction import merge_pdfs

EMAIL_ADDRESS = ''
# The link where to get this Password: https://support.google.com/accounts/answer/185833?hl=en
GMAIL_APPLICATION_PASSWORD = ''
EMAIL_SUBJECT_NAMING = ''  # Example: Izvod po dinarskom racunu broj
PDF_FILE_PATTERN = ''  # Example: d+ Izvod br\.\s+\d+-\S+\.PDF
DOWNLOAD_FOLDER = 'bills'
START_DATE = ''  # Example:'1-Jan-2024'
END_DATE = ''  # Example:'31-Jan-2024'


def main():
    # Download PDF attachments
    download_pdf_attachments(EMAIL_ADDRESS, GMAIL_APPLICATION_PASSWORD, DOWNLOAD_FOLDER,
                             EMAIL_SUBJECT_NAMING, PDF_FILE_PATTERN, START_DATE, END_DATE)

    # Correctly setting the directory containing the downloaded PDFs
    # Assuming the script is run from the project root directory
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(project_root)
    directory = os.path.join(project_root, 'Bank_Statements', DOWNLOAD_FOLDER)
    print(directory)
    output_file = os.path.join(directory, 'merged.pdf')
    print(directory)
    # Merge the downloaded PDFs
    merge_pdfs(directory, output_file)
    print(f"PDFs merged into {output_file}")


if __name__ == '__main__':
    main()
