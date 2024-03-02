import struct
getBin = lambda x: x > 0 and str(bin(x))[2:] or "-" + str(bin(x))[3:]

def floatToBinary64(value) :
    val = struct.unpack('Q', struct.pack('d', value))[0]
    return getBin(val)
def binaryToF10at(value):
    hx = hex(int(value, 2))
    return struct.unpack("d", struct.pack("q", int(hx,16)))[0]

binstr = floatToBinary64(19.5)
print( 'Equivalente binario de 19.5: ')
print(binstr + '\n')

f1 = binaryToF10at(binstr)
print( ' Equivalente decimal de' + binstr)
print(f1)