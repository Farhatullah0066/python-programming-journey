#while loop

number = 1
while number <= 10:
    print(number)
    number += 1 
    
    
    #exercise -2 
number = 2
while number<=20:
    print(number)
    number += 2
    
    #exercise -3
number = 1

while number <= 10:

    if number == 5:
        number += 1
        continue

    print(number)
    number += 1

print("Loop finished")

#exercise -4
for i in range(1, 10):
    if i % 2 == 0:
        print(i, "is even")
        
        #exercise -5
for i in range(1, 11):
    if i % 2 != 0:
        print(i, "is odd")
    
    
    #exercise -6
  

for i in range(1, 5):
    for j in range(i ,):
        print("*", end=" ")
    print()
    
    #exercise -7 
    for i in range(1, 10):
        print(i*5)
    
    #exercise -8 sum of first 10 natural numbers
total = 0
for i in range(1, 11):
    total += i
print("Sum of first 10 natural numbers is:", total)

#exercise -9 factorial of a number
number = 5
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print("Factorial of", number, "is:", factorial)

#exercise -10 multiplication table of a number
number = int(input("Enter a number to print its multiplication table: "))
print("Multiplication table of", number)
for i in range(1, 11):
    print(number, "x", i, "=", number * i)