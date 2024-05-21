def fizzbizz(n):
    # Loop through numbers from 1 to n (inclusive)
    for i in range(1, n + 1):
        # Check if i is divisible by 15 (3 and 5)
        if i % 15 == 0:
            print("fizzbizz")  # Print "fizzbizz" if divisible by 15
        # Check if i is divisible by 3
        elif i % 3 == 0:
            print("fizz")  # Print "fizz" if divisible by 3
        # Check if i is divisible by 5
        elif i % 5 == 0:
            print("bizz")  # Print "bizz" if divisible by 5
        # If none of the above, just print the number
        else:
            print(i)

if __name__ == "__main__":
    # Prompt the user to enter a number and convert it to an integer
    n = int(input("Enter a number: "))
    fizzbizz(n)
