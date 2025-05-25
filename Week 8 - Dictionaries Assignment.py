# Hassan - Week 8 Dictionaries Assignment
# This program takes employee data from lists and puts it into a list of dictionaries
# This keeps related info together like a database row

# Step 1: Lists with employee data from last week
employee_numbers = [2001, 2002, 2003, 2004]
employee_names = ["Muayed Alomari", "Furhaan Khan", "Ahmed Saudi", "Ahmed Altaii"]
employee_salaries = [28.50, 30.75, 26.40, 32.10]
hourly_rates = [28.50, 30.75, 26.40, 32.10]  # Using same numbers here
company_raises = [1.10, 1.08, 1.12, 1.15]    # Raise multipliers (example: 1.10 = 10% raise)

# Step 2: Create a list that will store the final structured employee dictionaries
employee_data = []

# Step 3: Go through each employee using a loop to combine their info into a dictionary
for i in range(len(employee_numbers)):
    # Step 3a: Make a dictionary for one employee using data from each list
    employee = {
        'employee_number': employee_numbers[i],
        'name': employee_names[i],
        'salary': employee_salaries[i],
        'hourly_rate': hourly_rates[i],
        'raise_multiplier': company_raises[i]
    }

    # Step 3b: Add the employee dictionary to the final list
    employee_data.append(employee)

# Step 4: Print the final structured list like a database table
print("Final Employee Data (Structured):")
for emp in employee_data:
    print(emp)
