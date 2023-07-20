
list = input("Enter a list of numbers ").split()

positive = []

for num in list:
    try:
        num = int(num)
        if num > 0:
            positive.append(num)
    except ValueError:
        pass

print("Positive numbers in the list:", positive)
