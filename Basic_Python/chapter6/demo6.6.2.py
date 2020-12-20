# 二分查找

def search(sequence, number, lower, upper):
    if lower  == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle + 1, upper)
        else:
            return search(sequence, number, lower, middle)


seq = [99,43, 1, 2, 0, 76, 42, 101, 30, 7, 12, 11, 100]

print("排序之前的seq:", seq)

seq.sort()

print("排序之后的seq:", seq)


print(search(seq,100,0,len(seq)))










