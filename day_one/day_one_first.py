def read_ints(filename):
    with open(filename) as file:
        return [int(row) for row in file]


def find_combo_linear():
    """ Tries to find the combination of two entries from the list with the sum 2020. O(n^2) complexity. """

    expenses = read_ints('data_first.txt')
    first_index = 0

    while first_index < len(expenses) - 1:
        first_value = expenses[first_index]

        for second_value in expenses[first_index + 1:]:
            if first_value + second_value == 2020:
                return first_value, second_value

        first_index += 1

    return None


def find_combo_log():
    """ Tries to find the combination of two entries from the list with the sum 2020. O(n log n) complexity. """

    expenses = sorted(read_ints('data_first.txt'))
    for index in range(len(expenses) - 1):
        combo = test_combo_log(expenses[index], index + 1, len(expenses) - 1, expenses)
        if combo is not None:
            return combo

    return None


def test_combo_log(first_value, start_index, end_index, expenses):

    test_index = start_index + int((end_index - start_index) / 2)
    second_value = expenses[test_index]
    combo_value = first_value + second_value

    if combo_value == 2020:
        return first_value, second_value

    elif combo_value > 2020 and start_index < test_index:
        return test_combo_log(first_value, start_index, test_index - 1, expenses)

    elif test_index < end_index:
        return test_combo_log(first_value, test_index + 1, end_index, expenses)

    return None


if __name__ == '__main__':

    combo = find_combo_linear()
    if combo is not None:
        print('Linear: The answer is {} * {} = {}'.format(combo[0], combo[1], combo[0] * combo[1]))

    combo2 = find_combo_log()
    if combo2 is not None:
        print('Logarithmic: The answer is {} * {} = {}'.format(combo2[0], combo2[1], combo2[0] * combo2[1]))

