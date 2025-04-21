# lst=[i for i in range(1,21) if i % 2 == 0 ]
# print(lst)

# gravity_ratio_of_all_planets = {
#         "mercury": 37.6 / 100,
#         "venus": 88.9 / 100,
#         "mars": 37.8 / 100,
#         "jupiter": 236.0 / 100,
#         "saturn": 108.1 / 100,
#         "uranus": 81.5 / 100,
#         "neptune": 114.0 / 100
#     }

# lst=" ,".join([planet.capitalize() for planet in gravity_ratio_of_all_planets])
# print(lst)

# PRACTICE QUESTION OF LIST COMPREHENSION
# 1:Square of numbers:
# [1, 2, 3, 4, 5] list ka square list comprehension se banao.
# Output: [1, 4, 9, 16, 25]
square=[i **2 for i in range(1,6,1)]
print(square)

# 2:Even numbers:
# List mein se sirf even numbers nikaalo.
# [10, 15, 20, 25, 30] → [10, 20, 30]

num=[10 , 15 , 20 ,25 ,30]
even=[i for i in num if i%2 == 0]
print(even)

# 3:Convert to uppercase:
# List: ['apple', 'banana', 'cherry']
# Output: ['APPLE', 'BANANA', 'CHERRY']

fruits=['apple', 'banana', 'cherry']
upper=[fruit.upper() for fruit in fruits ]
print(upper)

# 4:Length of words:
# ['hello', 'world', 'python']
# Output: [5, 5, 6]
words=['hello', 'world', 'python']
length=[len(word) for word in words ]
print(length)

# 5:Numbers from 1 to 10 but only odd numbers:
# Output: [1, 3, 5, 7, 9]
odd_num=[i for i in range(1,11,1) if i%2 != 0]
print(odd_num)


# 🔁 Intermediate Level:
# 6:Squares of even numbers from 1 to 20:
# Output: [4, 16, 36, 64, ..., 400]

sqr_of_even=[i**2 for i in range(1,21,1) if i%2 == 0]
print(sqr_of_even)

# 7:List of first letters of each word:
# Input: ['Dog', 'Cat', 'Mouse']
# Output: ['D', 'C', 'M']
animals=['Dog', 'Cat', 'Mouse']
first_word=[animal[0] for animal in animals]
print(first_word)

# 8:Reverse each string:
# Input: ['apple', 'banana', 'cherry']
# Output: ['elppa', 'ananab', 'yrrehc']

my_fruits=['apple', 'banana', 'cherry']
reverse=[fruit[::-1] for fruit in my_fruits]
print(reverse)

# 9:Filter strings with length > 3:
# Input: ['hi', 'hello', 'ok', 'python']
# Output: ['hello', 'python']
my_words=['hi', 'hello', 'ok', 'python']
filter_words=[ele for ele in my_words if len(ele) > 3]
print(filter_words)

# 10:Create a list of tuples with number and its square from 1 to 5:
# Output: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

tuple_sqr=[(i,i**2) for i in range(1,6,1)]
print(tuple_sqr)

# 💡 Advanced Level:
# 11:Flatten a 2D list using list comprehension:
# Input: [[1,2],[3,4],[5,6]]
# Output: [1,2,3,4,5,6]

your_list=[[1,2],[3,4],[5,6]]
result=[i for item in your_list for i in item]
print(result)

# 12:Find all vowels in a string:
# Input: "hello world"
# Output: ['e', 'o', 'o']

vowels="aeiou"
sentence="hello world"

answer=[vov for vov in sentence if vov in vowels]
print(answer)

# 13:Create a list of numbers divisible by both 3 and 5 from 1 to 100
# Output: [15, 30, 45, 60, 75, 90]

divisible=[i for i in range(1,101,1) if i %3 == 0 and i % 5 == 0]
print(divisible)

# 14:Replace negative numbers with 0:
# Input: [2, -4, 5, -1, 0, -3]
# Output: [2, 0, 5, 0, 0, 0]
input_list= [2, -4, 5, -1, 0, -3]
rem_neg=[i if i > 0 else 0 for i in input_list]
print(rem_neg)
