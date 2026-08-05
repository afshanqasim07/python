# try:
#     age = int(input("Enter your age:"))
#     print(age)
# except ValueError:
#     print("enter the age number only")
try:
     with open ("my_notes.txt" ,"r") as file:
        print("FILE EXIST")
except FileNotFoundError:
    print("NO DATASET EXIST")