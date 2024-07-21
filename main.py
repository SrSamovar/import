from datetime import datetime
from application.db.people import get_employees
from application.salary import calculate_salary

now = datetime.now()

if __name__ == "__main__":
    print(get_employees())
    print(calculate_salary())
    print(now)
