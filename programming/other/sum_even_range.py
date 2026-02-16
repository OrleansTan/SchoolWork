# Write and submit a program, sum_even_range.py, which demonstrates the following:
# • Read two integers start and stop.
# • Compute the sum of even numbers in the inclusive range.
# • Use a for loop with range and an if condition inside the loop.
# • Handle cases where start > stop by swapping.
# • Print exactly one labelled line with the total.
# • Avoid using built-in sum on a comprehension for this task.
# • Keep the script under 40 lines.
# • Test with small, negative, and equal ranges.

start = int(input("Enter a start number: "))
stop = int(input("Enter a end number: "))
Even_sum = 0
tempint = 0
if start > stop:
    tempint = stop
    stop = start
    start = tempint
# if number i even add them up and print out the total
for number in range(start,stop,):
    if number % 2 == 0:
         print(f"{number} is an even number.")
         Even_sum = Even_sum + number
    # if start is greater then stop print the numbers backwards
    else:
        print(f"{number} is an odd number.")
print(f"total equals {Even_sum}")
