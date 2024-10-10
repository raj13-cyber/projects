# Create a function that will take two numbers as parameters
# Next, Inside a function, multiply two numbers and save their product in a product variable
# Next, use the if condition to check if the product >1000. If yes, return the product
# Otherwise, use the else block to calculate the sum of two numbers and return it

def calculation(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
      return  num1 + num2
    
# first condition
result = calculation(100, 30)
print("The result is", result)


# Write a Python code to iterate the first 10 numbers, and in each iteration, 
# print the sum of the current and previous number.

print("printing current and previous number sum in a range(10)")

previous_num = 0

# iterate first 10 numbers

for i in range (1,11):
    new_value = previous_num+i
    print("current number",i, "previous number",previous_num, "sum: ", new_value)

    previous_num = i



# Write a Python code to accept a string from the user and display characters present at an even index number.

word = input('Enter a word ')
print("orginal String is", word)

size = len(word)

print("Printing only even index chars")

for i in range(0, size -1, 2):
    print(word[i])


# Write a Python code to remove characters from a string from 0 to n and return a new string.

def remove_characters(word, n):
    print ("The actual word is",word)
    x = word[n:]
    return x

print(remove_characters("rajendiran",5))


# Write a Python code to remove characters from a string from 0 to n and return a new string.

def value_check(numberlist):
    print("given value is: ", numberlist)

    first_num = numberlist[0]
    last_num = numberlist[-1]

    if first_num == last_num:
        return True
    else:
        return False
     

numbers_x = [10, 20, 30, 40, 10]
print("The result is", value_check(numbers_x))

numbers_y = [70, 65, 35, 75, 50]
print("The result is", value_check(numbers_y))
