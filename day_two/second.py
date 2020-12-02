def count_valid_passwords_straight(filename):
    counter = 0
    for current_row in open(filename):
        mi, tail = current_row.split('-', 1)
        ma, tail = tail.split(' ', 1)
        letter, password = tail.split(': ', 1)

        if (password[int(mi) - 1] == letter) ^ (password[int(ma) - 1] == letter):
            counter += 1

    return counter


print('Valid passwords: {}'.format(count_valid_passwords_straight('passwords.txt')))
