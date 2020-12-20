file = open("sportsteam.txt","r")

print("second and third character of second line: ")
file.readline()
file.readline()
file.read(1)
print(file.read(2))

file.close
