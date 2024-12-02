# Advent of Code 2024
# =-= Day 2 =-=

# =-= Shared =-=
def get_diff_dir(a:int,b:int):
    diff = b-a
    nz_diff = (diff*2)+1                # This prevents div by 0
    dir = nz_diff / abs(nz_diff)        # This will find the direction as +1 or -1 without branching
    return (abs(diff),dir)

# =-= Tasks =-=
def task1():
    f = open("input","r")
    lines = f.readlines()
    f.close()

    # Numbers have to be either all increasing or all decreasing
    # Adjacents must differ by at least 1 and at most 3

    unsafe_reports = 0

    for report in lines:
        split_report = report.split()       # Normally I'd split on " " but Python automatically splits on whitespace
        diff,gt_dir = get_diff_dir(int(split_report[0]),int(split_report[1]))

        if diff == 0 or diff > 3:
            unsafe_reports += 1

        else:
            for i in range(1,len(split_report)-1):
                diff,test_dir = get_diff_dir(int(split_report[i]),int(split_report[i+1]))

                if test_dir != gt_dir or diff == 0 or diff > 3: # If this report is unsafe:
                    unsafe_reports += 1                         # Add to the unsafe reports
                    break                                       # Skip checking the rest - the entire report is unsafe

    print(len(lines)-unsafe_reports)


if __name__ == "__main__":
    task1()