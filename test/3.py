import numpy as np
import pandas as pd
import collections as col

with open('./cmoa_clean.tsv', encoding='utf8') as f:
    cmoa_data = np.loadtxt(f, dtype='O', skiprows=1, delimiter="\t")
    cmoa_data[:, 3] = cmoa_data[:, 3].astype(float)
    cmoa_data[:, 4] = cmoa_data[:, 4].astype(float)
    cmoa_data = np.array(cmoa_data)
f.close()
# Field Name title creation_date medium item_width item_height full_name birth_place

df = pd.DataFrame(
    {
        'title': cmoa_data[:, 0],
        'creation_date': cmoa_data[:, 1],
        'medium': cmoa_data[:, 2],
        'item_width': cmoa_data[:, 3],
        'item_height': cmoa_data[:, 4],
        'full_name': cmoa_data[:, 5],
        'birth_place': cmoa_data[:, 6]
    }
)
print(df['full_name'])
# Separate names with |
idx_list = df.index.tolist()
for i in range(len(idx_list)):
    idx = idx_list[i]
    d_l = df['full_name'][idx].split()
    while '' in d_l:
        d_l.remove('')
    new_str = ''
    for j in range(len(d_l)):
        if j != len(d_l) - 1:
            new_str += d_l[j] + '|'
        else:
            new_str += d_l[j]

    df['full_name'] = new_str

print(df['full_name'].head())
# print(len(df['title'].tolist()))
title_count_dict = dict(col.Counter(df['title'].tolist()))
groupsize = sorted(list(set(list(title_count_dict.values()))))
# print(groupsize)
title_count = [0 for i in range(len(groupsize))]
for i in range(len(groupsize)):
    for k,v in title_count_dict.items():
        if v == groupsize[i]:
            title_count[i] += 1

new_df = pd.DataFrame(
    {
        'groupsize': groupsize,
        'Artifacts': title_count
    }
)
print(new_df)


with open('./museum_data_assignment-1.tsv') as f:
    museum = np.loadtxt(f, dtype = 'O', skiprows=1, delimiter="\t")
    museum = np.array(museum)
f.close()

# artifactNumber	ObjectName	BeginDate	group1	category1	material	Length	Width	Height	image
df_1 = pd.DataFrame(
    {
        'artifactNumber': museum[:, 0],
        'ObjectName': museum[:, 1],
        'BeginDate': museum[:, 2],
        'group1': museum[:, 3],
        'category1': museum[:, 4],
        'material': museum[:, 5],
        'Length': museum[:, 6],
        'Width': museum[:, 7],
        'Height': museum[:, 8],
        'image': museum[:, 9]
    }
)

with open('./unique_foods.csv') as f:
    food = np.loadtxt(f, dtype = 'O', skiprows=1, delimiter="\t")
    food = np.array(food)
f.close()

food_list = food.tolist()
# print(food_list)
# Exporting works
artifact_list = df_1['ObjectName'].tolist()

count_list = []
for i in range(len(artifact_list)):
    artifact = artifact_list[i]
    count = 0
    for j in range(len(food_list)):
        if food_list[j] in artifact:
            count += 1
    count_list.append(count)

# name_list = df['full_name'].tolist()
target_artifact_list = []
for i in range(len(count_list)):
    if count_list[i] >= 1:
        target_artifact_list.append(artifact_list[i])

target_artifact_list = list(set(target_artifact_list))
for i in range(len(target_artifact_list)):
    print(f"{target_artifact_list[i]} with food!")