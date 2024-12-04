# Advent of Code 2024
# =-= Day 3 =-=

# -- Shared --
def find_function(data:str,func_name:str):
    func_start = func_name + "("
    start_idx, end_idx = 0, -1
    offset = 0
    while data[start_idx+offset:end_idx].count(func_start)>0:
        start_idx = data.index(func_start,start_idx+offset)
        end_idx=data.index(")",start_idx)+1
        offset += 1
    return start_idx,end_idx

def mul_from_str(mul_str:str):
    values = mul_str.split(",",1)
    if len(values) == 2:
        if values[0].isnumeric() and values[1].isnumeric():
            return int(values[0]) * int(values[1])
    return 0

# -- Task 1 --
def task1():
    '''
        Task 1 requires a string to be checked for any instances of 'mul(*,*)', where * can be any integer.
        Once these are all found, you must perform the mul operation (multiply).
        Finally, sum the result of all multiplications.
    '''

    # Initial thought is to use regex, but Python doesn't support it without imports. I want to do AoC without imports.

    f = open("input","r")
    data = f.read()
    f.close()

    result = 0

    start_idx,end_idx = 0,0

    while end_idx != -1:
        data_chunk = data[start_idx:]
        new_start_idx,end_idx = find_function(data_chunk,"mul")
        result += mul_from_str(data_chunk[new_start_idx+4:end_idx-1])
        start_idx += end_idx

    print(result)

    return 0

# -- Task 2 --
def task2():
    '''
        Task 2 requires a string to be checked for any instances of 'mul(*,*)', where * can be any integer.
        Once these are all found, you must perform the mul operation (multiply).
        It also requires that instances of "do()" and "don't()" should be checked for, where don't() disables
        multiplications until a subsequent do() is found in the data.
        Finally, sum the result of all enabled multiplications.
    '''

    f = open("input","r")
    data = f.read()
    f.close()

    result = 0

    start_idx,end_idx = 0,0

    mul_enable = True               # controlled by "do()" and "don't()"
    
    while end_idx != -1:
        data_chunk = data[start_idx:]       # 1st remove already checked portion of data
        if mul_enable:
            new_start_idx,end_idx = find_function(data_chunk,"mul") # find the next occurance of mul in data chunk
            next_dont = find_function(data_chunk,"don't")[1]        # find the next don't so we know when to stop & skip
            mul_enable = end_idx<next_dont or next_dont == -1       # we know we're past a don't if end_idx is higher & -1 means no more don'ts
            if mul_enable:
                result += mul_from_str(data_chunk[new_start_idx+4:end_idx-1])
            else:
                end_idx=next_dont       # we need to roll back to the don't if end_idx passed it

        else:
            new_start_idx,end_idx = find_function(data_chunk,"do")  # when we loop around again we can find next do
            mul_enable = True                                       # and just enable because we have it

        start_idx += end_idx        # always updating start_idx to the new end point pushes us along in the data

    print(result)
    return 0

if __name__ == "__main__":
    task1()
    task2()