# Email PDF Downloader and Merger

## Description

This Python project automates the process of downloading specific PDF attachments from Gmail and then merging them into
a single PDF file. It's particularly useful for consolidating PDF documents that match a given naming pattern directly
from your email.

## Setup Instructions

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- `pip` (Python package installer)

### Installation Steps

1. **Clone the Repository**
    - Clone this repository to your local machine using `git clone https://github.com/KozlovKA/Bank_Statements`.
    - Navigate to the cloned directory.

2. **Set Up a Virtual Environment (Recommended)**
    - Create a virtual environment: `python3 -m venv venv`
    - Activate the virtual environment:
        - On Windows: `venv\Scripts\activate`
        - On macOS/Linux: `source venv/bin/activate`

3. **Install Required Packages**
    - Install the required Python packages: `pip install -r requirements.txt`

4. **Gmail API Configuration**
    - You need to enable IMAP access in your Gmail settings.
    - Generate and use an app-specific password for Gmail. Follow the instructions provided by
      Google [here](https://support.google.com/accounts/answer/185833?hl=en).

5. **Configure the Script**
    - Open `main.py` in a text editor.
    - Set the `EMAIL_ADDRESS`, `GMAIL_APPLICATION_PASSWORD`, `EMAIL_SUBJECT_NAMING`,`START_DATE`, `END_DATE`
      and `PDF_FILE_PATTERN` variables with your Gmail details and specific PDF naming pattern.

## Running the Code

1. **Execute the Script**
    - Run the script using: `python main.py`
    - The script will connect to Gmail, download the specified PDFs, and merge them into a single file in the specified
      directory.

2. **Check the Output**
    - After running, check the `Bank_Statements/bills` directory for the downloaded PDFs and the merged PDF file.

3. **Deactivate Virtual Environment (Optional)**
    - Once done, you can deactivate the virtual environment: `deactivate`

## Additional Information

- The `utils/email_interaction.py` script is responsible for connecting to Gmail and downloading the PDFs.
- The `utils/pdf_interaction.py` script handles the merging of the downloaded PDFs.
- Ensure that the directory paths and email subject patterns are correctly set according to your requirements.
