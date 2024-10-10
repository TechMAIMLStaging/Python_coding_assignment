# 1. Find the second largest element in a list (without using max() function).
def find_second_largest(nums):
    largest = second_largest = float('-inf')
    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num

numbers = [10, 20, 4, 45, 99]
result = find_second_largest(numbers)
print("Second largest element:", result)

#=============================================================================================================#

# 2. Check if a number is prime.
def is_prime(n):
    if n <= 1:
        return False

number = 29
result = is_prime(number)
print(f"{number} is a prime number." if result else f"{number} is not a prime number.")

#------------------------------------------------------------------------------------------------------------------------------#

# 3. Reverse a string without using inbuilt functions.
def reverse_string(s):
    reversed_str = ''
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]
    return reversed_str

input_str = "Hello, World!"
result = reverse_string(input_str)
print("Reversed string:", result)

#===============================================================================================================================#

# 4. Merge two sorted arrays into a single sorted array without using any built-in sort methods.
def merge_sorted_arrays(arr1, arr2):
    i = j = 0
    merged_array = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1
    while i < len(arr1):
        merged_array.append(arr1[i])
        i += 1
    while j < len(arr2):
        merged_array.append(arr2[j])
        j += 1
    return merged_array

array1 = [1, 3, 5, 7]
array2 = [2, 4, 6, 8]
result = merge_sorted_arrays(array1, array2)
print("Merged sorted array:", result)

#=============================================================================================================#

# 5. Calculate the factorial of a number using recursion.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

number = 5
result = factorial(number)
print("Factorial of", number, "is", result)

#=============================================================================================================#

# 6. Find the largest contiguous subarray sum (Kadane’s Algorithm).
def max_subarray_sum(arr):
    max_current = max_global = arr[0]
    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        if max_current > max_global:
            max_global = max_current
    return max_global

array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_sum(array)
print("Largest contiguous subarray sum is", result)

#=============================================================================================================#

# 7. Check if a given string is a palindrome.
def is_palindrome(s):
    return s == s[::-1]

input_str = "racecar"
result = is_palindrome(input_str)
print(f"{input_str} is a palindrome." if result else f"{input_str} is not a palindrome.")

#=============================================================================================================#

# 8. Convert a decimal number to binary without using built-in functions.
def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary_str = ''
    while n > 0:
        binary_str = str(n % 2) + binary_str
        n //= 2
    return binary_str

decimal_number = 10
result = decimal_to_binary(decimal_number)
print("Binary of", decimal_number, "is", result)


#=============================================================================================================#

# 9. Find pairs in an array with a given sum.
def find_pairs_with_sum(arr, target_sum):
    pairs = []
    seen = set()
    for num in arr:
        complement = target_sum - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    return pairs

array = [1, 2, 3, 4, 5]
target_sum = 6
result = find_pairs_with_sum(array, target_sum)
print("Pairs with sum", target_sum, ":", result)

#=============================================================================================================#

# 10. Count the frequency of elements in a list.
def count_frequency(arr):
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    return frequency

array = [1, 2, 2, 3, 3, 3, 4]
result = count_frequency(array)
print("Frequency of elements:", result)

#=============================================================================================================#

# 11. Generate the first N numbers in the Fibonacci sequence using recursion.
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fibs = fibonacci(n - 1)
        fibs.append(fibs[-1] + fibs[-2])
        return fibs

N = 10
result = fibonacci(N)
print("First", N, "numbers in the Fibonacci sequence:", result)

#=============================================================================================================#

# 12. Remove duplicates from a list while preserving the order of elements.
def remove_duplicates(arr):
    seen = set()
    result = []
    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

array = [1, 2, 2, 3, 4, 4, 5]
result = remove_duplicates(array)
print("Array after removing duplicates:", result)

#=============================================================================================================#

# 13. Check if two strings are anagrams of each other.
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

string1 = "listen"
string2 = "silent"
result = are_anagrams(string1, string2)
print(f"{string1} and {string2} are anagrams." if result else f"{string1} and {string2} are not anagrams.")

#=============================================================================================================#

# 14. Count vowels and consonants in a string.
def count_vowels_and_consonants(s):
    vowels = "aeiouAEIOU"
    count_vowels = sum(1 for char in s if char in vowels)
    count_consonants = sum(1 for char in s if char.isalpha() and char not in vowels)
    return count_vowels, count_consonants

input_str = "Hello, World!"
vowels_count, consonants_count = count_vowels_and_consonants(input_str)
print("Vowels:", vowels_count, "Consonants:", consonants_count)

#=============================================================================================================#

# 15. Implement the binary search algorithm for a sorted list.
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

sorted_array = [1, 2, 3, 4, 5]
target_value = 3
result = binary_search(sorted_array, target_value)
print("Index of", target_value, "is", result)

#=============================================================================================================#

# 16. Check if a given list is sorted in ascending order.
def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

array = [1, 2, 3, 4, 5]
result = is_sorted(array)
print("List is sorted." if result else "List is not sorted.")

#=============================================================================================================#

# 17. Calculate the transpose of a matrix.
def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

matrix = [[1, 2, 3], [4, 5, 6]]
result = transpose_matrix(matrix)
print("Transpose of the matrix:", result)

#=============================================================================================================#

# 18. Find the sum of digits of a given number using recursion.
def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)

number = 12345
result = sum_of_digits(number)
print("Sum of digits of", number, "is", result)

#=============================================================================================================#

# 19. Find the intersection of two lists.
def intersection_of_lists(list1, list2):
    return list(set(list1) & set(list2))

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = intersection_of_lists(list1, list2)
print("Intersection of the lists:", result)

#=============================================================================================================#

# 20. Find all permutations of a string.
def permutations(s):
    if len(s) <= 1:
        return [s]
    perms = []
    for i, char in enumerate(s):
        for perm in permutations(s[:i] + s[i + 1:]):
            perms.append(char + perm)
    return perms

input_str = "abc"
result = permutations(input_str)
print("Permutations of", input_str, ":", result)
