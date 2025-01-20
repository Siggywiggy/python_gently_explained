def collatz(startingnum):
    if startingnum <= 1:
        return []

    sequence_nums = list()
    sequence_nums.append(startingnum)

    while True:
        if startingnum == 1:
            break

        elif startingnum % 2 == 0:
            startingnum = startingnum // 2
            sequence_nums.append(startingnum)
        else:

            startingnum = startingnum * 3 + 1
            sequence_nums.append(startingnum)

    return sequence_nums


print(collatz(10))
print(collatz(11))
assert len(collatz(256)) == 9