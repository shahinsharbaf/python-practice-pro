number = int(input("Enter how many square created in dic? "))

square_dictinary = {}

for i in range(1, number+1):
    square_dictinary[i] = i*i

print(square_dictinary)
