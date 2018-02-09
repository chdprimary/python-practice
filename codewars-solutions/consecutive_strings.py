# You are given an array strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.
# Example: longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
# n being the length of the string array, if n = 0 or k > n or k <= 0 return "".

# My second solution, more readable
def longest_consec(strarr, k):
    if len(strarr) == 0 or k > len(strarr) or k <= 0:
        return ''

    curr_longest_str = ''
    curr_str = ''
    for i in range(len(strarr)):
        if i+k <= len(strarr):
            curr_str = ''.join(strarr[i:i+k])
            if len(curr_str) > len(curr_longest_str):
                curr_longest_str = curr_str

    return curr_longest_str

# My first solution
def longest_consec(strarr, k):
    if len(strarr) == 0 or k > len(strarr) or k <= 0:
        return ''

    curr_longest_len = 0
    start_idx = 0
    for i in range(len(strarr)):
        if i+k <= len(strarr):
            if len(''.join(strarr[i:i+k])) > curr_longest_len:
                curr_longest_len = len(''.join(strarr[i:i+k]))
                start_idx = i

    return ''.join(strarr[start_idx:start_idx+k])