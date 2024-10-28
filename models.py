from datetime import datetime

class HealthData:
    def __init__(self, user_id, heart_rate, blood_pressure):
        self.user_id = user_id
        self.heart_rate = heart_rate
        self.blood_pressure = blood_pressure
        self.timestamp = datetime.now()

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "heart_rate": self.heart_rate,
            "blood_pressure": self.blood_pressure,
            "timestamp": self.timestamp
        }
