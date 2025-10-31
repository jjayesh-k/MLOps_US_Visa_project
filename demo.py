import os

# This should match EXACTLY what's in your system variables
mongo_db_url = os.getenv('MONGODB_URL')  # Notice: MONGODB_URL not MONGO_DB_URL
print(mongo_db_url)