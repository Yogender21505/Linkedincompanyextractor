import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def extract_data():
    connection = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )

    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT company_id, company_linkedin_url FROM companies")
    companies = cursor.fetchall()

    cursor.close()
    connection.close()
    return companies

if __name__ == "__main__":
    companies = extract_data()
    # print(companies)
