def exception_handler():
    bill = 0
    while True:
        user_input = input("Enter your amount or enter \"q\" to exit\n")
        if user_input == "q":
            break
        else:
            try:
                user_input = int(user_input)
                bill = bill + user_input
                print("Your bill till now is {}".format(bill))
            except Exception as e:
                print("Your input resulted in an error: {}".format(e))


if __name__ == "__main__":
    exception_handler()
