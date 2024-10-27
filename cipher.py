def encode(item_to_encode, shift_by, alphabet):
    encoded = ''
    for letter in item_to_encode:
        if letter.isalpha():
            lowercase_letter = letter.lower()
            index = alphabet.index(lowercase_letter)
            encoded_index = (index + shift_by) % 26
            encoded_letter = alphabet[encoded_index]
            # encoded += encoded_letter.upper() if letter.isupper() else encoded_letter
            encoded += encoded_letter
        else:
            encoded += letter
    return encoded

def main():                                     # alternate main to pass unit tests
    alphabet = 'abcdefghijklmnopqrstuvwxyz'     # alphabet to use for indexes
    item_to_encode = input()                    # input Item to encode
    shift_by = 5                                # preset amount to shift by
    encoded_message = encode(item_to_encode, shift_by, alphabet)    # run the encode function and return results
    print(encoded_message)                      # print results

if __name__ == "__main__":  # run the main function
    main()





