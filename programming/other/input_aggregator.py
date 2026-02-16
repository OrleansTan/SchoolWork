#
# Write and submit a program, input_aggregator.py, which demonstrates the following:
# • Use a sentinel-driven while loop to read integers until stop.
# • Ignore blank lines and reject non-integers with a message.
# • Track count, sum, min, and max as inputs arrive.
# • If no valid numbers were entered, print No data.
# • Otherwise print count, sum, min, max on separate labelled lines.
# •Ensure the loop terminates when the user types stop.
# • Keep the script under 70 lines.
# • Test with empty input, one value, and several values.


def getUserInput():
    tempstr = ""
    tempstr = str(input("Enter data: "))
    #tempstr = tempstr.lower()
    return tempstr.lower()

def main():
    userInput = ""
    DataList =[]
    while userInput != "stop":
        userInput = getUserInput()
        if userInput != "":
            try:
                userInt = int(userInput)

                DataList.append(userInt)
            except:
                print ("...a message...")
        else:
            print("No data")
    if len(DataList)!= 0:
        print(f"max {max(DataList)}")
        print(f"min {min(DataList)}")
        print(f"sum {sum(DataList)}")
        print(f"count {len(DataList)}")
    else:
        print("There Really was no data.")

if __name__ == "__main__":
    main()
