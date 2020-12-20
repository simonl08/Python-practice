file = open("filename.txt","r")

print("First line: ")
print(file.readline())
file.seek(0)
print("First character: ")
print(file.read(1))
file.readline()
print("Second line: ")
print(file.readline())

print(file.read(2))

file.close()
