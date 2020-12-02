from collections import namedtuple
from dataclasses import dataclass
import re
import time


def count_valid_passwords_straight(filename):
    counter = 0
    for current_row in open(filename):
        min, remainder = current_row.split('-', 1)
        max, remainder = remainder.split(' ', 1)
        letter, password = remainder.split(': ', 1)
        if int(min) <= password.count(letter) <= int(max):
            counter += 1

    return counter


PasswordRow = namedtuple('PasswordRow', ['min', 'max', 'letter', 'password'])


def count_valid_passwords_regex(filename):
    counter = 0
    for current_row in open(filename):
        password_row = PasswordRow(*re.split('[-: ]{1,2}', current_row.strip()))
        if int(password_row.min) <= password_row.password.count(password_row.letter) <= int(password_row.max):
            counter += 1

    return counter


def count_valid_passwords_oneliner(filename):
    return len([pw for pw in (re.split('[-: ]{1,2}', row) for row in open(filename)) if int(pw[0]) <= pw[3].count(pw[2]) <= int(pw[1])])


straight_start = time.perf_counter_ns()
straight_count = count_valid_passwords_straight('passwords.txt')
straight_end = time.perf_counter_ns()
print('Valid passwords straight ({}ms): {}'.format((straight_end - straight_start) / 1000000, straight_count))

regex_start = time.perf_counter_ns()
regex_count = count_valid_passwords_regex('passwords.txt')
regex_end = time.perf_counter_ns()
print('Valid passwords regex ({}ms): {}'.format((regex_end - regex_start) / 1000000, regex_count))

oneliner_start = time.perf_counter_ns()
oneliner_count = count_valid_passwords_oneliner('passwords.txt')
oneliner_end = time.perf_counter_ns()
print('Valid passwords oneliner ({}ms): {}'.format((oneliner_end - oneliner_start) / 1000000, oneliner_count))
