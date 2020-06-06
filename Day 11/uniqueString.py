def is_unique(input_str):
    if len(input_str) > 256:
        return False
    char = [False]*128
    for i in range(0, len(input_str)):
        val = ord(input_str[i])
        if char[val]:
            return False
        char[val] = True
    return True
input_str = "abcdefghij"
print(is_unique(input_str))
