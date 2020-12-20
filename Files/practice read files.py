file = open("filename.txt","r")

print("First line: " + file.readline())
print("Second line: " + file.readline())
print("Rest of file: " + file.read())
print("Blank line: " + file.readline())

file.close()
