from datetime import date

def age_calculator():
    print("🧓 Age Calculator 🧒")
    birth_year = int(input("Enter your birth year: "))
    current_year = date.today().year
    age = current_year - birth_year
    print(f"You are {age} years old in {current_year}.")

age_calculator()
