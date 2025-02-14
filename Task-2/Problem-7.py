
set1=set(map(int,input().split()))
set2=set(map(int,input().split()))
def common_num(set1, set2):
    common = set1.intersection(set2)
    return common


print(common_num(set1, set2))