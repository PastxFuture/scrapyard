# Python program to implement Morse Code Translator
 
'''
VARIABLE KEY
'cipher' -> 'stores the morse translated form of the english string'
'decipher' -> 'stores the english translated form of the morse string'
'message' -> 'stores the string to be encoded or decoded'
'''
 
# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', ' ':'.....'}

def encrypt(message):
    cipher = ''

    for letter in message:
        # dictionary.get(keyname, value)
        # Required. The keyname of the item you want to return the value from
        # Optional. A value to return if the specified key does not exist.
        cipher += MORSE_CODE_DICT.get(letter, ' ')

    return cipher

def decrypt(message):

 # Encrypt Morsecode

    decipher = '' 

    # Swap key/values in d:
    d_encrypt = dict([(v, k) for k, v in MORSE_CODE_DICT.items()])

    #if message.startswith('.') or message.startswith('−'):

    # Morse code is separated by empty space chars
    message = message.split(' ')

    for letter in message:
        decipher += d_encrypt.get(letter, ' ')

    return decipher.title()


# Hard-coded driver function to run the program
def main():
    message = 'Hello World'
    message1 = '.... . .-.. .-.. --- ..... .-- --- .-. .-.. -..'
    result = encrypt(message.upper())
    result1 = decrypt(message1)
    print(result)
    print(result1)

# Executes the main function
if __name__ == '__main__':
    main()