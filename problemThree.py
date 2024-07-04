class WordCounter:
    def __init__(self, file_name):
        self.file_name = file_name
    
    def count_words(self):
        try:
            with open(self.file_name, 'r') as file:
                text = file.read()
                words = text.split()
                return len(words)
        except FileNotFoundError:
            print(f"Error: File '{self.file_name}' not found.")
            return -1
        except IOError:
            print(f"Error: Could not read from file '{self.file_name}'.")
            return -1

file_name = 'sample.txt'

word_counter = WordCounter(file_name)

word_count = word_counter.count_words()

if word_count != -1:
    print(f"Number of words in '{file_name}': {word_count}")
