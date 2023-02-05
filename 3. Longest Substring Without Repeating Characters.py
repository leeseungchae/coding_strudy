import re


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """

    temp_list = []

    temp_str = ''

    for idx, st in enumerate(s):

        if st in temp_str:
            temp_list.append(temp_str)
            fi = temp_str.find(st)
            temp_str = temp_str[fi+1:]
            temp_str += st
            continue
        else:
            temp_str +=st
            if idx == len(input)-1:
                temp_list.append(temp_str)
    result = ''
    for temp in temp_list:
        if len(result) < len(temp):
            result = temp
    return len(result)


input = "abcabcbb"

result = lengthOfLongestSubstring(input)
print(result)