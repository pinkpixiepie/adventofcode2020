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


#Day 2, and we do it like we did it in Perl...
import re
def day2_task1():
    with open("input/day2.txt") as f:
        line = f.readline()
        c = 0
        while line:
            if int(re.findall(r"(\d+)-", line)[0]) <= \
               len(re.findall(re.findall(r"(\w):", line)[0], re.findall(r":(.+)", line)[0] )) <= \
               int(re.findall(r"-(\d+)", line)[0]):
                c += 1
            line = f.readline()
        print(c)
    f.close()

def day2_task2():
    with open("input/day2.txt") as f:
        line = f.readline()
        c = 0
        while line:
            chars = []
            chars.extend(re.findall(r":(.+)", line)[0])
            if (chars[int(re.findall(r"(\d+)-", line)[0])] == re.findall(r"(\w):", line)[0] or
                chars[int(re.findall(r"-(\d+)", line)[0])] == re.findall(r"(\w):", line)[0]) and \
                chars[int(re.findall(r"(\d+)-", line)[0])] != chars[int(re.findall(r"-(\d+)", line)[0])]:
                c += 1
            line = f.readline()
        print(c)
    f.close()