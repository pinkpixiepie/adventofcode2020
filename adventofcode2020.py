def day1_task1():
    with open("input/day1.txt") as f:
        n = 2020
        n2 = n//2
        numbers = list(map(int, f.readlines()))
        fnum = {n - x for x in numbers if x <= n2} & {x for x in numbers if x > n2}
        pairs = [(n - x, x) for x in fnum]
        print(pairs[0][0]*pairs[0][1])
    f.close()

def day1_task2():
    with open("input/day1.txt") as f:
        nums = list(map(int, f.readlines()))
        n = len(nums)
        sum = 2020
        for i in range(0, n-2):
            for j in range(i + 1, n-1):
                for k in range(j + 1, n):
                    if (nums[i]+nums[j]+nums[k] == sum):
                        print(nums[i]*nums[j]*nums[k])
    f.close()

day1_task2()