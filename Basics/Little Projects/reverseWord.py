inp = input("enter a word ")
spliter = inp.split()
for i in spliter:
    print(i[::-1], end =' ')
