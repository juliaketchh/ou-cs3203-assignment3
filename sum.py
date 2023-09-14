def sum(nums):
    total = 0
    for i in nums:
       total += i
    return total
def product(nums):
    total = 1
    for i in nums:
        total = total * i
    return total

def main():
    inputString = input("enter a list of numbers (seperated by commas): ")
    inputList = inputString.split(',')

    try:
        numbers = [int(num) for num in inputList]
    except ValueError:
        print("Invalid input. Please enter numbers separated by commas.")

    print("sum of the numbers: ")
    print(sum(numbers))
    print("product of the numbers: ")
    print(product(numbers))

if __name__ == "__main__":
    main()