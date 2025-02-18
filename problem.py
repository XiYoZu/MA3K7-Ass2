import numpy as np

n = 8

og_set = np.arange(1,n+1)
og_list = []
og_list.append(og_set)

def process_list(my_list):
    target_list = []
    for k in range (len(my_list)):
        current_list = my_list[k].copy()
        for i in range (len(my_list[0])-1):
            for j in range (i+1, len(my_list[0])):
                new_list = np.append(current_list,abs(current_list[i]-current_list[j]))
                new_list = np.delete(new_list, [i,j])
                target_list.append(new_list)
    return target_list

while len(og_list[0]) > 1:
    og_list = process_list(og_list)

dist_list = np.zeros(n+1, dtype=int)

for i in range(len(og_list)):
    dist_list[og_list[i][0]] += 1

print(dist_list)

    

