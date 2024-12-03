from collections import defaultdict

def read_file(file_name):
    level_list = []

    with open(file_name, 'r') as file:
        for line in file:
            parts = line.split()
            level_list.append(parts)

    return level_list

def calculate_safe_reports(level_list):
    total = 0

    for level in level_list:
        if int(level[1]) - int(level[0]) > 0:
            isIncreasing = 1
        elif int(level[1]) - int(level[0]) < 0:
            isIncreasing = -1
        else:
            continue
        isSafe = True
        for i in range(1, len(level)):
            difference = int(level[i]) - int(level[i - 1])
            if not (1 <= abs(difference) <= 3 and difference * isIncreasing > 0):
                isSafe = False
                break
        if isSafe:
            total += 1
    
    return total

def is_safe(level):
        if int(level[1]) - int(level[0]) > 0:
            isIncreasing = 1
        elif int(level[1]) - int(level[0]) < 0:
            isIncreasing = -1
        else:
            return False
        isSafe = True
        for i in range(1, len(level)):
            difference = int(level[i]) - int(level[i - 1])
            if not (1 <= abs(difference) <= 3 and difference * isIncreasing > 0):
                isSafe = False
                break
        return isSafe

def check_reports(reports):
    total = 0
    
    for report in reports:
        if is_safe(report):
            total += 1
            continue
        
        found_safe_by_removal = False
        for i in range(len(report)):
            modified_report = report[:i] + report[i+1:]
            if is_safe(modified_report):
                found_safe_by_removal = True
                break
        
        if found_safe_by_removal:
            total += 1
    
    return total

level_list = read_file('Day2.txt')

total = calculate_safe_reports(level_list)
total2 = check_reports(level_list)

print(f"Total distance: {total}")
print(f"Total distance: {total2}")
