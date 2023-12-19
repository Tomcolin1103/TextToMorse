import sys

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', ' ': '/', '!': '/-.-.--'}


def encrypt(message):
    text_to_return = ''

    for i in range(0, len(message)):
        text_to_return += MORSE_CODE_DICT[message[i].upper()]

    return text_to_return


def decrypt(message):
    message = message.split(' ')
    text_to_return = ''

    for i in range(0, len(message)):
        for key, value in MORSE_CODE_DICT.items():
            if message[i] == value:
                text_to_return += key

    return text_to_return


if sys.argv[1] == 'decrypt':
    print(decrypt(sys.argv[2]))

if sys.argv[1] == 'encrypt':
    print(encrypt(sys.argv[2]))


