class WordCounter:
    def __init__(self, file_name):
        # Initialize the WordCounter object with the file name.
        self.file_name = file_name
    
    def count_words(self):
        # Count the number of words in the text file.
        try:
            with open(self.file_name, 'r') as file:
                text = file.read()
                words = text.split()
                return len(words)
        except FileNotFoundError:
            print(f"Error: File '{self.file_name}' not found.")
            return -1
        except IOError:
            print(f"Error: Could not read from file '{self.file_name}'")
            return -1

# Text file
file_name = 'sample.txt'

# Create an instance of WordCounter with the file name
word_counter = WordCounter(file_name)

# Count the words in the file
word_count = word_counter.count_words()

# Display the result if the file was found and read successfully
if word_count != -1:
    print(f"Number of words in '{file_name}': {word_count}")
