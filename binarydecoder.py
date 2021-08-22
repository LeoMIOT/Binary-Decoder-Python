# Binary Decoder - Leo Moura / BR - 2021 /
#--------------------------------------------------- 
# Binary data for testing ... be free to try another data.
# 01001100 01100101 01101111 00100000 01001101 01101111 01110101 01110010 01100001 00100000 00101101 00100000 01000010 01101001 01101110 01100001 01110010 01111001 00100000 01000100 01100101 01100011 01101111 01100100 01100101 01110010
#--------------------------------------------------- 
#Bits are almost always bundled together into 8-bit collections, and these collections are called bytes
bits_collection_size = 8 #  8 bits or 1 Byte
answer = 'YES'
answer = input('Say YES to continue...').upper()
while answer == 'YES':
    receiver = input("Type your binary data and press enter to continue")
    bits_collection = receiver.replace(" ","") #Remove whitespace
    def data_formatting(bits_collection):
         return bits_collection
    print('Typed data  ..',data_formatting(bits_collection))
    split_data = [str(bits_collection[i:i+bits_collection_size]) for i in range(0,len(receiver),bits_collection_size)]
    print ('8-bit collections ..',split_data) #8-bit collections
    result = " ".join(chr(int(bits_collection[i:i+8],2))for i in range (0, len(bits_collection),bits_collection_size))
    print ('Decoded Message ..', result) # ASCII
    answer =input('Say YES to continue...').upper()
# -----------------------------------------------------
