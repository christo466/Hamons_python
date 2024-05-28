# Hamons_python
## Automated Readability Index

We use __./script1.sh__ to run the program after running the program we input the file for checking ARI.from __sys__ we import __argv__ module.The __argv__ is a list in the __sys__ module that contain the command line arguments passed to a python script.After that we import __re__ .

The __re__ module in the python is used for working with regular expressions, which we use for matching pattern in text.__script, file = argv__ is used to unpack command line arguments into variables in a python script. we unpack the elements of the argv list into two variables __script__ and __file__. We open the input file using __open(file)__  command and we assign it to variable called __open_file__.

When we open the file without specifying the mode it automatically opens in the read mode. After that we read the file using __read__ command and we assign the the contents into __content__ variable. After that we close the file using __close()__.

After that we split the contents inside the variable __contents__ using __split()__ command which gives a list of all the words in the file and we use __len()__ command to find the count of the words inside the file.

To calculate the number of characters in the file we find the length of the __contents__ variable using __len()__ command which gives the count of the total characters.

To Calculate the number of sentences we use regular expression __re__ which we have imported. first we create a regular expression using __r"[.!?]"__. the __r__ indicates the raw strings in the regular expression. The raw strings consider the backslashes as literal characters. after this we assign it to a variable called __regex__.

we use __re.findall()__ function to scan through the given string and returns a list which contains all the matches. we give two inputs inside the re.findall function one is a regular expression
and another one is the variable that contain the string. By using this we can find the sentence count. we store this in the sen_count variable.

We Calculate the __Automated readability index__ using this values with the ARI formula. We store the output into the ARI variable. we use __match__ statement which is a control flow construct for matching against a series of cases And print the outputs. 






