from collections import namedtuple


def count_valid_passwords_straight(filename):
    counter = 0
    for current_row in open(filename):
        min, tail = current_row.split('-', 1)
        max, tail = tail.split(' ', 1)
        letter, password = tail.split(': ', 1)

        if (password[int(min) - 1] == letter) ^ (password[int(max) - 1] == letter):
            counter += 1

    return counter


print('Valid passwords: {}'.format(count_valid_passwords_straight('passwords.txt')))
