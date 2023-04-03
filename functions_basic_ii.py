def countdown(max):
    result = []
    for i in range(max,-1, -1):
        result.append(i)
    return result

def print_and_return(list):
    print(list[0])
    return list[1]

def first_plus_length(list):
    return list[0] + len(list)

def greater_than_second(list):
    big_list = []
    for i in range(len(list)):
        if list[i] > list[1]:
            big_list.append(list[i])
    if len(big_list) <= 2:
        return False
    else:
        print(len(big_list))
        return(big_list)

def this_length_that_value(size,value):
    list = []
    while len(list) < size:
        list.append(value)
    return list
