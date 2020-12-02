from collections import namedtuple
import re
import timeit


def count_valid_passwords_straight(filename):
    counter = 0
    for current_row in open(filename):
        mi, tail = current_row.split('-', 1)
        ma, tail = tail.split(' ', 1)
        letter, password = tail.split(': ', 1)
        if int(mi) <= password.count(letter) <= int(ma):
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


def parse_pw_row(string):
    mi, tail = string.split('-', 1)
    ma, tail = tail.split(' ', 1)
    letter, password = tail.split(': ', 1)
    return mi, ma, letter, password


def is_valid_pw(pw):
    return int(pw[0]) <= pw[3].count(pw[2]) <= int(pw[1])


def count_valid_passwords_func(filename):
    return len(list(filter(is_valid_pw, map(parse_pw_row, open(filename)))))


timing_repetitions = 1000

straight_timing = timeit.Timer('count_valid_passwords_straight("passwords.txt")', globals=globals()).timeit(timing_repetitions)
straight_count = count_valid_passwords_straight('passwords.txt')
print('Using simple parsing')
print('Valid passwords: {}'.format(straight_count))
print('Benchmark for {} repetitions: {:.6}'.format(timing_repetitions, straight_timing))

regex_timing = timeit.Timer('count_valid_passwords_regex("passwords.txt")', globals=globals()).timeit(timing_repetitions)
regex_count = count_valid_passwords_regex('passwords.txt')
print('Using regex parsing')
print('Valid passwords: {}'.format(regex_count))
print('Benchmark for {} repetitions: {:.6}'.format(timing_repetitions, regex_timing))

oneliner_timing = timeit.Timer('count_valid_passwords_oneliner("passwords.txt")', globals=globals()).timeit(timing_repetitions)
oneliner_count = count_valid_passwords_oneliner('passwords.txt')
print('Using oneliner parsing')
print('Valid passwords: {}'.format(oneliner_count))
print('Benchmark for {} repetitions: {:.6}'.format(timing_repetitions, oneliner_timing))

func_timing = timeit.Timer('count_valid_passwords_func("passwords.txt")', globals=globals()).timeit(timing_repetitions)
func_count = count_valid_passwords_oneliner('passwords.txt')
print('Using func parsing')
print('Valid passwords: {}'.format(func_count))
print('Benchmark for {} repetitions: {:.6}'.format(timing_repetitions, func_timing))
