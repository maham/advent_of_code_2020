import time


target_value = 2020


def read_ints(filename):
    with open(filename) as file:
        return [int(row) for row in file]


def find_combo_linear(expenses):
    """ Tries to find the combination of three numbers from the list with the sum target_value using linear searching.
        O(n^3) complexity. """

    while len(expenses):
        first_value = expenses.pop()

        for second_index, second_value in enumerate(expenses):
            current_total = first_value + second_value
            if current_total > target_value:
                continue

            diff = target_value - current_total
            if diff in expenses[second_index + 1:]:
                return first_value, second_value, diff

    return None


def find_combo_log(expenses):
    """ INSERT DESCRIPTION """

    while len(expenses):
        first_value = expenses.pop()

        for second_index, second_value in enumerate(expenses):
            current_total = first_value + second_value
            if current_total > target_value:
                continue

            diff = target_value - current_total
            if combo_find(diff, 0, len(expenses) - 1, expenses):
                return first_value, second_value, diff

    return None


def combo_find(value, start_index, end_index, expenses):
    middle_index = start_index + ((end_index - start_index) >> 1)
    middle_value = expenses[middle_index]

    if middle_value == value:
        return True

    elif value > middle_value and middle_index < end_index:
        return combo_find(value, middle_index + 1, end_index, expenses)

    elif start_index < middle_index:
        return combo_find(value, start_index, middle_index - 1, expenses)

    return False


if __name__ == '__main__':

    expenses = read_ints('expenses.txt')
    linear_start = time.perf_counter_ns()
    combo = find_combo_linear(expenses)
    linear_end = time.perf_counter_ns()
    if combo is not None:
        duration = (linear_end - linear_start) / 1000000
        product = combo[0] * combo[1] * combo[2]
        print('Linear({}ms): The answer is {} * {} * {} = {}'.format(duration, combo[0], combo[1], combo[2], product))

    expenses = sorted(read_ints('expenses.txt'))
    log_start = time.perf_counter_ns()
    combo2 = find_combo_log(expenses)
    log_end = time.perf_counter_ns()
    if combo2 is not None:
        duration = (log_end - log_start) / 1000000
        product = combo2[0] * combo2[1] * combo2[2]
        print('Log({}ms): The answer is {} * {} * {} = {}'.format(duration, combo2[0], combo2[1], combo2[2], product))
