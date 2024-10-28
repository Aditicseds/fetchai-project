from database import db
from models import HealthData

# Collection name
health_data_collection = db['health_data']

def create_health_data(user_id, heart_rate, blood_pressure):
    health_data = HealthData(user_id, heart_rate, blood_pressure)
    health_data_collection.insert_one(health_data.to_dict())

def get_current_health_data(user_id):
    # Fetch the latest health data for the given user
    return health_data_collection.find_one({"user_id": user_id}, sort=[("timestamp", -1)])

def get_previous_health_data(user_id):
    # Fetch previous health data for the given user
    return list(health_data_collection.find({"user_id": user_id}).sort([("timestamp", -1)]).limit(5))

def get_all_health_data():
    # Fetch all health data
    return list(health_data_collection.find())
