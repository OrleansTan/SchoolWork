# a = [1, 2, 3, 4, 5, 6,]
# b = ["hi", "bye"]
#
# print(a)
#
# # list are an iterable datatype
#
# for element in a:
#     print (element)
#
# for element in b:
#     print (element)
#
# l = [4, "foo", 6, 8, "Tanner"]
#
# try
# recept
#
# for element in b:
#     print (f"things {element}")

empty_list = ["a"]
if empty_list:
    print("do thing 1")
    word = "hello"
    print(word)
    print(word[4])
    print(word[1])
else:
    print("tanner")

list_words = ["Stromlo", "Melrose", "Deakin", "Orana", "Mccillop"]

print (list_words[2:4])

for high_school in list_words:
    print(high_school)
    print(high_school[0])

for letter in "hello":
    print(letter)


my_list = list("aieou")
print("aieou")
print(my_list)

my_list_appended = my_list + ["y"]
print(my_list_appended)
my_list_appended.append ('A')
print(my_list_appended)
my_list_appended = my_list + ["y"]
print(my_list_appended)

my_list_appended.remove("i")
print(my_list_appended)


if "z" in my_list_appended:
    my_list_appended.remove("z")
else:
    print("z was never there ")

print(f"After pop!(): ")
