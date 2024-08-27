import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def enrich_company_data(company_link):
    url = "https://linkedin-bulk-data-scraper.p.rapidapi.com/company"
    payload = {"link": company_link}
    headers = {
        "x-rapidapi-key": os.getenv('RAPIDAPI_KEY'),
        "x-rapidapi-host": "linkedin-bulk-data-scraper.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()
        # print(data)
        # Filter out unwanted keys
        unwanted_keys = ['affiliatedOrganizationsByEmployees', 'affiliatedOrganizationsByShowcases', 'locations', 'similarOrganizations']
        enriched_data = {k: v for k, v in data.get('data', {}).items() if not any(substring in k for substring in unwanted_keys)}

        return enriched_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

if __name__ == "__main__":
    sample_link = "https://www.linkedin.com/company/huzzle-app/"
    enriched_data = enrich_company_data(sample_link)
    if enriched_data:
        print()
    else:
        print("Failed to retrieve or process the data.")
