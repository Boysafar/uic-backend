
# 1. Use for, .split(), and if to create a Statement that will print out words that start with 's':

st = "Print only the words that start with s in this sentence"
words = st.split()

for word in words:
    if word[0].lower() == "s":
        print(word)


# 2. Use range() to print all the even numbers from 0 to 10.

for i in range(0,10):
    if i % 2 == 0:
        print(f"Juft sonlar {i}")


# 3. Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

divisible_by_3 = [num for num in range(1, 51) if num % 3 == 0]

# Natijani chop etish
print(divisible_by_3)


# 4. Go through the string below and if the length of a word is even print "even!"
str = "Print every word in this sentence that has an even number of letters"

words = str.split()

for word in words:
    # So'z uzunligini juftlikka tekshiramiz
    if len(word) % 2 == 0:
        print(f"{word}: even!")


# 5. Write a program that prints the integers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

for i in range(0, 100):
    if i % 15 == 0:
        print(f"{i}: FizzBuzz")
    elif i % 3 == 0:
        print(f"{i}: Fizz")
    elif i % 5 == 0:
        print(f"{i}: Buzz")
    else:
        print(i)

# 6. Use List Comprehension to create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'

# List Comprehension orqali har bir so'zning birinchi harfini olish
first_letters = [word[0] for word in st.split()]

print(first_letters)
