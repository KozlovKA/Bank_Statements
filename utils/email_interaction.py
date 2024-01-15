import imaplib
import os
import re
import email
from email.header import decode_header
from concurrent.futures import ThreadPoolExecutor


def download_attachment(part, download_folder, pdf_pattern):
    """
    Download an attachment from an email part to a specified folder.

    :param part: An email message part (a part of the email).
    :param download_folder: The folder where the attachment will be downloaded.
    :param pdf_pattern: The PDF file naming pattern to filter attachments by.
    """
    file_name = part.get_filename()
    if file_name:
        file_name = decode_header(file_name)[0][0]
        if isinstance(file_name, bytes):
            file_name = file_name.decode()

        # Remove newline characters from the file name
        file_name = file_name.replace('\r', '').replace('\n', '')

        if "pdf" in file_name.lower() and re.match(pdf_pattern, file_name, re.IGNORECASE):
            # Use the absolute path to the download folder
            target_folder = download_folder

            # Ensure the target directory exists
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            file_path = os.path.join(target_folder, file_name)
            try:
                with open(file_path, 'wb') as file:
                    file.write(part.get_payload(decode=True))
                print(f'Successfully downloaded: {file_name}')
            except Exception as e:
                print(f'Error downloading {file_name}: {e}')
        else:
            print(f'Skipping non-matching file: {file_name}')
    else:
        print('No filename found for a part, skipping...')


def download_pdf_attachments(gmail_user, gmail_password, download_folder, email_subject_naming, pdf_pattern,
                             start_date, end_date,
                             max_emails=40000,
                             ):
    """
    Connects to Gmail via IMAP and downloads PDF attachments from emails.

    This function fetches emails from the inbox, filters for PDF attachments
    matching a specific naming pattern, and downloads them to a specified folder.

    :param gmail_user: The Gmail email address.
    :param gmail_password: The Gmail password or app password.
    :param download_folder: The folder path where PDFs will be saved.
    :param email_subject_naming: The subject naming pattern to filter emails by.
    :param pdf_pattern: The PDF file naming pattern to filter attachments by.
    :param start_date: The start date for filtering emails (format: '1-Jan-2020').
    :param end_date: The end date for filtering emails (format: '31-Dec-2020').
    :param max_emails: The maximum number of emails to process.
    """
    print("Connecting to Gmail...")
    host = 'imap.gmail.com'
    mail = imaplib.IMAP4_SSL(host)
    mail.login(gmail_user, gmail_password)
    mail.select('inbox')

    # Modify the search criteria to look for emails with the specific subject start
    # Modify the search criteria with date range
    print(
        f"Fetching email messages with subject starting: '{email_subject_naming}' between {start_date} and {end_date}")
    query = '(SUBJECT "{}" SINCE "{}" BEFORE "{}")'.format(email_subject_naming, start_date, end_date)
    typ, messages = mail.search(None, query)
    messages = messages[0].split()[:max_emails]
    print(f"Number of messages to process: {len(messages)}")

    with ThreadPoolExecutor(max_workers=10) as executor:
        for num in messages:
            print(f"Processing message {num}...")
            typ, data = mail.fetch(num, '(RFC822)')
            raw_email = data[0][1]
            email_message = email.message_from_bytes(raw_email)

            for part in email_message.walk():
                if part.get_content_maintype() == 'multipart' or part.get('Content-Disposition') is None:
                    continue
                executor.submit(download_attachment, part, download_folder, pdf_pattern)

    print("Closing the connection to Gmail...")
    mail.close()
    mail.logout()
    print("Process completed.")
