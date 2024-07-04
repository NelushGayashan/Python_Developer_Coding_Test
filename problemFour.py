class DictionarySorter:
    def __init__(self, input_dict):
        self.input_dict = input_dict
    
    def sort_dict_by_values(self):
        sorted_dict = {key: value for key, value in sorted(self.input_dict.items(), key=lambda item: item[1])}
        return sorted_dict

input_dict = {'a': 5, 'b': 2, 'c': 3, 'd': 8}

dict_sorter = DictionarySorter(input_dict)

sorted_dict = dict_sorter.sort_dict_by_values()

print("Given Dictionary:", input_dict)
print("Sorted Dictionary by Values:", sorted_dict)
