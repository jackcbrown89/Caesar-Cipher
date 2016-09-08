#JACK'S ENCRYPTION

MAX_KEY_SIZE = 26

def getMode():
    while True:
        print('Please select mode: encryption (e) or decryption (d)')
        mode = input().lower()
        if mode == 'e':
            return mode
        elif mode == 'd':
            return mode
        else:
            print('Please enter "e" to encrypt or "d" to decrypt')


def getMessage():
    print("What's the message?")
    return input()

def getKey():
    key = 0
    while True:
        print('Enter the shift (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key


def getNewMsg(mode, message, key):
    if mode == 'd':
        key = -key
    translated =""

    for char in message:
        if char.isalpha():
            num = ord(char)
            num += key

        if char.isupper():
            if num > ord('Z'):
                num -= 26
            elif num < ord('A'):
                num += 26
        elif char.islower():
            if num > ord('z'):
                num -= 26
            elif num < ord('a'):
                num += 26

            translated += chr(num)
        else:
            translated += char
    return translated

mode = getMode()
message  = getMessage()
key = getKey()

print('Your new message is: ')
print(getNewMsg(mode, message, key))
    
        
