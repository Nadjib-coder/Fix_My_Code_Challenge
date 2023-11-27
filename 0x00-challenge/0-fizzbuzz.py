#!/usr/bin/python3
"""
fizzbuzz task
"""
import sys


def fizzbuzz(n):
    """
    a function that prints numbers from 1 to n separated by a space.

    - for multiples of three print "Fizz"
    and for multiples of five print "Buzz".
    - for numbers which are multiples of both three and five print "FizzBuzz"
    """
    if c < 1:
        return

    tmp_result = []
    for x in range(1, c + 1):
        if (x % 3) == 0 and (x % 5) == 0:
            tmp_result.append("FizzBuzz")
        elif (x % 3) == 0:
            tmp_result.append("Fizz")
        elif (x % 5) == 0:
            tmp_result.append("Buzz")
        else:
            tmp_result.append(str(x))
    print(" ".join(tmp_result))


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    number = int(sys.argv[1])
    fizzbuzz(number)
