def getMessage():
    print('Enter Ciphertext')
    return input()

def getOutput():
    return input()

message = getMessage()
print('Output (y for yes, n for no)')
for key in range(1, 26):
    converted = ''
    for letter in message:
        if letter.isalpha():
            val = ord(letter)
            val -= key

            if letter.isupper():
                if val > ord('Z'):
                    val -= 26
                elif val < ord('A'):
                    val += 26
            elif letter.islower():
                if val > ord('z'):
                    val -= 26
                elif val < ord('a'):
                    val += 26
            converted += chr(val)
        else:
            converted += letter

    print('is it "%s"?' % (converted))
    output = getOutput()
    if output == 'y':
        exit(0)