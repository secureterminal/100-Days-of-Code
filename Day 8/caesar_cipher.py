def new_index(old_index, shift, direction):
    if direction == 'encode':
        temp_index = old_index + shift
        if temp_index > 25:
            while temp_index > 25:
                temp_index -= 26
        return temp_index
    else:
        temp_index = old_index - shift
        if temp_index < 0:
            while temp_index < 0:
                temp_index += 26
        return temp_index



def ceasar(text, shift, direction):
    final = ''
    for str in text:
        if str not in alphabet:
            final += str
        else:
            new_str = alphabet[new_index(alphabet.index(str), shift, direction)]
            final += new_str
    return final


def game_over():
    end_game = input('Do you want to continue playing? Type "Y" for "Yes" and "N" for "NO" \n').lower()
    if end_game == 'y':
        return True
    else:
        print('Goodbye...')
        return False

continue_game = True

while continue_game == True:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    if (direction == 'encode') | (direction == 'decode'):
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        print(f'The {direction}d text is  {ceasar(text, shift, direction)}')
    else:
        print(f'Your input, "{direction}" is invalid, can\'t you read the instructions?')
        
    continue_game = game_over()
    
 