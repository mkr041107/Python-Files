import csv
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
import logging
import time

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to perform geocoding with retries
def geocode_with_retry(address, max_retries=5, initial_delay=1):
    for attempt in range(max_retries):
        try:
            geolocator = Nominatim(user_agent="my_app", timeout=None)
            location = geolocator.geocode(address)
            
            if location:
                return location.latitude, location.longitude
            else:
                logging.warning(f"No coordinates found for {address}")
                return None, None
        
        except GeocoderTimedOut:
            if attempt == max_retries - 1:
                logging.error(f"Max retries reached for {address}. No coordinates found.")
                return None, None
            else:
                delay = initial_delay * (2 ** attempt)  # Exponential backoff
                logging.info(f"Timeout occurred for {address}. Retrying in {delay:.2f} seconds...")
                time.sleep(delay)
        
        except GeocoderServiceError as e:
            logging.error(f"Geocoding service error for {address}. Error: {str(e)}")
            return None, None
        
        except Exception as e:
            logging.error(f"Unexpected error occurred for {address}. Error: {str(e)}")
            return None, None

# Read the CSV file
csvFile = "C:\\Users\\334706\\Downloads\\addresses.csv"

results = []
with open(csvFile, 'r', newline='') as file:
    csv_reader = csv.reader(file)
    
    # Skip the header row
    next(csv_reader)
    
    # Process each row
    for row in csv_reader:
        city = row[0]
        address = f"{row[1]} {row[2]}, {row[3]}"
        state = row[2]
        zip_code = row[3]

        logging.info(f"Processing: {city}, {address}")

        latitude, longitude = geocode_with_retry(address)

        if latitude is not None and longitude is not None:
            results.append((city, address, state, zip_code, latitude, longitude))

# Write results to a new CSV file
output_file = "C:\\Users\\334706\\Downloads\\coordinatessssss.csv"

with open(output_file, 'w', newline='') as output_csv:
    writer = csv.writer(output_csv)
    writer.writerow(["City", "Address", "State", "Zip", "Latitude", "Longitude"])
    writer.writerows(results)
logging.info(f"Processing complete. Results written to {output_file}")