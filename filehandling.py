with open("my_notes.txt", "w") as file:
    file.write("AFSHAN")
with open("my_notes.txt", "a") as file:
    file.write("\nLEARNING PYTHON")
with open("my_notes.txt", "r") as file:
    print(file.read())