filename = input("Enter the filename: ")

last_dot = filename.rfind('.')

if last_dot == -1:
    print("No file extension found.")
else:
    extension = filename[last_dot + 1:]
    print(f"The file extension is: {extension}")
