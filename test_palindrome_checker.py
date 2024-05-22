import re
import logging

# Configure logging
logging.basicConfig(filename='palindrome_log.txt', 
                    level=logging.INFO, format='%(asctime)s - %(message)s')

def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    # Check if the cleaned string is equal to its reverse
    is_palindrome = cleaned == cleaned[::-1]
    return is_palindrome, cleaned



if __name__ == "__main__":
    while True:
        # Ask the user to input a string
        user_input = input("Enter a string to check if it's a palindrome (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        result, cleaned_str = is_palindrome(user_input)
        # Print the result
        print(f'Is "{user_input}" a palindrome? {result}')
        print(f'Cleaned string: "{cleaned_str}"')
        # Log the input and result
        logging.info(f'Input: "{user_input}", Cleaned: "{cleaned_str}", Is Palindrome: {result}')
