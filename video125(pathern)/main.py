number_of_starts = int(input("Enter stars number? "))

for i in range(1, number_of_starts+1):
    for j in range(0, i):
        print('*', end=' ')
    print()


for i in range(-number_of_starts+1, 0):
    for j in range(0, -i):
        print("*", end=" ")
    print()
