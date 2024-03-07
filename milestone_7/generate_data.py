from random import choice
from faker import Faker
import json
from datetime import datetime

fake = Faker()

def generate_data(num_employees=200):
    departments = ["HR", "Finance", "Engineering", "R&D"]
    employee_data = []
    employee_id = 0

    for _ in range(num_employees):
        employee_id += 1
        name = fake.name()
        hiring_date = fake.date_this_decade().strftime('%Y-%m-%d')
        department = choice(departments)
        birthday = fake.date_of_birth(minimum_age=22, maximum_age=60).strftime('%Y-%m-%d')

        employee_data.append({
            'Id': employee_id,
            'Name': name,
            'Hiring_Date': hiring_date,
            'Department': department,
            'Birthday': birthday
        })

    with open('database.json', 'w') as json_file:
        json.dump(employee_data, json_file, indent=2)

generate_data()
print("Data generated and written to database.json.")
