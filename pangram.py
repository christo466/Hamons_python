def is_pangram(s):
    # Define a pattern containing all lowercase alphabet letters
    pattern = 'abcdefghijklmnopqrstuvwxyz'
    
    # Convert the input string to lowercase and convert it to a list
    stringlist = list(s.lower())
    
    # Iterate through each letter in the pattern
    for x in pattern:
        # Check if the current letter is not present in the input string
        if x not in stringlist:
            return False  # Return False if any letter is missing
    
    # If all letters are present, return True
    return True

if __name__ == "__main__":
    # Prompt the user to enter a string
    s = input("Enter a string: ")
    
    # Check if the input string is a pangram and print the result
    if is_pangram(s):
        print("The string is a pangram.")
    else:
        print("The string is not a pangram.")
