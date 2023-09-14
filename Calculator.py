while True:

    while True:

        try:

            first_number = float(input("enter first number: "))
            break

        except ValueError:
            print("invalid input. please enter a numeric value")

    while True:

        try:

            operation = input("enter operation number: ")

            if operation in ("+", "-", "*", "/", "**", "//", "%"):
                break

            else:
                raise ValueError

        except ValueError:
            print("invalid input. please enter +,  -,  *,  /,  **,  //,  %")

    while True:

        try:

            second_number = float(input("enter second number: "))

            if second_number == 0 and operation in ("/", "//"):
                raise ZeroDivisionError

            break

        except ZeroDivisionError:
            print("cannot divide by zero, please enter another numeric value")

    if operation == "+":
        result = first_number + second_number

    elif operation == "-":
        result = first_number - second_number

    elif operation == "*":
        result = first_number * second_number

    elif operation == "/":
        result = first_number / second_number

    elif operation == "**":
        result = first_number**second_number

    elif operation == "//":
        result = first_number // second_number

    elif operation == "%":
        result = first_number % second_number

    else:
        result = None

    if result != None:
        print(f"Result is: {result}")

    else:
        print("unexpected error")

    while True:

        try:

            repeat = input("Do you want to perform another operation (y/n): ")

            if repeat in ("y", "Y", "n", "N"):
                break

            else:
                raise ValueError

        except ValueError:
            print("invalid input. please enter y, n")

    if repeat in ("n", "N"):
        print("We hope we have made you happy")
        input("Press any key")

        break
