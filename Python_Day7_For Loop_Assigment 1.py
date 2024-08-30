# Python program to check if the given string is a palindrome 

def is_palindrome(s):
    # Remove spaces and convert to lowercase to handle case-insensitivity
    s = s.replace(" ", "").lower()
    
    # Get the length of the string
    length = len(s)
    
    # Loop through half of the string
    for i in range(length // 2):
        # Compare characters from the start and end of the string
        if s[i] != s[length - 1 - i]:
            return False  # Not a palindrome if characters don't match
    
    return True  # Palindrome if all characters match

# Main part of the program
if __name__ == "__main__":
    # Input string from the user
    input_string = input("Enter a string to check if it's a palindrome: ")
    
    # Check if the input string is a palindrome
    if is_palindrome(input_string):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

# Output:

# (String is Palindrome Output):
# Enter a string to check if it's a palindrome: Malayalam
# The string is a palindrome.

# (String is Not Palindrome Output):
# Enter a string to check if it's a palindrome: Hello
# The string is not a palindrome.

