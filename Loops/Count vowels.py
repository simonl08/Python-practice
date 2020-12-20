vowels = ["a","e","i","o","u","A","E","I","O","U"]
word=str(input("Enter any words here: "))
count=0

for c in word.lower():
    for v in vowels:
        if c == v:
            count=count+1
print(count)
