file = open("sportsteam.txt","w")
file.write("Manchester City" + "\n")
file.write("Manchester United" + "\n")
file.write("Chelsea" + "\n")
file.write("Liverpool" + "\n")
file.write("Leicester City"+ "\n") 

file.close()

file = open("sportsteam.txt","r")

print("First sports team: " + file.readline())
print("Second sports team: " + file.readline())

file.close()
