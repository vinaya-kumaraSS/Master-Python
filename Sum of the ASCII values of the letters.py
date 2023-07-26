def check(n):
    schar = n
    for i in range(65, 91):
        if schar == chr(i):
            return i
word = input("Enter the word (Capital Letter): ")
sum_of_letters = 0
for n in word:
    sum_of_letters=sum_of_letters+ check(n)

print(f"Sum of the ASCII values of the letters is {sum_of_letters}")
