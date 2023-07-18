filename = input("Input the Filename: ")

dot_index = filename.rfind('.')


if dot_index != -1:
    extension = filename[dot_index + 1:]
    print("The extension of the file is:", extension)
else:
    print("Invalid file name or extension not found.")
