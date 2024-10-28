from pymongo import MongoClient

# MongoDB connection settings
MONGO_URI = "mongodb://localhost:27017"
DATABASE_NAME = "uagent_db"

# Create a MongoDB client
client = MongoClient(MONGO_URI)

# Access the database
db = client[DATABASE_NAME]

