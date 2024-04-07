from flask import Flask, render_template

app = Flask(__name__)

# Sample data (you would replace this with actual data)
members = [
    {"id": 1, "name": "John Doe", "membership_type": "Premium"},
    {"id": 2, "name": "Alice Smith", "membership_type": "Basic"},
    # Add more members here
]

@app.route('/')
def dashboard():
    return render_template('dashboard.html', members=members)

if __name__ == '__main__':
    app.run(debug=True)
