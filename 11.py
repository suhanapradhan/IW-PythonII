
filename = input("Enter a filename: ")
for i in range(len(filename)):
    if filename[i] == ".":
        print("The extension of the filename is:", filename[i+1:])
