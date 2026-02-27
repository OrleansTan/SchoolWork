# with open("first.txt", "r") as f:
#     f.read("Tanner \n" )
#
# with open("surname.txt", "r") as f:
#     f.read("TWo \n")
#
# with open("output.txt,", "a") as f:
#     f.write

with open("first.txt", "r") as f:
    first = f.read().strip()

    with open("surname.txt", "r") as f:
     surname = f.read().strip()

     with open("fullname.txt", "w") as h:
        fullname = f"{first} {surname}"
        print(fullname)
        h.write(f"{fullname}\n")





