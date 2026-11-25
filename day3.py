x = 17
y = 5

print(x / y)
print(x // y)
print(x % y)
print(x ** 2)

# Exercise 2

a = 10
a += 5
a *= 2
a -= 8
print(a)


# Exercise 3

x = 15
y = 10

print(x > y)
print(x == y)
print(x != y)
print(x <= 15)
print(type(x > y))


# Exercise 4

product = int(input("Enter the product price: "))
quantity = int(input("Enter the quantity: "))
total_bill = product * quantity

if total_bill >= 5000:
    print(total_bill)


# Exercise 5 — Logical operators

a = 10
b = 20

print(a < b and b == 20)
print(a > b or b == 20)
print(not a == 10)
print(a == 10 and b < 15)


# Exercise 6 — Truthiness

print(bool(""))
print(bool("Python"))
print(bool(0))
print(bool(100))
print(bool([]))
print(bool([1, 2, 3]))


# Exercise 7

age = int(input("Enter your age: "))
student_card = True
permission = True

eligible = (age >= 18 and student_card) or permission
print(eligible)

#exercise 8 

total_bill = int(input("Enter the total bill amount: "))
membership_card = input("Do you have a membership card? (yes/no): ").lower() == "yes"
discount = bool(input("Do you have a discount? (yes/no): ").lower() == "yes")
eligible = total_bill >= 5000 and membership_card
print("Eligible for discount:", eligible)


Exercise 11 — Short-circuit experiment
print(False and print("Hello"))
print(True or print("World"))
print(True and print("Python"))
print(False or print("Programming"))