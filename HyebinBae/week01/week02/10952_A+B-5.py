while True:
    line = input()
    A, B = map(int, line.split())

    if A == 0 and B == 0:
        break
    print(A + B)