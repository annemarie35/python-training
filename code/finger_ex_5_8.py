# Remedy the problem described in the previous paragraph.
# Hint: a simple way to do this is to create a new book by appending something to the original book.

don_quixote_book = 'In a village of La Mancha, the name of which I have no desire to call to mind, there lived not long since one of those gentlemen that keep a lance in the lance-rack, an old buckler, a lean hack, and a greyhound for coursing.'
don_quixote_book_appended  = don_quixote_book + '^'
gen_decode_keys = (
    lambda book,
           cipher_text: {
        s: book[int(s)] for s in cipher_text.split('*')
    }
)

#print(don_quixote_book[300]) # IndexError: string index out of range

print(gen_decode_keys(don_quixote_book_appended, '-1*2')) # Prints {'-1': '^', '2': ' '}
print(gen_decode_keys(don_quixote_book_appended, '22*13*33*137')) # Prints {'-1': '^', '2': ' '}


# Using encoder and encrypt as models, implement the functions decoder and decrypt. Use them to decrypt the message
#   22*13*33*137*59*11*23*11*1*57*6*13*1*2*6*57*2*6*1*22*13*33*1
#   37*59*11*23*11*1*57*6*173*7*11
# which was encrypted using the opening of Don Quixote.

don_quixote_book = 'In a village of La Mancha, the name of which I have no desire to call to mind, there lived not long since one of those gentlemen that keep a lance in the lance-rack, an old buckler, a lean hack, and a greyhound for coursing.'

def decoder(book, text_to_decode):
    return \
        {
            s: book[int(s)] for s in text_to_decode.split('*')
        }

def decrypter(book, text_to_decrypt, decoder):
    decoded_text = decoder(book, text_to_decrypt)
    decrypted_text = ''
    for value in decoded_text.values():
        decrypted_text += str(value)

    return decrypted_text

text_to_decrypt = '22*13*33*137*59*11*23*11*1*57*6*13*1*2*6*57*2*6*1*22*13*33*137*59*11*23*11*1*57*6*173*7*11'
print(decoder(don_quixote_book, text_to_decrypt))
print(decrypter(don_quixote_book, text_to_decrypt, decoder))