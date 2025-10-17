import time

# This function receives input from viginer_handler and performs encryption or decryption—it acts as the translator.
def viginer_cipher(message, key, enc_dec):
  

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_message = ''
    key_plus = 0

    for letter in message.lower():

        # The first component loops through the shift_message so that it continues throughout the entire message.
        shift_index_key = key[ key_plus % len(key)]
        
        # Use an if condition to check whether letter is in alphabet. If true, process it; otherwise, skip to the next iteration.
        if letter in alphabet.lower():

            # After looping the key, it's time to find the new letter's index.
            key_plus += 1
            num_index = alphabet.find(shift_index_key) 
            letter_index = alphabet.find(letter)
            new_letter_index = ((num_index *  enc_dec)  + letter_index) % len(alphabet)
            new_letter = alphabet[new_letter_index]
            new_message += new_letter

        # If the character isn't in the alphabet, check if it's a space. If so, append it as-is.
        elif letter == ' ':
            new_message += ' '

        # If neither of the previous conditions are met, it's most likely a punctuation mark or a number, so leave it unchanged.
        else:
            new_message += letter
 
    return new_message

# this function handle the user input and
def viginer_handler():

    # Obtain the message input for encryption or decryption.
    message = input('Write the message you want to encrypt')
    # Ensures the Message is alphabetic; if not, prints a message and stops the code.
    if not message.isalpha():
         print('the Message should be letters not numbers or something else.')
        # Now, if the user enters numbers, return will stop the code from running further.
         return
        
    
    # Two choices: 1 for encryption, 2 for decryption (using * -1). Otherwise, it does nothing but prints the message inside the else block.
    key_mess = input('Write the key for encryption or decryption.')

    # I used .lower() to make the key flexible—without it, the code would break if the user enters an uppercase letter.
    key_mess = key_mess.lower()

    

    # Ensures the key is alphabetic; if not, prints a message and stops the code.
    if not key_mess.isalpha():
        print('the Key Message should be letters not numbers or something else.')

        # Now, if the user enters numbers, return will stop the code from running further.
        return
    
    # this takes the user input.
    type_enc =  input('if you want to encrypt press 1, if you to decrypt press 2.')
    type_translation = str.maketrans({' ' : ''})
    type_translated = type_enc.translate(type_translation)

    # Checks if the string contains only digits.
    if type_translated.isdigit():

        # Converts type_translated to an integer and assigns it to the number variable.
        number = int(type_translated)
        if number == 1:
            direction =  1
        elif number == 2:
            direction = -1

        # If the user enters a number other than 1 or 2, it prints the following message.
        else:
            print('choose just 1 or 2.')
            return
        
    # If the user enters anything other than numbers, it prints the following message.
    else:
        print('Do not print letters or anything else, just digits(1 or 2).')
        return

    
    # This informs the user not to use numbers; if they do, they should choose letters instead.
    
    # To make it user-friendly, I decided to add some flair to the code for the user.
    print(f'your Message is {message} and your key message is {key_mess}. and you Numcryption is {type_enc}')
    time.sleep(2)
    print('Processing...')
    time.sleep(3)


    return f' The Result is {viginer_cipher(message, key_mess, direction)}'