
# Write and submit a program, grade_band.py, which demonstrates the following:
# • Read a numeric score from input as float.
# • Print band: HD, D, C, P, or F according to provided cutoffs.
# • Use if/elif/else with clear, non-overlapping ranges.
# scores message.1 ty
# • Reject scores outside 0..100 with an error message.
# • Ensure each output ends with a newline.
# • Keep the script under 45 lines.
# • Test with boundary values at each cutoff.
# • Use descriptive variable names.


def getscore():

    enterscore = 101.0
    while enterscore  > 100.0 or enterscore <0.0:
        enterscore = float(input("Enter a grade between 0 and 100 (for the student X): "))
        if enterscore  > 100.0 or enterscore <0.0:
            print(f"Grade entered is not allowed ({enterscore})")
    return enterscore

def getgrade(sScore):
    if sScore > 85.0:
        return "HD"
    elif sScore > 75.0:
        return "D"
    elif sScore > 65.0:
        return "C"
    elif sScore >= 50.0:
        return "P"
    else:
        return "F"


def main():
   studentscore =  getscore()
   studentgrade =  getgrade(studentscore)
   print(f"{studentgrade}")


if __name__ == "__main__":
    main()
