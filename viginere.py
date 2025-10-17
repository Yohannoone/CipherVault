import time

#the encryption section
def encrypt(message, key):
  
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_message = ''
    key_plus = 0

    for letter in message.lower():

        # The first component loops through the shift_message so that it continues throughout the entire message.
        shift_index_key = key[ key_plus % len(key)]
        
        # Use an if condition to check whether letter is in alphabet. If true, process it; otherwise, skip to the next iteration.
        if letter in alphabet:

            # After looping the key, it's time to find the new letter's index.
            key_plus += 1
            num_index = alphabet.find(shift_index_key) 
            letter_index = alphabet.find(letter)
            new_letter_index = (num_index + letter_index) % len(alphabet)
            new_letter = alphabet[new_letter_index]
            new_message += new_letter

        # If the character isn't in the alphabet, check if it's a space. If so, append it as-is.
        elif letter == ' ':
            new_message += ' '

        # If neither of the previous conditions are met, it's most likely a punctuation mark or a number, so leave it unchanged.
        else:
            new_message += letter
 
    return new_message

#the handler of encryption section
def encryption_handler():

    # Obtain the message input for encryption or decryption.
    message = input('Write the message you want to encrypt.')
    # Ensures the Message is alphabetic; if not, prints a message and stops the code.
    if not message.replace(" ", "").isalpha():
        print('The message should only contain letters and spaces.')
        return
        # Now, if the user enters numbers, return will stop the code from running further.
         
        
    # Two choices: 1 for encryption, 2 for decryption (using * -1). Otherwise, it does nothing but prints the message inside the else block.
    key_mess = input('Write the key for encryption.')

    # I used .lower() to make the key flexible—without it, the code would break if the user enters an uppercase letter.
    key_mess = key_mess.lower()

    # Ensures the key is alphabetic; if not, prints a message and stops the code.
    if not key_mess.isalpha():
        print('the Key Message should be letters not numbers or something else.')

        # Now, if the user enters numbers, return will stop the code from running further.
        return
    


    
    
    # To make it user-friendly, I decided to add some flair to the code for the user.
    print(f'your Message is {message} and your key message is {key_mess}.')
    time.sleep(2)
    print('Processing...')
    time.sleep(3)

    print (f'The Result is {encrypt(message, key_mess)}')
    return f' The Result is {encrypt(message, key_mess)}'





# the decryption section
def decrypt(message, key):
  
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_message = ''
    key_plus = 0

    for letter in message.lower():

        # The first component loops through the shift_message so that it continues throughout the entire message.
        shift_index_key = key[ key_plus % len(key)]
        
        # Use an if condition to check whether letter is in alphabet. If true, process it; otherwise, skip to the next iteration.
        if letter in alphabet:

            # After looping the key, it's time to find the new letter's index.
            key_plus += 1
            num_index = alphabet.find(shift_index_key) 
            letter_index = alphabet.find(letter)
            new_letter_index = ((num_index * -1 ) + letter_index) % len(alphabet)
            new_letter = alphabet[new_letter_index]
            new_message += new_letter

        # If the character isn't in the alphabet, check if it's a space. If so, append it as-is.
        elif letter == ' ':
            new_message += ' '

        # If neither of the previous conditions are met, it's most likely a punctuation mark or a number, so leave it unchanged.
        else:
            new_message += letter
 
    return new_message

#the handler of decryption section
def decryption_handler():

    # Obtain the message input for encryption or decryption.
    message = input('Write the message you want to decrypt')
    # Ensures the Message is alphabetic; if not, prints a message and stops the code.
    if not message.replace(" ", "").isalpha():
        print('The message should only contain letters and spaces.')
        return
        # Now, if the user enters numbers, return will stop the code from running further.
         
        
    # Two choices: 1 for encryption, 2 for decryption (using * -1). Otherwise, it does nothing but prints the message inside the else block.
    key_mess = input('Write the key for decryption.')

    # I used .lower() to make the key flexible—without it, the code would break if the user enters an uppercase letter.
    key_mess = key_mess.lower()

    # Ensures the key is alphabetic; if not, prints a message and stops the code.
    if not key_mess.isalpha():
        print('the Key Message should be letters not numbers or something else.')

        # Now, if the user enters numbers, return will stop the code from running further.
        return
    


    
    
    # To make it user-friendly, I decided to add some flair to the code for the user.
    print(f'your Message is {message} and your key message is {key_mess}.')
    time.sleep(2)
    print('Processing...')
    time.sleep(3)

    print (f'The Result is {decrypt(message, key_mess)}')
    return f' The Result is {decrypt(message, key_mess)}'

