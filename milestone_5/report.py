import csv
from datetime import datetime


def read_csv(file_name):
    data = []
    with open(file_name, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data


def generate_report(data, month):
    birthdays = {}
    anniversaries = {}

    for employee in data:
        hire_date = datetime.strptime(employee['Hiring_Date'], '%Y-%m-%d')
        birthday = datetime.strptime(employee['Birthday'], '%Y-%m-%d')

        if hire_date.month == datetime.strptime(month, '%B').month:
            anniversaries[employee['Department']] = anniversaries.get(employee['Department'], 0) + 1
        elif birthday.month == datetime.strptime(month, '%B').month:
            birthdays[employee['Department']] = birthdays.get(employee['Department'], 0) + 1

    print(f"Report for {month} generated")
    print("--- Birthdays ---")
    print(f"Total: {sum(birthdays.values())}")

    print("By department:")
    for department, count in birthdays.items():
        print(f"- {department}: {count}")

    print("--- Anniversaries ---")
    print(f"Total: {sum(anniversaries.values())}")

    print("By department:")
    for department, count in anniversaries.items():
        print(f"- {department}: {count}")


if __name__ == "__main__":
    database_file = 'database.csv'
    report_month = 'January'

    employee_data = read_csv(database_file)
    generate_report(employee_data, report_month)
