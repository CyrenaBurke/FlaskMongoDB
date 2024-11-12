from pymongo import MongoClient

# Replace with your MongoDB URI
uri = "mongodb://localhost:27017/"  # For local MongoDB
# uri = "mongodb+srv://<username>:<password>@cluster0.mongodb.net/test"  # For MongoDB Atlas

try:
    # Create a MongoClient object
    client = MongoClient(uri)

    # Attempt to connect and test the connection
    client.admin.command('ping')
    print("Successfully connected to MongoDB!")

    # Optionally, list databases to ensure MongoDB is accessible
    databases = client.list_database_names()
    print("Databases:", databases)

except Exception as e:
    print("Error connecting to MongoDB:", e)
