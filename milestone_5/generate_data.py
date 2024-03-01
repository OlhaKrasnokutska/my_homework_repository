from random import choice

from faker import Faker
import csv

fake = Faker()

def generate_data(num_employees=200):
    departments = ["HR", "Finance", "Engineering", "R&D"]
    with open('database.csv', 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Hiring_Date', 'Department', 'Birthday']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for _ in range(num_employees):
            name = fake.name()
            hiring_date = fake.date_this_decade()
            department = choice(departments)
            birthday = fake.date_of_birth(minimum_age=22, maximum_age=60)

            writer.writerow({'Name': name, 'Hiring_Date': hiring_date, 'Department': department, 'Birthday': birthday})

generate_data()
print("Data generated and written to database.csv.")