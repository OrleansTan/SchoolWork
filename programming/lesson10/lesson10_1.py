
def restricted_division(numerator, denominator):
    if numerater == 17:
        raise ValueError("Error: Cruzy does not like 17. Choose another.")
    return numerator / denominator

try:
    dividend = int(input("Enter a dividend: "))
    divisor = int(input("enter a divisor: "))
    quotient = dividend / divisor

except ZeroDivisionError:
    print("Error:")
    sys.exit(1)

except ZeroDivisionError:
    print("Error:")
    sys.exit(1)
except Exception as e:
    print("Error: I dont know what happened!?")
    print(f"this is the error{e}")
else:
    print("Else block")
    print(f"{dividend}/{divisor} = {quotient}")
finally:
    print("Finally block!")
