# List of employees (each employee is a tuple: (name, age, department, salary))
employees = [
    ("Omar", 30, "IT", 3000),
    ("Sara", 28, "HR", 2500),
    ("Khaled", 35, "IT", 3200),
    ("Lina", 26, "Finance", 2700)
]

# Function to add a new employee
def add_employee():
    name = input("Enter employee name: ")
    age = int(input("Enter employee age: "))
    department = input("Enter department: ")
    salary = float(input("Enter salary: "))
    employees.append((name, age, department, salary))
    print("✅ Employee added successfully.\n")

# Function to search for an employee by name
def search_employee():
    name = input("Enter the name to search: ")
    found = False
    for name1,age,department,salary in employees:
        if name1.lower() == name.lower():
            print(f"Employee: Name={name1}, Age={age}, Department={department}, Salary={salary}")
            found = True
            break
    if not found:
        print("❌ Employee not found.\n")

# Function to calculate average salary
def average_salary():
    if not employees:
        print("There are no employees.")
        return
    total = sum(emp[3] for emp in employees)
    avg = total / len(employees)
    print(f"The average salary is: %d\n"%avg)

# Function to display employees by department
def show_by_department():
    dept = input("Enter department name: ")
    found = False
    for emp in employees:
        if emp[2].lower() == dept.lower():
            print(f"Name: {emp[0]}, Age: {emp[1]}, Salary: {emp[3]}")
            found = True
    if not found:
        print("❌ No employees found in this department.\n")

# Main menu
def main_menu():
    while True:
        print("\n📋 Employee Management System")
        print("1. Add Employee")
        print("2. Search Employee by Name")
        print("3. Calculate Average Salary")
        print("4. Show Employees by Department")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            search_employee()
        elif choice == "3":
            average_salary()
        elif choice == "4":
            show_by_department()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid option. Please try again.")

# Run the program
main_menu()
