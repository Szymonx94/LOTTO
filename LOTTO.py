import random


def new_number():
    """
    Function choose number
    :return: new number user
    """
    while True:
        try:
            result = int(input("Choose the number: "))
            break
        except ValueError:
            print("It's not number")
    return result


def new_numbers():
    """
    New get 6 different numbers between 1 and 49.
    :return: list new 6 numbers
    """
    result = []
    while len(result) < 6:

        number = new_number()
        if number not in result and 0 < number <= 49:
            result.append(number)
        elif number in result:
            print('It is the same number')
    return result


def sorted_numbers(numbers):
    """ Sorted new numbers
    :param numbers:
    :return: print sorted numbers
    """
    print(" ".join(str(number) for number in sorted(numbers)))


def random_numbers():
    """
    6 random numbers
    :param
    :return: New random numbers
    """
    numbers = list(range(1, 50))
    random.shuffle(numbers)
    return numbers[:6]


def lotto():
    """
    Main fuction lotto
    :return: result lotto
    """
    user = new_numbers()
    print("Your numbers: ")
    sorted_numbers(user)

    drawing_of_numbers = random_numbers()
    print("Lotto numbers: ")
    sorted_numbers(drawing_of_numbers)

    hits = 0

    for number in user:
        if number in drawing_of_numbers:
            hits += 1

    print(f"You hit {hits} {'number' if hits == 1 else 'numbers'}!")



if __name__ == '__main__':
    lotto()
