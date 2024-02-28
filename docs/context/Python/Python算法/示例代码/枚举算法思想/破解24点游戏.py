#
import copy
import itertools


# 计算出4个数所有的排列
def calculate_list(nums,length=4):
    origin_list = list(set(itertools.permutations(nums, length)))
    return origin_list


# 计算任意2个数，四则运算的结果
def arithmetic(num1, num2):
    list = [num1 + num2, num1 - num2, num1 * num2, num1 / num2]
    return list


def rebuild_list(origin_list_part):
    for cell in set(itertools.combinations(origin_list_part, 2)):  # 计算两个数的组合
            answer=[]
            answer=arithmetic(cell[0], cell[1])
            list = copy.deepcopy(origin_list_part)
            list.remove(cell[0])
            list.remove(cell[1])
            list=list(set(itertools.product(list,answer)))
    return list

if __name__ == "__main__":
    nums=list(map(int,input().split()))
    origin_list=calculate_list(nums)
    for origin_list_part in origin_list:
        print(rebuild_list(origin_list_part))

