l = [1, 2, 3]
l =[[1],[2,3]]

print(f"Before append: {l}")
l.append([2,3])
print(f"After append: {l}")
print(f"Lenght of l: {len(l)}")
print(l[0])
l[0].append(5)
print(f"After append: {l}")
print(f"The first element of the first lsit: {l[1][1]}")

print(l)

for inner_list in l:
    for number in inner_list:
        print(number)


def locate(character, gameboard):


for row in gameboard:
    for cell in row:
        ptint(cell, end =' ')
    print()


gameboard = [
    ["."] * 10,
    ["."] * 10,
    ["."] * 10,
    ["."] * 10,
    ["."] * 10
]

pc = 'x'
gameboard[0][5] = pc

enemy = "$"
gameboard[4][5] = enemy
print("start of game")
for row in gameboard:
    print("".join(row))





students_with_score = {
    "Tanner": 64.0
    "sam": 75.2
    "zaki": 88.0
    'jai': 91.8
  }
d2 =   {
     "Tanner": "Maths"
    "sam": "IT"
    "zaki": "Eng"
    'jai': "Rust shards making class what a nerd for real"


    }
for s
