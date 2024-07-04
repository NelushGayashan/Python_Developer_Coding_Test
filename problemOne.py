class StringReverser:
    def __init__(self, input_string):
        #Initialize the StringReverser with an input string.
        self.input_string = input_string
    
    def reverse_string(self):
        #Reverse the input string.
        
        return self.input_string[::-1]

# Define the input string
input_str = "Hello"

# Create an instance of StringReverser with the input string
reverser = StringReverser(input_str)

# Call the reverse_string method to get the reversed string
reversed_str = reverser.reverse_string()

# Print the original and reversed strings
print(f"Given String: {input_str}")
print(f"Reversed String: {reversed_str}")
