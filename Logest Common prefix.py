from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    """Longest Common Prefix
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".

    :argument strs: list
    :return str
    """

    check = None
    if len(strs) == 1:
        check = strs[0]
    else:
        for idx, word in enumerate(strs):
            idx += 1
            if idx == 1:
                for i in range(len(strs) - idx):
                    word_2 = strs[idx + i]
                    hap = ""
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


""" input spec:
    영어 단어들로 이루어진 리스트만 입력 가능하고,
    단어의 공백 및 알파벳 이외의 글자는 허용하지 않는다."""

Input = ["flower", "flow", "flight"]
result = longestCommonPrefix(Input)

print(result)
