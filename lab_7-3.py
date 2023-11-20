"""
Create a Python file named lab_7-3.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Copy your lab 7-1 code into the file
Add 4 test cases to the end of the file, with comments
Ensure your lab runs accurately

"""
# Author: Andrew Tkacs

def greeting():
    """
    This function prints 'Hello World' on one line.
    """
    print("Hello World!")

    # Return the docstring for the greeting function
    return greeting.__doc__

# Call the greeting function
greeting()

# Test Case 1

# Call the greeting function again and print the returned docstring
docstring_result = greeting()
print(docstring_result)

# Test Case 2

# Call the greeting function with additional text
greeting_with_text = greeting() + " how are you "
print(greeting_with_text)

# Test Case 3

# Call the greeting function and store the result in a variable
greeting_result = greeting()

# Test Case 4

# Print the result of the greeting function stored in the variable
print(greeting_result)
