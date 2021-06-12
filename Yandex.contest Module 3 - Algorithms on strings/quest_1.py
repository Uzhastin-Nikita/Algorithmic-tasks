def get_hash(string, substring, n):
    k = 31
    m = 1
    substring_hash = 0

    for i in substring[::-1]:
        substring_hash += ord(i) * m
        m *= k
        substring_hash %= n
        m %= n
    
    m = 1
    hash = 0
    for i in string[:len(substring)][::-1]:
        hash += ord(i) * m
        m *= k
        hash %= n
        m %= n
    
    hash_tag = 1
    for i in range(len(substring) - 1):
        hash_tag *= k
        hash_tag %= n
    
    res = []

    if hash == substring_hash:
        res.append(0)

    for i in range(1, len(string) - len(substring) + 1):
        # вычисляем хеш
        new_hash = ((hash % n - ord(string[i - 1]) * hash_tag % n) * k % n + ord(string[i + len(substring) - 1])) % n
        if new_hash == substring_hash:
            res.append(i)
        hash = new_hash
    return res

string = input()
substring = input()
n = 2 ** 31 - 1
array = get_hash(string, substring, n)
print(' '.join(map(str, array)))

    