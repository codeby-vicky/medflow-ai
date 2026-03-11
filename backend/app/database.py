from pymongo import MongoClient

# MongoDB Atlas connection string
MONGO_URI = "mongodb+srv://dbname:#########@vignesh.or7uklc.mongodb.net/medflow_ai?retryWrites=true&w=majority&appName=Vignesh"

# Connect to MongoDB
client = MongoClient(MONGO_URI)

# Select database
db = client["medflow_ai"]

# Collections
patients_collection = db["patients"]
prescriptions_collection = db["prescriptions"]
billing_collection = db["billing"]
