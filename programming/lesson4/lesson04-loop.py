# Startnumber = 0
# while Startnumber <= 6:
#     print(Startnumber)
#     Startnumber += 1

# for i in range(1,100,4):
#      print(i)

print(" first loop ")
print("second loop ")
upper_bound = 25
for dishwasher in range(1, upper_bound):
    print(dishwasher)

print('second for loop')
total = 0
list_of_numbers = [1,2,3,4,5,6,100]
for jellybeen in list_of_numbers:
    print(jellybeen)
    total = total + jellybeen
print(f"total: {total}")

print('second for loop')
print("5 is the sentinel ")
print("when we get to 5, we stop the loop!")
total = 0
list_of_numbers = [1,2,3,4,5,6,100]
for jellybeen in list_of_numbers:
   if jellybeen == 5:
      break
  print(jellybeen)
