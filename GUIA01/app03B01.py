def BinarioADecima1(binario) :
    decimal, i = 0,0
    while(binario != 0):
        dec = binario % 10
        decimal = decimal + dec * pow(2,i)
        binario = binario//10
        i+=1
    print(decimal)
BinarioADecima1(100)
BinarioADecima1(101)
BinarioADecima1(10011110101010111111111)