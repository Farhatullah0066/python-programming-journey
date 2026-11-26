age = 20
marks = 75
scholarship = "yes"
if age>=18 and (marks>=60 or scholarship=="yes"):
    print("You are eligible for the scholarship.")
else:
    print("admission rejected.")
print("admission completed.")


#Exercise 2 - Admission eligibility
age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))
scholarship = input("Do you have a scholarship? (yes/no): ").lower()
if age >= 18 and (marks >= 60 or scholarship == "yes"):
    print("admission approved.")
else:
    print("admission rejected.")
print("admission completed.")