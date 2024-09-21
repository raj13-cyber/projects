print("printing current and previous number sum in a range(10)")

previous_num = 0

# iterate first 10 numbers

for i in range (1,11):
    new_value = previous_num+i
    print("current number",i, "previous number",previous_num, "sum: ", new_value)

    previous_num = i