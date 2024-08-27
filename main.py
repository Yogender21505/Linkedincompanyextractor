import mysql.connector
from extract_data import extract_data
from enrich_data import enrich_company_data
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def insert_enriched_data(connection, company_id, enriched_data):
    cursor = connection.cursor()
    query = """
        INSERT INTO enriched_companies (company_id, company_name, company_size, company_industry, company_website)
        VALUES (%s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
        company_name=VALUES(company_name),
        company_size=VALUES(company_size),
        company_industry=VALUES(company_industry),
        company_website=VALUES(company_website)
    """
    cursor.execute(query, (
        company_id,
        enriched_data.get('companyName'),  # Update the keys to match the API response
        enriched_data.get('employeeCount'),  # Assuming 'company_size' corresponds to 'employeeCount'
        enriched_data.get('industry'),  # 'company_industry' corresponds to 'industry'
        enriched_data.get('websiteUrl')  # 'company_website' corresponds to 'websiteUrl'
    ))
    connection.commit()
    cursor.close()

def main():
    connection = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )

    companies = extract_data()
    for company in companies:
        enriched_data = enrich_company_data(company['company_linkedin_url'])
        # print(enriched_data)
        if enriched_data:
            insert_enriched_data(connection, company['company_id'], enriched_data)

    connection.close()
    print("Data enrichment completed.")

if __name__ == "__main__":
    main()
