file = open("filename.txt","r")

print("First line: ")
print(file.readline())
file.readline()
print("Third line: ")
print(file.readline())
file.seek(0)
print("First Line again: ")
print(file.readline())


file.close()
