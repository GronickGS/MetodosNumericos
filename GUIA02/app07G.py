def ieee745 (N): # bits
    a = int (N[0])
    b = int(N[1:9],2)
    c = int("1" + N[9:],2)
    return (-1)**a*c/(1<<(len(N)-9-(b-127)))

N = "110000011010010011"
print(ieee745(N))