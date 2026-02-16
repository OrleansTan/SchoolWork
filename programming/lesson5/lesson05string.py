#
# def normalize(name):
#     name = name.strip()
#
#     name = name.capitalize()
#     return name

name = input("Enter name: ")


name = normalize(name)

name = name.title()

name_split = name.split()
print(name_split)

fname = name_split[0]
lname = name_split[1]
print(f"First name: {fname}")
print(f"Last name: {lname}")

print (f"wellcome to the world,{name}")

if fname.isalpha():
    print("the first name is entirely letters ")
else:
    print("there are some non-letter characters in the first name ")

if fname == "Tanner" and lname == "Two":
    print ("your are in the main frame ")
else:
    print("you are in the new world ")
