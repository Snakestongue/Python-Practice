credit_number = "1234-5678-9023-3456"
#[start: end: step]
#[::x] will print ever x character(if 2 it will print every second char)
#[-x] will give you last char and than like 1(-1 will be 6, -2 will be 5, so on)
#start is inclusive, end is exlcusive which is why 0-4 only prints 1234 and not 1234-

credit_number = credit_number[::-1] # reverses string
print(credit_number)