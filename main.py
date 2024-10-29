
def count_characters(text):
    # Convert the text to lowercase to avoid duplicates
    text = text.lower()
    
    # Initialize an empty dictionary to store character counts
    char_count = {}
    
    # Loop through each character in the text
    for char in text:
        # If character is already in dictionary, increment its count
        if char in char_count:
            char_count[char] += 1
        else:
            # Otherwise, add the character to the dictionary with count 1
            char_count[char] = 1
    
    return char_count

def main(file_path):
    # Read the file content
    with open(file_path, 'r') as file:
        text = file.read()
    
    # Count words
    words = text.split()
    word_count = len(words)
    
    # Count characters
    char_count = count_characters(text)
    
    # Sort characters by frequency in descending order
    sorted_chars = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    
    # Print the report
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\n")
    
    for char, count in sorted_chars:
        # Only display letters for this report
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")

main("books/frankenstein.txt")
