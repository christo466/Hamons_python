def is_palindrome(s):
    length = len(s)
    s=list(s.lower())
    for y in range(length // 2):  # Only iterate up to half the length of the string
        if s[y] != s[length - 1 - y]:
            return False  # Return False as soon as a mismatch is found
    return True  # Return True if no mismatches were found

if __name__ == "__main__":
    # Prompt the user to enter a string
    s = input("Enter a string: ")
    # Check if the input string is a palindrome
    if is_palindrome(s):
        print("Yes, it's a palindrome!")
    else:
        print("No, it's not a palindrome.")
