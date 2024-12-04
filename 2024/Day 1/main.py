# Advent of Code 2024
# =-= Day 1 =-=

# -- Shared --
def split_number_file(filename):
    f = open(filename,"r")
    lines = f.readlines()
    f.close()

    lA,lB = [],[]
    for line in lines:
        cur_line = line.split(" ") # I know that in the result of this my two numbers will be at indexes 0 (first) and -1 (last)
        lA.append(int(cur_line[0]))
        lB.append(int(cur_line[-1])) # Casting to int automatically strips '\n' before conversion

    return (lA,lB)

# -- Task 1 --
def task1():
    '''
        Task 1 requires us to split the input file into two number lists and find the difference between the smallest->biggest
        values of each list.

        Final output is the total sum of the differences.
    '''
    lA,lB = split_number_file("input")
    diff = []

    lA.sort()
    lB.sort()

    for i in range(0,len(lA)):
        diff.append(abs(lA[i]-lB[i])) # Absoluting makes this a walk in the park
    
    print(sum(diff))

    return 0

# -- Task 2 --
def task2():
    '''
        Task 2 requires us to split the input file into two number lists and find how many times a number from list A appears
        in list B.

        Final output is the total sum of occurrances. Note: repeated numbers from list A are counted in the final sum.
    '''
    lA,lB = split_number_file("input")
    sim_score = []
    for num in lA:
        sim_score.append(num*lB.count(num))
    
    print(sum(sim_score))

    return 0

if __name__ == "__main__":
    task1()
    task2()