from flask import Flask, request, jsonify
from datetime import datetime
import json

app = Flask(__name__)

# Load data from JSON file
with open('database.json', 'r') as json_file:
    database = json.load(json_file)


def filter_employees(month, department, filter_key):
    filtered_employees = []

    for employee in database:
        employee_month = datetime.strptime(employee[filter_key], "%Y-%m-%d").strftime("%B").lower()
        if month.lower() == employee_month and department.lower() == employee["Department"].lower():
            filtered_employees.append({
                "id": employee["Id"],
                "name": employee["Name"],
                "birthday": datetime.strptime(employee["Birthday"], "%Y-%m-%d").strftime("%b %d"),
                "employed": datetime.strptime(employee["Hiring_Date"], "%Y-%m-%d").strftime("%b %d")
            })

    return filtered_employees


@app.get('/birthdays')
def get_birthdays():
    month = request.args.get('month')
    department = request.args.get('department')

    if not month or not department:
        return jsonify({"error": "Missing parameters"}), 400

    birthdays = filter_employees(month, department, "Birthday")

    return jsonify({
        "total": len(birthdays),
        "employees": birthdays
    })


@app.get('/anniversaries')
def get_anniversaries():
    month = request.args.get('month')
    department = request.args.get('department')

    if not month or not department:
        return jsonify({"error": "Missing parameters"}), 400

    anniversaries = filter_employees(month, department, "Hiring_Date")

    return jsonify({
        "total": len(anniversaries),
        "employees": anniversaries
    })


if __name__ == '__main__':
    app.run(debug=True)
