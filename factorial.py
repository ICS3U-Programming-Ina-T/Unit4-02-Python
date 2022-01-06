#!/usr/bin/env python3

# Created by: Ina Tolo
# Created on: Jan. 5, 2022
# This program asks the user for a whole number.
# It then calculates the factorial of that number.

def main():
    # initializations
    loop_counter = 0
    factorial_answer = 1

    # get the user number
    user_number_string = input("Enter a whole number: ")
    print("")

    try:
        # converts user input to integer
        user_number_int = int(user_number_string)

        if user_number_int >= 0:
            # replicates a do..while loop
            # calculate the factorial of the user number using a loop
            while True:
                loop_counter = loop_counter + 1
                factorial_answer = factorial_answer * loop_counter
                print("Tracking {0} times through loop.".format(loop_counter))
                if loop_counter >= user_number_int:
                    break

            # display answer to user
            print("")
            print("{}! = {}".
                  format(user_number_int, factorial_answer))
        else:
            print("Please enter a whole number!")
    except Exception:
        print("{} is invalid.". format(user_number_string))


if __name__ == "__main__":
    main()
