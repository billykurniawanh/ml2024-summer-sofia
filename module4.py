N = int(input("Input a number: "))

number_list = []
for i in range(N):
    num = int(input(f"Enter number {i + 1}: "))
    number_list.append(num)

X = int(input("Enter a number to search for: "))

if X not in number_list:
    print(-1)
else:
    index = number_list.index(X) + 1
    print(index)
