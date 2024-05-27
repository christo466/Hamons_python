def freq(s):
    # Initialize an empty dictionary to store character frequencies
    my_dict = {}
    
    # Convert the input string to lowercase and convert it to a list of characters
    mystring_list = list(s.lower())
    
    # Get the length of the list
    length = len(mystring_list)
    
    # Iterate over each character in the list
    for x in mystring_list:
        # Initialize a counter for the frequency of the current character
        number_of_chara = 0
        
        # Iterate through the entire list again to count occurrences of the current character
        i = 0
        while i < length:
            if x == mystring_list[i]:
                number_of_chara  += 1  # Increment the counter if the current character matches
            i += 1
            
        # Add the character frequency to the dictionary if it's not a space
        if x != " ":
            my_dict[x] = number_of_chara 
    
   
    print(my_dict)        

if __name__ == "__main__":
    # Prompt the user to enter a string
    s = input("Enter a string: ")
    
    # Call the freq function to calculate and print character frequencies
    freq(s)
