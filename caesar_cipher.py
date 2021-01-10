ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
custom = '0123456789abcdefghijklmnopqrstuvwxyz!#$%&.?@'

password = 'HardPassword'
shift = 19


def decrypt(password, chars):
    print()
    print('Decryption:')
    decryption = ''
    temp = ''
    shift = len(chars)

    for i in range(1, shift):
        temp_alph = list(chars)
        for x in range(i):
            temp_alph.append(temp_alph[0])
            temp_alph.pop(0)
        shift -= 1

        for letter in password.lower():
            if letter == ' ':
                decryption += letter
            else:
                index = chars.index(letter)
                temp = temp_alph[index]
                decryption += temp
        print(f'{shift}: {decryption.title()}')
        decryption = ''


def encrypt(password, shift, chars):
    print(f'Password: {password}')
    print(f'Shift: {shift}')
    encryption = ''
    temp_alph = list(chars)

    for x in range(shift):
        temp_alph.append(temp_alph[0])
        temp_alph.pop(0)

    for letter in password.lower():
        if letter == ' ':
            encryption += letter
        else:
            index = chars.index(letter)
            temp = temp_alph[index]
            encryption += temp
    return encryption.title()


encryption = encrypt(password, shift, ALPHABET)
print(f'Encryption: {encryption}')
decrypt('M Pszi Gcfiv Wigyvmxc', ALPHABET)
