class EvenNumberSquared:
    def __init__(self, nums):
        self.nums = nums
    
    def squares_of_even_numbers(self):
        return [num ** 2 for num in self.nums if num % 2 == 0]

# Example usage:
nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums2 = [-2, -1, 0, 1, 2, 3, 4, 5, 6]

# Creating instances of EvenNumberSquared
even_squared1 = EvenNumberSquared(nums1)
even_squared2 = EvenNumberSquared(nums2)

# Calling squares_of_even_numbers method
result1 = even_squared1.squares_of_even_numbers()
result2 = even_squared2.squares_of_even_numbers()

# Printing results
print("Given List:", nums1)
print("Squares of Even Numbers:", result1)
print()
print("Given List:", nums2)
print("Squares of Even Numbers:", result2)
