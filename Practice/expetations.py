
try:
    age=int(input('Age : '))
    income=200000
    risk=income//age
    print(f"Age : {age}")
    print(f"Risk : {risk}")
except ValueError:
    print("Invalid Value")
except ZeroDivisionError:
    print("Age can not be zero")