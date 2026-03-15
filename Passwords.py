import secrets
import argparse
import string
import sys

def load_common_passwords(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read().splitlines()

def generate_password(n, lines, alphabet):
    code1 = code2 = code3 = code4 = 1
    code5 = 0
    temp_password = ''.join(secrets.choice(alphabet) for _ in range(n))
    
    for char in temp_password:
        if char in string.ascii_lowercase: code1 = 0
        elif char in string.ascii_uppercase: code2 = 0
        elif char in string.digits: code3 = 0
        elif char in string.punctuation: code4 = 0

    for line in lines:
        if line in temp_password: code5 = 1; break
    if code1 == code2 == code3 == code4 == code5 == 0:
        return temp_password
    else:
        return generate_password(n, lines, alphabet)

def main():
    parser = argparse.ArgumentParser(prog='Passwords.py', description='Генерация паролей')
    parser.add_argument('-l', '--length', type=int, default=16, help='Длина генерируемого пароля')
    parser.add_argument('-c', '--count', type=int, default=1, help='Число генерируемых паролей')
    parser.add_argument('-w', '--write', type=str, default='', help='Куда записать')
    parser.add_argument('-d', '--dictionary', type=str, default='10-char-common-passwords.txt', help='Кастомный словарь для проверки')
    argc = parser.parse_args()
    if argc.length < 4: print('Ошибка: Минимальная длина паролей - 4 символа'); sys.exit()
    if argc.count < 1: print('Ошибка: Минимальное количество генерируемых паролей - 1'); sys.exit()

    lines = load_common_passwords(argc.dictionary)

    alphabet = string.ascii_letters + string.digits + string.punctuation
    passwords_list = [generate_password(argc.length, lines, alphabet) for _ in range(argc.count)]
    if argc.write == '':
        print('\n'.join(passwords_list))
    else:
        with open(argc.write, 'w') as f:
            f.write('\n'.join(passwords_list))

if __name__ == '__main__':
    main()