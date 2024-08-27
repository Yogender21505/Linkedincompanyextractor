# LinkedIn Company Data Enrichment

## Description

This project enriches company data from LinkedIn using the LinkedIn Bulk Data Scraper API. It extracts basic company information from a MySQL database, fetches additional details from the API, and stores the enriched data back into the database.

## Features

- Extracts company data (ID and LinkedIn URL) from a MySQL database.
- Enriches company data using the LinkedIn Bulk Data Scraper API.
- Inserts or updates enriched company data in the database.
- Handles errors and logging for API requests.

## Installation

### Prerequisites

- Python 3
- MySQL( MySQL workbench and server)
- Pip (for Python package management)
- `.env` file for environment variables
- LinkedIn Bulk Data Scraper API
### Screenshots of Database(company_data)
## companies
![image](https://github.com/user-attachments/assets/c3cb7af3-554f-4aa4-8df9-8c67628295f4)
## enrich_data
![image](https://github.com/user-attachments/assets/d3f4e030-dcfe-4e2d-9389-fd8fb8314afd)

### Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Yogender21505/Linkedincompanyextractor.git
   cd your-repository
   ```
2. **Create a Virtual Environment (optional but recommended):**
   ```bash
   python -m venv venv
   ```
3. **Activate the Virtual Environment:**
    ```bash
    venv\Scripts\activate
    ```
4. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
5. **Set Up Environment Variables:**
   ### Create a .env file in the root directory of the project with the following content:##
    ```bash
    DB_HOST=localhost
    DB_USER=root
    DB_PASSWORD=password
    DB_NAME=mydatabase
    RAPIDAPI_KEY=your_rapidapi_key
    ```
6. **Database Setup:**
   Ensure your MySQL database has the required tables. The companies table should have columns company_id and company_linkedin_url, and the enriched_companies table should have columns for company_id, company_name, company_size, company_industry, and company_website.
7. **Usage***
    #### Run the main script to start the data enrichment process:
      ```bash
    python main.py
      ```
    #### Extract Data: Fetches company data from the MySQL database.
    ```bash
    python extract_data.py
    ```
    #### Enrich Data: Fetches additional details from the LinkedIn API.
    ```bash
    python enrich_data.py
    ```
9. **How It Works**
Extraction: The extract_data.py script connects to the MySQL database, retrieves the list of companies with their LinkedIn URLs, and returns it as a list of dictionaries.
Enrichment: The enrich_data.py script sends a request to the LinkedIn Bulk Data Scraper API with a company’s LinkedIn URL, processes the response to filter out unwanted data, and returns the enriched data.
Integration: The main.py script coordinates the process by extracting data, enriching it, and inserting or updating it in the MySQL database.

10. **Testing**
  To test the functionality, ensure your database is properly set up and run the following commands to test data extraction and enrichment separately:

  ```bash
  python extract_data.py
  python enrich_data.py
  ```
