while True:
    try:
        num = int(input("Enter a number plz: "))
        if num >= 0:
            print("Tanner")
        else:
            print("Sam")
            sys.exit(1)
            break
    except:
        print("your lost")

