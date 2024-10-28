# import requests
# import time
# from flask_cors import CORS
# from uagents import Agent
# from flask import Flask, request, jsonify
# from flask_socketio import SocketIO
# import threading
# import winsound 

# # Initialize Flask app and SocketIO for handling web requests and real-time events
# app = Flask(__name__)
# CORS(app)  # Enable CORS for all routes
# socketio = SocketIO(app)

# # Configuration for the Node.js health data server
# node_js_server = "http://localhost:3000/health"  # URL for fetching health data

# # In-memory storage for health data
# health_data_store = []  # This will hold health data records

# # Function to continuously monitor health data from the server
# def monitor_health_data(agent):
#     while True:
#         try:
#             # Send a GET request to fetch health data from the server
#             response = requests.get(node_js_server)
#             if response.status_code == 200:
#                 # If response is successful, parse the JSON data
#                 health_data = response.json()

#                 # Check if all necessary keys are present in the data
#                 if all(key in health_data for key in ['heartRate', 'pulse', 'temperature', 'bloodPressure', 'bloodSugar']):
#                     print(f"Received health data: {health_data}")
#                     # Pass the health data to the agent for processing
#                     agent.process_health_data(health_data)

#                     # Save the health data to the in-memory store
#                     health_data_store.append(health_data)

#                 else:
#                     print("Invalid data structure received")

#             else:
#                 # Print an error message if the response status is not 200
#                 print(f"Error fetching data: {response.status_code}")

#         except Exception as e:
#             # Print any exceptions that occur during the request
#             print(f"Error fetching data: {e}")

#         time.sleep(6)  # Wait for 10 seconds before checking again

# # Custom Agent class to handle and process health data
# class HealthAgent(Agent):
#     def process_health_data(self, health_data):
#         # Check for emergency situations based on health parameters
#         if (health_data.get('heartRate', 0) > 100 or 
#             float(health_data.get('temperature', 0)) > 100.4 or
#             health_data.get('bloodPressure', {}).get('systolic', 0) > 140 or
#             health_data.get('bloodPressure', {}).get('diastolic', 0) > 90 or
#             health_data.get('bloodSugar', 0) > 180):
            
#             print("Emergency situation detected!")  # Print emergency alert
#             # Emit a real-time event using SocketIO
#             print("Emergency situation detected!")  # Print emergency alert
#             winsound.Beep(1000, 1000)  # Beep sound with frequency 1000 Hz for 1 second
#             # Emit a real-time event using SocketIO
#             socketio.emit('emergencyAlert', {'message': 'Emergency situation detected!'})

#         # Generate health advice based on the current health data
#         diet_plan, exercise_plan = self.generate_health_advice(health_data)
#         print(f"Advice: {diet_plan}")  # Print dietary advice
#         print(f"Exercise Suggestion: {exercise_plan}")  # Print exercise advice

#     def generate_health_advice(self, health_data):
#         # Default advice if no critical health data is detected
#         diet_plan = "Eat more vegetables and fruits."
#         exercise_plan = "Consider yoga or light walking."

#         # Customize advice based on specific health conditions
#         if health_data.get('heartRate', 0) > 90:
#             diet_plan = "Reduce sugar intake."
#             exercise_plan = "Consider doing meditation."
#         if float(health_data.get('temperature', 0)) > 99.5:
#             diet_plan = "Stay hydrated and rest."
#         if health_data.get('bloodPressure', {}).get('systolic', 0) > 130:
#             exercise_plan = "Avoid intense exercises and focus on relaxation techniques."

#         return diet_plan, exercise_plan

# # Route to retrieve the most recent health data from in-memory storage
# @app.route('/api/uagent/previous-data', methods=['GET'])
# def get_previous_data():
#     if health_data_store:
#         health_data = health_data_store[-1]  # Retrieve the most recent health data
#         response = {
#             "heartRate": health_data['heartRate'],
#             "pulse": health_data['pulse'],
#             "temperature": health_data['temperature'],
#             "bloodPressure": health_data['bloodPressure'],
#             "bloodSugar": health_data['bloodSugar'],
#             "timestamp": health_data.get('timestamp', 'N/A')  # Assuming you have a timestamp field
#         }
#     else:
#         response = {"response": "No previous data available."}
#     return jsonify(response)

# @app.route('/')
# def home():
#     return "Welcome to the Health Monitoring API!"

# # Route to retrieve current health data from in-memory storage
# @app.route('/api/uagent/current-data', methods=['GET'])
# def get_current_data():
#     if health_data_store:
#         health_data = health_data_store[-1]  # Retrieve the most recent health data
#         response = {
#             "heartRate": health_data['heartRate'],
#             "pulse": health_data['pulse'],
#             "temperature": health_data['temperature'],
#             "bloodPressure": health_data['bloodPressure'],
#             "bloodSugar": health_data['bloodSugar'],
#             "timestamp": health_data.get('timestamp', 'N/A')  # Assuming you have a timestamp field
#         }
#     else:
#         response = {"response": "No current data available."}
#     return jsonify(response)

# # Route to respond to chat queries
# @app.route('/api/chatbot/query', methods=['POST'])
# def handle_query():
#     user_query = request.json.get('query')
    
#     # Check for specific commands
#     if user_query.lower() == 'latest health data':
#         if health_data_store:
#             latest_health_data = health_data_store[-1]  # Get the latest data
#             return jsonify(latest_health_data)
#         else:
#             return jsonify({"response": "No health data available."})
    
#     elif user_query.lower() == 'previous data':
#         if len(health_data_store) > 1:
#             previous_health_data = health_data_store[-2]  # Get the second most recent data
#             return jsonify(previous_health_data)
#         else:
#             return jsonify({"response": "No previous data available."})

#     # Provide a generic response for unrecognized queries
#     return jsonify({"response": f"You asked: {user_query}. I don't have specific information for that."})

# # Start the health monitoring function in a separate thread
# # Initialize the HealthAgent instance
# agent = HealthAgent()

# # Start the health monitoring function in a separate thread so it runs continuously
# thread = threading.Thread(target=monitor_health_data, args=(agent,))
# thread.start()

# # Run the Flask app using SocketIO, listening on port 5000 with debug mode enabled
# if __name__ == '__main__':
#     try:
#         socketio.run(app, debug=True, port=5000)
#     except Exception as e:
#         print(f"Error starting Flask server: {e}")



# import requests
# import time
# from flask_cors import CORS
# from uagents import Agent  # Ensure you have the correct uagents package installed
# from flask import Flask, request, jsonify
# from flask_socketio import SocketIO
# import threading
# import winsound

# # Initialize Flask app and SocketIO for handling web requests and real-time events
# app = Flask(__name__)
# CORS(app)  # Enable CORS for all routes
# socketio = SocketIO(app)

# # Configuration for the Node.js health data server
# node_js_server = "http://localhost:3000/health"  # URL for fetching health data

# # In-memory storage for health data
# health_data_store = []  # This will hold health data records

# # Function to continuously monitor health data from the server
# def monitor_health_data(agent):
#     while True:
#         try:
#             # Send a GET request to fetch health data from the server
#             response = requests.get(node_js_server)
#             if response.status_code == 200:
#                 # If response is successful, parse the JSON data
#                 health_data = response.json()

#                 # Check if all necessary keys are present in the data
#                 if all(key in health_data for key in ['heartRate', 'pulse', 'temperature', 'bloodPressure', 'bloodSugar']):
#                     print(f"Received health data: {health_data}")
#                     # Pass the health data to the agent for processing
#                     agent.process_health_data(health_data)

#                     # Save the health data to the in-memory store
#                     health_data_store.append(health_data)

#                 else:
#                     print("Invalid data structure received")

#             else:
#                 print(f"Error fetching data: {response.status_code}")

#         except Exception as e:
#             print(f"Error fetching data: {e}")

#         time.sleep(6)  # Wait for 6 seconds before checking again

# # Custom Agent class to handle and process health data
# class HealthAgent(Agent):
#     def process_health_data(self, health_data):
#         # Check for emergency situations based on health parameters
#         if (health_data.get('heartRate', 0) > 100 or 
#             float(health_data.get('temperature', 0)) > 100.4 or
#             health_data.get('bloodPressure', {}).get('systolic', 0) > 140 or
#             health_data.get('bloodPressure', {}).get('diastolic', 0) > 90 or
#             health_data.get('bloodSugar', 0) > 180):
            
#             print("Emergency situation detected!")  # Print emergency alert
#             winsound.Beep(1000, 1000)  # Beep sound with frequency 1000 Hz for 1 second
#             # Emit a real-time event using SocketIO
#             socketio.emit('emergencyAlert', {'message': 'Emergency situation detected!'})

#         # Generate health advice based on the current health data
#         diet_plan, exercise_plan = self.generate_health_advice(health_data)
#         print(f"Advice: {diet_plan}")  # Print dietary advice
#         print(f"Exercise Suggestion: {exercise_plan}")  # Print exercise advice

#     def generate_health_advice(self, health_data):
#         # Default advice if no critical health data is detected
#         diet_plan = "Eat more vegetables and fruits."
#         exercise_plan = "Consider yoga or light walking."

#         # Customize advice based on specific health conditions
#         if health_data.get('heartRate', 0) > 90:
#             diet_plan = "Reduce sugar intake."
#             exercise_plan = "Consider doing meditation."
#         if float(health_data.get('temperature', 0)) > 99.5:
#             diet_plan = "Stay hydrated and rest."
#         if health_data.get('bloodPressure', {}).get('systolic', 0) > 130:
#             exercise_plan = "Avoid intense exercises and focus on relaxation techniques."

#         return diet_plan, exercise_plan

# # Route to retrieve the most recent health data from in-memory storage
# @app.route('/api/uagent/previous-data', methods=['GET'])
# def get_previous_data():
#     if health_data_store:
#         health_data = health_data_store[-1]  # Retrieve the most recent health data
#         response = {
#             "heartRate": health_data['heartRate'],
#             "pulse": health_data['pulse'],
#             "temperature": health_data['temperature'],
#             "bloodPressure": health_data['bloodPressure'],
#             "bloodSugar": health_data['bloodSugar'],
#             "timestamp": health_data.get('timestamp', 'N/A')  # Assuming you have a timestamp field
#         }
#     else:
#         response = {"response": "No previous data available."}
#     return jsonify(response)

# @app.route('/')
# def home():
#     return "Welcome to the Health Monitoring API!"

# # Route to retrieve current health data from in-memory storage
# @app.route('/api/uagent/current-data', methods=['GET'])
# def get_current_data():
#     if health_data_store:
#         health_data = health_data_store[-1]  # Retrieve the most recent health data
#         response = {
#             "heartRate": health_data['heartRate'],
#             "pulse": health_data['pulse'],
#             "temperature": health_data['temperature'],
#             "bloodPressure": health_data['bloodPressure'],
#             "bloodSugar": health_data['bloodSugar'],
#             "timestamp": health_data.get('timestamp', 'N/A')  # Assuming you have a timestamp field
#         }
#     else:
#         response = {"response": "No current data available."}
#     return jsonify(response)

# # Route to respond to chat queries
# @app.route('/api/chatbot/query', methods=['POST'])
# def handle_query():
#     user_query = request.json.get('query')
    
#     # Check for specific commands
#     if user_query.lower() == 'latest health data':
#         if health_data_store:
#             latest_health_data = health_data_store[-1]  # Get the latest data
#             return jsonify(latest_health_data)
#         else:
#             return jsonify({"response": "No health data available."})
    
#     elif user_query.lower() == 'previous data':
#         if len(health_data_store) > 1:
#             previous_health_data = health_data_store[-2]  # Get the second most recent data
#             return jsonify(previous_health_data)
#         else:
#             return jsonify({"response": "No previous data available."})

#     # Provide a generic response for unrecognized queries
#     return jsonify({"response": f"You asked: {user_query}. I don't have specific information for that."})

# # Initialize the HealthAgent instance
# agent = HealthAgent()

# # Start the health monitoring function in a separate thread so it runs continuously
# thread = threading.Thread(target=monitor_health_data, args=(agent,))
# thread.start()

# # Run the Flask app using SocketIO, listening on port 5000 with debug mode enabled
# if __name__ == '_main_':
#     try:
#         socketio.run(app, debug=True, port=5000)
#     except Exception as e:
#         print(f"Error starting Flask server: {e}")













# from uagents import Agent, Context
# import requests
# import time
# from flask_cors import CORS
# from flask import Flask, request, jsonify
# from flask_socketio import SocketIO
# import threading
# import winsound

# # Initialize Flask app and SocketIO
# app = Flask(__name__)
# CORS(app)
# socketio = SocketIO(app)

# # Configuration for the Node.js health data server
# node_js_server = "http://localhost:3000/health"

# # In-memory storage for health data
# health_data_store = []

# # HealthAgent definition using uagents
# class HealthAgent(Agent):
#     def __init__(self, name, seed):
#         super().__init__(name=name, seed=seed)
    
#     async def process_health_data(self, ctx: Context, health_data):
#         if (health_data.get('heartRate', 0) > 100 or 
#             float(health_data.get('temperature', 0)) > 100.4 or
#             health_data.get('bloodPressure', {}).get('systolic', 0) > 140 or
#             health_data.get('bloodPressure', {}).get('diastolic', 0) > 90 or
#             health_data.get('bloodSugar', 0) > 180):
            
#             ctx.logger.info("Emergency situation detected!")
#             winsound.Beep(1000, 1000)
#             socketio.emit('emergencyAlert', {'message': 'Emergency situation detected!'})
        
#         diet_plan, exercise_plan = self.generate_health_advice(health_data)
#         ctx.logger.info(f"Advice: {diet_plan}")
#         ctx.logger.info(f"Exercise Suggestion: {exercise_plan}")

#     def generate_health_advice(self, health_data):
#         diet_plan = "Eat more vegetables and fruits."
#         exercise_plan = "Consider yoga or light walking."

#         if health_data.get('heartRate', 0) > 90:
#             diet_plan = "Reduce sugar intake."
#             exercise_plan = "Consider doing meditation."
#         if float(health_data.get('temperature', 0)) > 99.5:
#             diet_plan = "Stay hydrated and rest."
#         if health_data.get('bloodPressure', {}).get('systolic', 0) > 130:
#             exercise_plan = "Avoid intense exercises and focus on relaxation techniques."

#         return diet_plan, exercise_plan

# # Monitor health data function using uagents
# # Monitor health data function using uagents
# def monitor_health_data(agent: HealthAgent):
#     while True:
#         try:
#             response = requests.get(node_js_server)
#             if response.status_code == 200:
#                 health_data = response.json()
#                 if all(key in health_data for key in ['heartRate', 'pulse', 'temperature', 'bloodPressure', 'bloodSugar']):
#                     health_data_store.append(health_data)
#                     socketio.emit('newHealthData', health_data)  # Emit new health data to frontend
#                     # Directly call the async function and run it
#                     socketio.start_background_task(agent.process_health_data, agent.context, health_data)
#                 else:
#                     print("Invalid data structure received")
#             else:
#                 print(f"Error fetching data: {response.status_code}")

#         except Exception as e:
#             print(f"Error fetching data: {e}")

#         time.sleep(6)


# # Initialize the HealthAgent instance
# agent = HealthAgent(name="HealthMonitor", seed="health recovery phrase")

# @app.route('/')
# def home():
#     return "Welcome to the Health Monitoring API!"

# @app.route('/api/uagent/current-data', methods=['GET'])
# def get_current_data():
#     if health_data_store:
#         health_data = health_data_store[-1]
#         response = {
#             "heartRate": health_data['heartRate'],
#             "pulse": health_data['pulse'],
#             "temperature": health_data['temperature'],
#             "bloodPressure": health_data['bloodPressure'],
#             "bloodSugar": health_data['bloodSugar'],
#             "timestamp": health_data.get('timestamp', 'N/A')
#         }
#     else:
#         response = {"response": "No current data available."}
#     return jsonify(response)

# # Start the Flask server and health monitoring
# if __name__ == "__main__":
#     threading.Thread(target=monitor_health_data, args=(agent,)).start()
#     socketio.run(app, debug=True, port=5000)






import requests
import time
from flask_cors import CORS
from uagents import Agent
from flask import Flask, request, jsonify
from flask_socketio import SocketIO
import threading
import winsound 

# Initialize Flask app and SocketIO for handling web requests and real-time events
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
socketio = SocketIO(app)

# Configuration for the Node.js health data server
node_js_server = "http://localhost:3000/health"  # URL for fetching health data

# In-memory storage for health data
health_data_store = []  # This will hold health data records

# Custom Agent class to handle and process health data
class HealthAgent(Agent):
    def process_health_data(self, health_data):
        # Check for emergency situations based on health parameters
        if (health_data.get('heartRate', 0) > 100 or 
            float(health_data.get('temperature', 0)) > 100.4 or
            health_data.get('bloodPressure', {}).get('systolic', 0) > 140 or
            health_data.get('bloodPressure', {}).get('diastolic', 0) > 90 or
            health_data.get('bloodSugar', 0) > 180):
            
            print("Emergency situation detected!")  # Print emergency alert
            winsound.Beep(1000, 1000)  # Beep sound with frequency 1000 Hz for 1 second
            # Emit a real-time event using SocketIO
            socketio.emit('emergencyAlert', {'message': 'Emergency situation detected!'})

        # Generate health advice based on the current health data
        diet_plan, exercise_plan = self.generate_health_advice(health_data)
        print(f"Advice: {diet_plan}")  # Print dietary advice
        print(f"Exercise Suggestion: {exercise_plan}")  # Print exercise advice

    def generate_health_advice(self, health_data):
        # Default advice if no critical health data is detected
        diet_plan = "Eat more vegetables and fruits."
        exercise_plan = "Consider yoga or light walking."

        # Customize advice based on specific health conditions
        if health_data.get('heartRate', 0) > 90:
            diet_plan = "Reduce sugar intake."
            exercise_plan = "Consider doing meditation."
        if float(health_data.get('temperature', 0)) > 99.5:
            diet_plan = "Stay hydrated and rest."
        if health_data.get('bloodPressure', {}).get('systolic', 0) > 130:
            exercise_plan = "Avoid intense exercises and focus on relaxation techniques."

        return diet_plan, exercise_plan

# Function to continuously monitor health data from the server
def monitor_health_data(agent):
    while True:
        try:
            response = requests.get(node_js_server)
            if response.status_code == 200:
                health_data = response.json()

                if all(key in health_data for key in ['heartRate', 'pulse', 'temperature', 'bloodPressure', 'bloodSugar']):
                    print(f"Received health data: {health_data}")
                    # Pass the health data to the agent for processing
                    socketio.start_background_task(agent.process_health_data, health_data)

                    # Save the health data to the in-memory store
                    health_data_store.append(health_data)

                else:
                    print("Invalid data structure received")

            else:
                print(f"Error fetching data: {response.status_code}")

        except Exception as e:
            print(f"Error fetching data: {e}")

        time.sleep(6)  # Wait for 6 seconds before checking again

# Route to retrieve the most recent health data from in-memory storage
@app.route('/api/uagent/previous-data', methods=['GET'])
def get_previous_data():
    if health_data_store:
        health_data = health_data_store[-1]  # Retrieve the most recent health data
        response = {
            "heartRate": health_data['heartRate'],
            "pulse": health_data['pulse'],
            "temperature": health_data['temperature'],
            "bloodPressure": health_data['bloodPressure'],
            "bloodSugar": health_data['bloodSugar'],
            "timestamp": health_data.get('timestamp', 'N/A')  # Assuming you have a timestamp field
        }
    else:
        response = {"response": "No previous data available."}
    return jsonify(response)

@app.route('/')
def home():
    return "Welcome to the Health Monitoring API!"

# Route to retrieve current health data from in-memory storage
@app.route('/api/uagent/current-data', methods=['GET'])
def get_current_data():
    if health_data_store:
        health_data = health_data_store[-1]  # Retrieve the most recent health data
        response = {
            "heartRate": health_data['heartRate'],
            "pulse": health_data['pulse'],
            "temperature": health_data['temperature'],
            "bloodPressure": health_data['bloodPressure'],
            "bloodSugar": health_data['bloodSugar'],
            "timestamp": health_data.get('timestamp', 'N/A')  # Assuming you have a timestamp field
        }
    else:
        response = {"response": "No current data available."}
    return jsonify(response)

# Route to respond to chat queries
@app.route('/api/chatbot/query', methods=['POST'])
def handle_query():
    user_query = request.json.get('query')
    
    # Check for specific commands
    if user_query.lower() == 'latest health data':
        if health_data_store:
            latest_health_data = health_data_store[-1]  # Get the latest data
            return jsonify(latest_health_data)
        else:
            return jsonify({"response": "No health data available."})
    
    elif user_query.lower() == 'previous data':
        if len(health_data_store) > 1:
            previous_health_data = health_data_store[-2]  # Get the second most recent data
            return jsonify(previous_health_data)
        else:
            return jsonify({"response": "No previous data available."})

    # Provide a generic response for unrecognized queries
    return jsonify({"response": f"You asked: {user_query}. I don't have specific information for that."})

# Initialize the HealthAgent instance
agent = HealthAgent()

# Start the health monitoring function in a separate thread so it runs continuously
thread = threading.Thread(target=monitor_health_data, args=(agent,))
thread.start()

# Run the Flask app using SocketIO, listening on port 5000 with debug mode enabled
if __name__ == '__main__':
    try:
        socketio.run(app, debug=True, port=5000)
    except Exception as e:
        print(f"Error starting Flask server: {e}")
