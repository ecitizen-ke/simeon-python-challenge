import re

def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    # Example usage
    example = "A man, a plan, a canal, Panama"
    print(f'Is "{example}" a palindrome? {is_palindrome(example)}')
