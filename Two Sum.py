from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:

    for idx, num in enumerate(nums,start=1):

        for j in range(len(nums)-idx):
            if target == num + nums[idx + j] :
                result = []
                result.append(idx-1)
                result.append(idx+j)
                return result


""" input spec:
    input은 리스트 이며, 실수만 입력 가능하다.
    타겟은 리스트 중 두개의 합의 값만 입력 가능하다"""


Input = [3.5,2.5,4]
target = 6

result = twoSum(Input,target)
print(result)
