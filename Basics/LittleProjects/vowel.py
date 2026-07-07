inp = input("Enter:  ")
vowels = "aeiou"
count = 0
for i in inp:
    if i.lower() in vowels:
        count +=1

print(count)