#!/usr/bin/env python

input = open("input","r")

total_weight = 0
elf_weight_list = []

for row in input:
    try:
        total_weight += int(row)
    except ValueError:
        elf_weight_list.append(total_weight)
        total_weight = 0

print(max(elf_weight_list))


temp_elf_weight_list = elf_weight_list.copy()
top_3_list = []

count = 0
while count < 3:
    highest_weight = max(temp_elf_weight_list)
    top_3_list.append(highest_weight)
    temp_elf_weight_list.remove(highest_weight)
    count += 1

print(sum(top_3_list))