#!/usr/bin/env python3

# Created by: Michael Clermont
# Created on: May 2022
# This program is gets the smallest number in an array

import random


def smallest_number_array(array):
    # this function is gets the smallest number in an array

    small_number = array[1]
    for counter in array:
        maxi = counter
        if small_number > maxi:
            small_number = maxi

    return small_number


def main():
    # this function uses a list

    random_numbers = []
    smallest_number = 0

    # input
    print("The numbers are: ")
    for loop_counter in range(0, 10):
        a_single_number = random.randint(0, 100)
        random_numbers.append(a_single_number)
        print("{0}, ".format(a_single_number), end="")
    print("")

    smallest_number = smallest_number_array(random_numbers)

    print("The smallest number generated is: {0} ".format(smallest_number))
    print("\nDone.")


if __name__ == "__main__":
    main()
