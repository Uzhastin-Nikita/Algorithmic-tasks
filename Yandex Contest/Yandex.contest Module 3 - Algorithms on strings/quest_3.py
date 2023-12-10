def prefix(str):
    pref = [0] * len(str)

    for i in range(len(str) - 1):
        j = pref[i]
        while (j>0) and (str[i+1] != str[j]):
            j = pref[j-1]
        if (str[i+1] == str[j]):
            pref[i+1] = j + 1
        else:
            pref[i+1] = 0
    return pref

str = input()

pref = prefix(str)

result = len(str) - pref[-1]

if (len(str) % result == 0):
    print(len(str) // result)
else:
    print('1')





