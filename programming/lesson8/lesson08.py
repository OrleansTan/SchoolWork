# print("hw")
#
# # iterable
#
#
# for charaacter in "hello":
#     print(charaacter)
#
#
# d = {"tanner": 97.26, "sam": 99.99}
# for key in d:
#     print(key)
#
# for key in d.values():
#
# for key,values in d.item():
#     print(key)
#
# students = ["tanner", "zaki", "jai"]
#
# for number, student in enumerate(students):
#     print(f"student # {number} is {student}.")
#
#
# for num in range(0,11):
#     print(num**3, end =' ')
# print()

def only_even(iterable):
    for x in iterable:
        yield x **2


def squares(iterable):
    for x in iterable:
        if x % 2 == 0:
            yield x ** 2
# iterable is something that can be looped on.

def counter(start,stop):
    i - start
    while i <= stop:
        yield i
        i +=1

print("Grenerators")

pipeline = sqaures(only(counter(1,10)))

for v in pipeline:
    print(v, end=' ')
print()

pipeline = sqaures(only(counter(10,20)))
sqauresl = [0,1,4,9,15,25]
print(squaresl)
sqauresl = [i * i for i in range(10,20)]
print(squaresl)

sqauresl = [2 * i for i in range(10,21)]
print(squaresl)




# yield mean give me the number and hold the curent number untill told otherwise
# list1 = []
# numbers = input("Enter numbers: ")
# for list2 in list1:
#     print(list2)


#

