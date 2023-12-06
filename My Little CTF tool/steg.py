import filebinary as fb

data = fb.read_file_hex("BurningKermit.jpg")

#convert to binary
binarydata = bin(int(data,16))
binarydata = '2'+binarydata[2:]
binary_steg_message = ''

#get LSB bit and build a string from it
for key, bit in enumerate(binarydata):
    if key%8 == 0:
        binary_steg_message += bit

#convert new binary to hex
hex_steg_message = hex(int(binary_steg_message[1:],2))


spaced_hex_message = ""



for key, byte in enumerate(hex_steg_message):
    if key %2 != 0:
        spaced_hex_message += byte +" "
    else:
        spaced_hex_message += byte
spaced_hex_message = spaced_hex_message[2:]
listed_hex_message = spaced_hex_message.split(" ")

hidden_message = ""
for key, byte in enumerate(listed_hex_message):
    try:
        decoded_byte = bytes.fromhex(str(byte)).decode('utf-8')
        hidden_message += decoded_byte + " "
    except UnicodeDecodeError:
        print("No UTF-8 decoding found on the " + byte + " byte")
list_hidden_message = hidden_message.split(" ")
print(list_hidden_message)


'''
final_message = list_hidden_message

for char in list_hidden_message:
    if " " not in char:
        final_message.remove(char)
'''
#exclude header :)

#add element at the beginning of the binary file so the lists starts at 1 and we'r'e able to divide by 8 to ge the LSB

#separate list elements

#regroup the bits 8 by 8 to form new hew --> convert to whatever