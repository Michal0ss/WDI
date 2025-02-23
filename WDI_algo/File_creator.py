import os

"""This code creates a specified number of empty files with the `.py` extension at a designated location, 
using the given names."""

folder_path = "" #TODO -> ENTER YOUR FILE PATH

#if not os.path.exists(folder_path):
#    os.makedirs(folder_path)

file_extension = ".py"
wtype = "DO"

for i in range(173,213):
    file_name = os.path.join(folder_path,f"z{i}_{wtype}{file_extension}")

    with open(file_name, 'w') as file:
        file.write(f"#Zadanie_{i}")

    print(f"Utworzono pli nr_{i}")