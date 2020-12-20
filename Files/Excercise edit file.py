file = open("filename.txt","r")

newline = "This is a new line" + "\n"
file.readline()
newline = newline+file.read()
file.close()

file = open("filename.txt","w")
file.write(str(newline))
file.close()
        
