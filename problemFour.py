class DictionarySorter:
    def __init__(self, input_dict):
        # Initialize the DictionarySorter object with an input dictionary.
        self.input_dict = input_dict
    
    def sort_dict_by_values(self):
        # Sort the dictionary by values in ascending order.
        sorted_dict = {key: value for key, value in sorted(self.input_dict.items(), key=lambda item: item[1])}
        return sorted_dict

# Example usage
input_dict1 = {'a': 5, 'b': 2, 'c': 3, 'd': 8}

# Create an instance of DictionarySorter with the input dictionary
dict_sorter1 = DictionarySorter(input_dict1)

# Call the sort_dict_by_values method to get the sorted dictionary
sorted_dict1 = dict_sorter1.sort_dict_by_values()

# Print the original and sorted dictionaries
print("Given Dictionary 1:", input_dict1)
print("Sorted Dictionary 1 by Values:", sorted_dict1)

# Example usage
input_dict2 = {'x': 10, 'y': 7, 'z': 1, 'w': 4}

# Create another instance of DictionarySorter with a different input dictionary
dict_sorter2 = DictionarySorter(input_dict2)

# Call the sort_dict_by_values method to get the sorted dictionary
sorted_dict2 = dict_sorter2.sort_dict_by_values()

# Print the original and sorted dictionaries
print("\nGiven Dictionary 2:", input_dict2)
print("Sorted Dictionary 2 by Values:", sorted_dict2)
