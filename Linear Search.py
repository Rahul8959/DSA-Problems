#Link of Problem: https://www.codingninjas.com/studio/problems/linear-search_6922070?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def linearSearch(n: int, num: int, arr: [int]) -> int:
    # Write your code here.
    count=0
    got=0
    for i,val in enumerate(arr):
        if val==num:
            return i
    return -1
    pass
