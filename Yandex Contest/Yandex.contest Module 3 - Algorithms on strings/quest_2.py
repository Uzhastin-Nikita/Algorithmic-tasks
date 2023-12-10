def get_hash(string, p, x):
    hash = 0
    for i in range(len(string)):
        hash = (hash * x + ord(string[i])) % p
    return hash

def get_new_hash(string, substring, p, x):
    if string == substring:
        return 0
    else:
        hash_string = get_hash(string, p, x)
        hash_substring = get_hash(substring, p, x)
        x_t = 1
        for i in range(len(string)-1):
            x_t = (x_t * x) % p
        for i in range(len(string)):
            if hash_string == hash_substring:
                return i
                break
            else:
                hash_substring = (x * (hash_substring - ord(substring[i]) * x_t) + ord(substring[i])) % p
        if hash_string != hash_substring:
            return -1
            
        
    
string = input()
substring = input()
x = 26
p = 10**9 + 7
print(get_new_hash(string, substring, p, x))

    

