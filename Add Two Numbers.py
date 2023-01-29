from typing import Optional

from Cython.Compiler.ExprNodes import ListNode


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

    result_list=[]



    l1_num =  ''.join(str(s) for s in l1)
    l2_num =  ''.join(str(s) for s in l2)

    sum = int(l1_num)+int(l2_num)

    for idx, i in enumerate(str(sum)):

        result_list.append(int(str(sum)[-idx-1]))
    print(result_list)



l1 =[2, 4, 3]
l2 = [5, 6, 4]


addTwoNumbers(l1,l2)