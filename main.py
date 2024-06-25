def print_file_content():
    file_path = 'books/frankenstein.txt'  # Adjust the path as per your directory structure

    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
            return content.lower()  # Convert content to lowercase and return
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

def count_words(text):
    # Split the text into words based on whitespace
    words = text.split()
    return len(words)

def count_characters(text):
    char_count = {}
    
    # Convert all characters to lowercase to avoid case sensitivity
    text_lower = text.lower()
    
    # Count occurrences of each character
    for char in text_lower:
        if char.isalpha():  # Check if the character is an alphabet
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    return char_count

def main():
    print("Reading content of frankenstein.txt:")
    text = print_file_content()
    
    if text:
        num_words = count_words(text)
        print(f"\nNumber of words in the text: {num_words}")
        
        char_count = count_characters(text)
        print("\nCharacter counts (lowercase):")
        for char, count in sorted(char_count.items()):  # Sort characters alphabetically
            print(f"{char}: {count}")
        
        # Generate a report for characters in alphabetical order
        print("\nCharacter counts report (alphabetical order):")
        total_chars = sum(char_count.values())
        for char, count in sorted(char_count.items(), key=lambda item: item[0]):  # Sort characters alphabetically
            percentage = (count / total_chars) * 100 if total_chars > 0 else 0
            print(f"{char}: {count} ({percentage:.2f}%)")
        
        # Generate a report for words
        print("\nWord counts report:")
        words = text.split()
        unique_words = set(words)
        total_words = len(words)
        unique_word_count = len(unique_words)
        average_word_length = sum(len(word) for word in words) / total_words if total_words > 0 else 0
        
        print(f"Total words: {total_words}")
        print(f"Unique words: {unique_word_count}")
        print(f"Average word length: {average_word_length:.2f} characters")
        print("\nMost common words:")
        from collections import Counter
        counter = Counter(words)
        for word, count in counter.most_common(10):
            print(f"{word}: {count}")

if __name__ == "__main__":
    main()
