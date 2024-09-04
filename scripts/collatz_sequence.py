#! python3
# collatz_sequence.py takes an input from user and print the collatz-sequence for it

def collatz(number: int) ->int:
    result = None
    if number % 2 == 0:
        result = number // 2
    else:
        result = number * 3 + 1

    print(result)
    return result


def main():
    number = None
    while True:
        print('Enter a positive integer')
        try:
            number = int(input())
            if number > 0:
                break
            else:
                continue
        except ValueError:
            continue

    while number != 1:
        number = collatz(number)


main()
