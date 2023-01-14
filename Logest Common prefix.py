def longestCommonPrefix(strs):
    check = None
    if len(strs) == 1:
        check = strs[0]
    else:
        for idx, word in enumerate(strs):
            idx += 1
            if idx == 1:
                for i in range(len(strs) - idx):
                    word_2 = strs[idx + i]
                    hap = ''
                    for i, j in zip(word, word_2):
                        if i == j:
                            hap = hap + i
                        else:
                            break
                    if check is not None and len(check) > len(hap):
                        check = hap
                    elif check is None:
                        check = hap
    for word in strs:
        if check in word:
            pass
        else:
            return ""
        return check


"""Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "". """

Input = ["flower","flow","flight"]
result = longestCommonPrefix(Input)

print(result)
