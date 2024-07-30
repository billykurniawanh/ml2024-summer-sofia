from module5_mod import NumberList

def main():
    number_list = NumberList()

    N = int(input("Input a number: "))
    number_list.set_length(N)

    for i in range(number_list.length):
        number = int(input(f"Enter number {i + 1}: "))
        number_list.insert(number)

    X = int(input("Enter a number to search for: "))
    result = number_list.search(X)
    print(result)

main()