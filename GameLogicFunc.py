def Presser(list):
    b = [0, 0, 0, 0]
    temp_ind = 0
    for k in list:
        if k != 0:
            if b[temp_ind] == 0:
                b[temp_ind] = k
            else:
                if b[temp_ind] == k:
                    b[temp_ind] += 1
                else:
                    b[temp_ind + 1] = k
                temp_ind += 1
    return b


def LeftComm(ac):
    a = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(0, 4):
        for j in range(0, 4):
            a[i][j] = ac[i][j]
    for i in range(0, 4):
        a[i] = Presser(a[i])
    return a


def RightComm(ac):
    a = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(0, 4):
        for j in range(0, 4):
            a[i][j] = ac[i][j]
    for i in range(0, 4):
        b = [0, 0, 0, 0]
        for j in range(0, 4):
            b[3 - j] = a[i][j]
        b = Presser(b)
        for j in range(0, 4):
            a[i][j] = b[3 - j]
    return a



def DownComm(ac):
    a = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(0, 4):
        for j in range(0, 4):
            a[i][j] = ac[i][j]
    for j in range(0, 4):
        b = [0, 0, 0, 0]
        for i in range(0, 4):
            b[3 - i] = a[i][j]
        b = Presser(b)
        for i in range(0, 4):
            a[i][j] = b[3 - i]
    return a


def UpComm(ac):
    a = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(0, 4):
        for j in range(0, 4):
            a[i][j] = ac[i][j]
    for j in range(0, 4):
        b = [0, 0, 0, 0]
        for i in range(0, 4):
            b[i] = a[i][j]
        b = Presser(b)
        for i in range(0, 4):
            a[i][j] = b[i]

    return a

def CHECK_TABLES(a, b):
    for i in range(0, 4):
        for j in range(0, 4):
            if a[i][j] != b[i][j]:
                return True
    return False