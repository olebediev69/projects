'''
I, Oleksandr Lebediev, fully acknowledge the consequences of academic misconduct.
During my work, I:
Consulted following materials: https://www.w3schools.com/python/python_file_write.asp
'''

from statistics import mode,mean

# opening the files
name_grades_file = open ("name_grades.txt", 'r')
analysis_file = open ("analysis_file.txt", 'w')


# clear the previous iterations of the code
analysis_file.write('')
some_dictonary = {}

def n_deletion(some_list):
    modified_list = []
    for i in some_list[1:]:
      modified_list.append(i.replace('\n', ''))
    return modified_list

def integiration_list(some_list):
    new_values_list = []
    for i in some_list:
        new_values_list.append(int(i))

    return new_values_list

def nested_list(some_list):
    unnested_list = [item for sublist in some_list for item in sublist]
    return unnested_list

for i in name_grades_file:
    splitted_list = i.split(' ')
    formatted_list = n_deletion(splitted_list)
    numbers_list = integiration_list(formatted_list)
    some_dictonary[splitted_list[0]] = numbers_list

general_grades_list = []
for grades_list in some_dictonary.values():
    general_grades_list.append(grades_list)

unnested_list = nested_list(general_grades_list)

for name,grades in some_dictonary.items():
    analysis_file.write(f"{name}'s average grade: {int(sum(grades)/len(grades))}\n")

analysis_file.write(f'\n The highest grade is {int(max(unnested_list))}\n')
analysis_file.write(f'\n The lowest grade is {int(min(unnested_list))}\n')
analysis_file.write(f'\n The mean grade is {int(mean(unnested_list))}\n')
analysis_file.write(f'\n The mode grade is {int(mode(unnested_list))}\n')

analysis_file.close()
name_grades_file.close()