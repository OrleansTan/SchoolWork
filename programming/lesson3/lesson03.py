# # a = 1 + 2
# # b = 5 % 3
# #
# # print ('fb = {b}')
#
# # The year must be evenly divisible by 4 (e.g., 2024, 2028).
# # If the year is also divisible by 100, it is NOT a leap year (e.g., 1700, 1800, 1900).
# # If the year is divisible by 400, it IS a leap year (e.g., 1600, 2000, 2400
# x = int(input("enter a year: "))
# is_leapyear = False
# if x % 4 == 0 or x % 100 !=0 and x % 400 == 0:
#     is_leapyear = True
#     # if x % 100 == 0:
#     #     is_leapyear = False
#     # if x % 400 == 0:
#     #     is_leapyear = True
# else:
#     is_leapyear = False
# if x == False:
#     print ("false ")
# else:
#     print("leap year ")

x = int(input("enter a year: "))
is_leapyear = False
if x % 4 == 0:
    if x % 100 == 0 and x % 400 == 0:
        print("leap")
    else:
        print("not leap")
else:
    print("not leap")

