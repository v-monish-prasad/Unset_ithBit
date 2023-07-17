def unsetI_thBit(ogNumber, checkBit):
    number = ogNumber
    for i in range(checkBit):
        number >>= 1

    if number & 1:
        return ogNumber ^ (1 << checkBit)
    else:
        return ogNumber


if __name__ == "__main__":
    A = int(input())
    B = int(input())

    print(unsetI_thBit(A, B))
