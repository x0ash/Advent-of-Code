# Advent of Code 2024
# =-= Day 3 =-=

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

    results = 0

    while "mul(" in data:
        start_idx = data.index("mul(",)
        data = data[start_idx+4:]
        if "mul(" in data:
            if ")" in data:
                end_idx = min(data.index(")"),data.index("mul("))
        elif ")" in data:
            end_idx = data.index(")")
        else:
            end_idx = len(data)
        value_str = data[0:end_idx]
        values = value_str.split(",",1)
        if len(values) == 2:
            if values[0].isnumeric() and values[1].isnumeric():
                results += (int(values[0])*int(values[1]))
        data = data[end_idx:]

    print(results)

    return 0

if __name__ == "__main__":
    task1()