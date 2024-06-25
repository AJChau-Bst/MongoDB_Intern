import os
import csv
from dotenv import load_dotenv
from pymongo import MongoClient

# Load environment variables from .env file
load_dotenv()

# MongoDB connection URI and database details
MONGODB_URI = os.getenv('MONGODB_URI')
DATABASE_NAME = os.getenv('DATABASE_NAME')
COLLECTION_NAME = os.getenv('COLLECTION_NAME')

# CSV output file name
CSV_OUTPUT_FILE = os.getenv('CSV_OUTPUT_FILE', 'output_data.csv')

# Connect to MongoDB
client = MongoClient(MONGODB_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

# Query MongoDB collection for data
cursor = collection.find({})

# Extract field names from the first document (assuming all documents have the same structure)
field_names = list(cursor[0].keys())

# Open CSV file for writing
with open(CSV_OUTPUT_FILE, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)

    # Write header
    writer.writeheader()

    # Write documents to CSV
    for document in cursor:
        writer.writerow(document)

# Print success message
print(f"Exported MongoDB data from '{COLLECTION_NAME}' collection to '{CSV_OUTPUT_FILE}'.")
