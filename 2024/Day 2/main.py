# Advent of Code 2024
# =-= Day 2 =-=

# -- Shared --
def get_diff_dir(a:int,b:int):
    diff = b-a
    nz_diff = (diff*2)+1                # This prevents div by 0
    dir = nz_diff / abs(nz_diff)        # This will find the direction as +1 or -1 without branching
    return (abs(diff),dir)

def validate_report(report:list):
    diff,gt_dir = get_diff_dir(report[0],report[1])         # This is our base different and ground truth direction

    if diff == 0 or diff > 3:
        return (0,0)
    else:
        for i in range(1,len(report)-1):                    # Don't need to recheck index 0 (and 1)
            diff, test_dir = get_diff_dir(report[i],report[i+1])

            if test_dir != gt_dir or diff == 0 or diff > 3:
                return (0,i)
        
        return (1,-1)

# -- Task 1 --
def task1():
    '''
        Task 1 wants us to find if all the levels in a report are either:
            - All increasing or all decreasing
            - A delta of 0<d<4

        Final output is the total number of reports within those guidelines.
    '''

    f = open("input","r")
    lines = f.readlines()
    f.close()

    safe_reports = 0

    for report in lines:
        split_report = [int(x) for x in report.split()]       # Normally I'd split on " " but Python automatically splits on whitespace
        safe_reports += validate_report(split_report)[0]             #[0] is the exit code of the function; 1 means successful

    print(safe_reports)

# -- Task 2 --
def task2():
    '''
        Task 2 wants us to find if all the levels in a report are either:
            - All increasing or all decreasing
            - A delta of 0<d<4
        -and- if by removing one value the report becomes valid.

        Final output is the total number of reports within those guidelines.
    '''
    f = open("input","r")
    lines = f.readlines()
    f.close()

    safe_reports = 0

    for report in lines:
        split_report = [int(x) for x in report.split()]
        exit_code, exit_index = validate_report(split_report)
        if exit_code == 0:
            for i in range(max(0,exit_index-1),min(len(split_report),exit_index+2)):        # Don't want bounds error, check 1 below & 1 above
                test_report = split_report.copy()
                test_report.pop(i)
                if validate_report(test_report)[0] == 1:
                    safe_reports += 1
                    break
        else:
            safe_reports += 1
    
    print(safe_reports)

if __name__ == "__main__":
    task1()
    task2()