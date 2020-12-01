def read_ints(filename):
    with open(filename) as file:
        return [int(row) for row in file]


def find_combo_linear():
    """ Tries to find the combination of three numbers from the list with the sum 2020 using linear searching.
        O(n^3) complexity. """

    expenses = read_ints('data_first.txt')

    first_index = 0

    while first_index < len(expenses) - 1:
        first_value = expenses[first_index]
        second_index = first_index + 1

        while second_index < len(expenses) - 1:
            second_value = expenses[second_index]

            for third_value in expenses[second_index + 1:]:
                if first_value + second_value + third_value == 2020:
                    return first_value, second_value, third_value

            second_index += 1

        first_index += 1

    return None


def find_combo_log():
    expenses = sorted(read_ints('data_first.txt'))

    first_index = 0

    while first_index < len(expenses) - 1:
        first_value = expenses[first_index]
        second_index = first_index + 1

        while second_index < len(expenses) - 1:
            second_value = expenses[second_index]

            combo = test_combo_log(first_value, second_value, second_index + 1, len(expenses) - 1, expenses)
            if combo is not None:
                return combo

            second_index += 1

        first_index += 1

    return None


def test_combo_log(first_value, second_value, start_index, end_index, expenses):

    test_index = start_index + int((end_index - start_index) / 2)
    third_value = expenses[test_index]
    combo_value = first_value + second_value + third_value

    if combo_value == 2020:
        return first_value, second_value, third_value

    elif combo_value > 2020 and start_index < test_index:
        return test_combo_log(first_value, second_value, start_index, test_index - 1, expenses)

    elif test_index < end_index:
        return test_combo_log(first_value, second_value, test_index + 1, end_index, expenses)

    return None


if __name__ == '__main__':

    combo = find_combo_linear()
    if combo is not None:
        product = combo[0] * combo[1] * combo[2]
        print('Linear: The answer is {} * {} * {} = {}'.format(combo[0], combo[1], combo[2], product))

    combo2 = find_combo_log()
    if combo2 is not None:
        product = combo2[0] * combo2[1] * combo2[2]
        print('Linear: The answer is {} * {} * {} = {}'.format(combo2[0], combo2[1], combo2[2], product))
