import requests

def fetch_report():
    base_url = 'http://127.0.0.1:5000/'
    endpoint = 'birthdays'

    month = input("Enter the month: ")
    department = input("Enter the department: ")

    url = f"{base_url}{endpoint}?month={month}&department={department}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        print(f"Report for {department} department for {month} fetched.")
        print(f"Total: {data['total']}")
        print("Employees:")
        for employee in data['employees']:
            print(f"- {employee['birthday']}, {employee['name']}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching report: {e}")

if __name__ == "__main__":
    fetch_report()
