import re
from six.moves import reduce

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

def day3(cx = 3, cy = 1):
    with open("input/day3.txt") as f:
        v = [x for x in f.read().split("\n")[::cy]]
    trees = 0
    x = 0
    for y in v:
        trees += (y[x % len(v[0])] == "#")
        x += cx
    return trees
    f.close()

def day3_task1():
    print(day3())

def day3_task2():
    moves = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees = []
    for x,y in moves:
        trees.append(day3(x, y))
    print(reduce(lambda x, y: x*y, trees))


def day4_validation(passport, extended_validation):
    reqfields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    allfields = reqfields + ['cid']

    invalidfields = 0

    passport_fields = passport.split(' ')

    for field in reqfields:
        if field not in passport:
            invalidfields += 1
            break
        else:
            for p in passport_fields:
                k, v = p.split(':')
                if not day4_extended_validation(k, v) and extended_validation:
                    invalidfields += 1
                    break

    return (invalidfields == 0)

def day4_extended_validation(key, value):
    eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    if "byr" in key:
        if int(value) >= 1920 and int(value) <= 2002:
            return True

    if "iyr" in key:
        if int(value) >= 2010 and int(value) <= 2020:
            return True

    if "eyr" in key:
        if int(value) >= 2020 and int(value) <= 2030:
            return True

    if "hgt" in key:
        if "in" in value:
            if 59 <= int(re.sub("[a-z]", "", value)) <= 76:
                return True
        else:
            if 150 <= int(re.sub("[a-z]", "", value)) <= 193:
                return True

    if "hcl" in key:
        e = re.compile('#[0-9a-f]{6}')
        m = e.match(value)
        return(bool(m))

    if "ecl" in key:
        return value in eye_colors

    if "pid" in key:
        return len(value) == 9

    if "cid" in key:
        return True

    return False

def day4(extended_validation = False):
    validcount = 0
    processable = []
    with open("input/day4.txt") as f:
        all_passports = f.readlines()
        all_passports = [line.strip() for line in all_passports]
        all_passports.append('')

        passport = ''
        for e in all_passports:
            if e != '':
                passport += ' ' + e
            else:
                processable.append(passport.strip())
                passport = ''

        for passport in processable:
            if day4_validation(passport, extended_validation):
                validcount += 1

    print(validcount)
