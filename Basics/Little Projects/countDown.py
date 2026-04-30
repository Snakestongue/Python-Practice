import time

inp = int(input("How long to sleep(in seconds) "))
for i in range(0, inp,):
    print(i)
    time.sleep(1)
print("Time done!")
