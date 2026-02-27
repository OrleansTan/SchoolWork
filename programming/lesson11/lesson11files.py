with open("output.txt", "w") as f:
    f.write("Hello, yourself, \n")

with open("output.txt", "a") as f:
    f.write("Hello, yourself,\n")

with open("output.txt", "r") as f:
    # input_text = f.read()
#
#     print(input_text)
#     print(len(input_text))
#
#     if "General" in input_text
#         print("Yeah, General is in there.")
#
#     print(split_lines)
#     print(len(split_lines))
#
#     input_text = f.readline()
#


    for index,line in enumerate(f.readlines(), start = 1):
        if "General" in line:
            print(index, line)
