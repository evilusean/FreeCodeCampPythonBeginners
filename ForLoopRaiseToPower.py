def raise2power(basenum, pownum):
    result = 1
    for index in range(pownum):
        result = result * basenum
    return result
print(raise2power(3,6))
#put numbers here ^