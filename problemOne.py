class StringReverser:
    def __init__(self, input_string):
        self.input_string = input_string
    
    def reverse_string(self):
        return self.input_string[::-1]

input_str = "Hello"
reverser = StringReverser(input_str)
reversed_str = reverser.reverse_string()
print(f"Given String: {input_str}")
print(f"Reversed String: {reversed_str}")
