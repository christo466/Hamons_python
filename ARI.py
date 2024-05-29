from sys import argv
import re

script, file = argv

# Open the file and read its contents
open_file=open(file) 
contents = open_file.read()
open_file.close()
# Calculate the number of words
words_file = len(contents.split())

# Print the number of words
print(f"words count:{words_file}")

# Calculate the number of characters
character = len(contents)

# Print the number of characters
print(f"the character count:{character}")

# Calculate the number of sentences using regex
regex = r"[.!?]"
sen_count = len(re.findall(regex, contents))

# Print the number of sentences
print(f"the sentence count: {sen_count}")


ARI = int(4.71 * (character / words_file) + (0.5 * (words_file / sen_count)) - 21.43)
print(ARI)

# Print grade level based on ARI value
match ARI:
        case 1:
            print("Kindergarten")
        case 2:
            print("First grade")
        case 3:
            print("Second grade")
        case 4:
            print("Third grade")
        case 5:
            print("Fourth grade")
        case 6:
            print("Fifth grade")
        case 7:
            print("Sixth grade") 
        case 8:
            print("Seventh grade")
        case 9:
            print("Eighth grade")
        case 10:
            print("Ninth grade")
        case 11:
            print("Tenth grade")
        case 12:
            print("Eleventh grade")
        case 13:
            print("Twelfth grade")
        case 14:
            print("College")
        case _:
            if ARI< 1:
                print("kindergarter")
            else:
                print("Above college")
