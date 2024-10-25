def encode(item_to_encode, shift_by, alphabet):
    print('Encoded:')
    encoded = ''                                     # set variable to hold encoded message
    
    for letter in item_to_encode:
        if letter.isalpha():                          # do the following if the letter is alphabetical, will not work for numbers or special characters
            lowercase_letter = letter.lower()         # normalize the letter so I only need to check on list of letters
            index = alphabet.index(lowercase_letter)  # look for the index of the letter to encode
            encoded_index = index + shift_by          # add the current index and the number to shift by together
            encoded_index = encoded_index % 26        # use modulo to make sure index stays in range 0-25
            encoded_letter = alphabet[encoded_index]  # get the new Letter
            encoded += encoded_letter.upper() if letter.isupper() else encoded_letter  # if uppercase add capital letter, if lower add lower
        else:                                         # If it is not a letter add it back
            encoded += letter

    return encoded

def decode(item_to_decode, shift_by, alphabet):
    print('Decoded:')
    decoded = ''

    for letter in item_to_decode:
        if letter.isalpha():                          # Only letters
            lowercase_letter = letter.lower()         # normalize the letter
            index = alphabet.index(lowercase_letter)  # look for the index of the letter to decode
            decoded_index = index - shift_by          # subtract the current index and the number to shift by together
            decoded_index = decoded_index % 26        # use modulo to make sure index stays in range 0-25
            decoded_letter = alphabet[decoded_index]  # get the new Letter
            decoded += decoded_letter.upper() if letter.isupper() else decoded_letter  # Add proper case and letter
        else:                                         # If it is not a letter add it back
            decoded += letter

    return decoded

def main():                   # main function
    encode_decrypt = input('Encode = y, Decode = n, input y or n: ') # ask are we encoding or decoding
    item_to_encode = ''       # set variable accessible in main function for encode/decode item
    shift_by = 0              # set variable for nuber to encode/decode by
    # below is my alphabet list to use the index and to encode and decode the list, probably could have used a string too.
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
                      

    if encode_decrypt == 'y':                                       # if encode == y then encode
        item_to_encode = input('item to encode: ')                  # set item to encode to user input
        shift_by = int(input('Number to encode by: '))              # set number to shift by to user input
        item_to_encode = encode(item_to_encode, shift_by, alphabet)  # Run the encode function
    elif encode_decrypt == 'n':
        item_to_encode = input('item to decode: ')                  # same info but reverse
        shift_by = int(input('Number to decode by: '))              # number to decode by
        item_to_encode = decode(item_to_encode, shift_by, alphabet) # run the decode function
    else:
        print('Please put a valid answer, y or n')  # if user enters some other value than y or n for encode/decode print this

    print(item_to_encode) # print returned value for encoded or decoded item
    


if __name__ == "__main__":  # run the main function
    main()





