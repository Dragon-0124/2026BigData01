import ticket

humans = int(input("How many peoples do you with? "))

ages=list()
age = 0

for i in range(humans):
    age = int(input(f"What is the age of person {i + 1}? "))
    ages.append(age)

print(f" Total Price is ₩{ticket.entrance_fee(ages)}.")