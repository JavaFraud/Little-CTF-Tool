import filebinary as fb

data = fb.read_file_hex("BurningKermit.jpg")

#convert to binary
binarydata = bin(int(data,16))
binarydata = '2'+binarydata[2:]
binary_steg_message = ''

#get 8th bit and build a string from it
for key, bit in enumerate(binarydata):
    if key%8 == 0:
        binary_steg_message += bit

#convert new binary to hex
hex_steg_message = hex(int(binary_steg_message[1:],2))
print(hex_steg_message)
#exclude header :)

#add element at the beginning of the binary file so the lists starts at 1 and we'r'e able to divide by 8 to ge the LSB

'''
#separate list elements
for key, element in enumerate(data):

print(bin(int(data[0:10],16)))
'''


#get last bit

#regroup the bits 8 by 8 to form new hew --> convert to whatever