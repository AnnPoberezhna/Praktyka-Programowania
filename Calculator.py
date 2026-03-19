def Add(numbers):
    if numbers == "":
        return 0
    split_nums = numbers.replace('\n', ',').split(',')
    #print(split_nums)
    if len(split_nums) > 2:
        raise ValueError
    splitted_nums = 0

    for i in split_nums:
        splitted_nums += int(i)


    return splitted_nums

# # input string "1,2"
# Add("1, 2, 3")