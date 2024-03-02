def DecimalABinario (num):
    if num >= 1:
        DecimalABinario(num // 2)
        print (num % 2)
DecimalABinario(28)