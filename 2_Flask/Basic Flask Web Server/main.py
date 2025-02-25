from flask import Flask 

# Instance of Flask Class
app = Flask(__name__)

# Define Home Page Route
@app.route("/")
def home():
  return "Welcome to Flask Web Server"

# Start the Web Server
if __name__ == "__main__":
  # Run on Default Port 5000
  print("Web Server Started at http://127.0.0.1:5000/")
  app.run(host="127.0.0.1", port=5000, debug=True) 