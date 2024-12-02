from collections import defaultdict

def read_file(file_name):
    left_list = []
    right_list = []
    similarity_dict = defaultdict(int)

    with open(file_name, 'r') as file:
        for line in file:
            parts = line.split()
            left_list.append(int(parts[0]))
            right_list.append(int(parts[1]))
            similarity_dict[int(parts[1])] += 1

    return left_list, right_list, similarity_dict

def calculate_total_distance(left_list, right_list):
    left_list.sort()
    right_list.sort()
    
    total_distance = 0
    for i in range(len(left_list)):
        total_distance += abs(left_list[i] - right_list[i])
    
    return total_distance

def calculate_similarity_score(col1, similarity_dict):
    score = 0
    for num in col1:
        score += num * similarity_dict[num]
    
    return score

left_list, right_list, sd = read_file('Day1.txt')

total_distance = calculate_total_distance(left_list, right_list)

similarity_score = calculate_similarity_score(left_list, sd)

print(f"Total distance: {total_distance}")
print(f"Similarity score: {similarity_score}")
