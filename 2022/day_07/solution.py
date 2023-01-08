from dataclasses import dataclass


@dataclass
class File:
    kids: list[any]
    size: int = 0


def sum_kids_size(file: File):
    kids_sum = 0
    for kid in file.kids:
        sum_kids_size(kid)
        kids_sum += kid.size
    file.size += kids_sum


if __name__ == '__main__':
    input_data = "data_big.in"

    current_folder = []
    all_folders = {"": File(kids=[])}

    with open(input_data, 'r') as f:
        for line in f.read().splitlines():

            if line.startswith("$ ls") or line.startswith("dir "):
                continue

            elif line.startswith("$ cd"):
                new_folder_str = line.split()[2]

                if new_folder_str == "..":
                    current_folder = current_folder[:-1]
                    continue

                else:
                    parent_folder_str = "/".join(current_folder)
                    current_folder.append(new_folder_str)
                    current_folder_str = "/".join(current_folder)

                if current_folder_str not in all_folders:
                    all_folders[current_folder_str] = File(kids=[])
                all_folders[parent_folder_str].kids.append(all_folders[current_folder_str])

            else:
                all_folders["/".join(current_folder)].size += int(line.split()[0])

    sum_kids_size(all_folders[""])

    size_over_100k = 0
    all_size_list = []

    for path, file in all_folders.items():
        if file.size <= 100000:
            size_over_100k += file.size
        all_size_list.append(file.size)

    needed_space = abs(40000000 - all_folders[""].size)
    files_to_delete = [s for s in sorted(all_size_list) if s >= needed_space]

    print("\n-- Part 1: --")
    print(size_over_100k)
    print("\n-- Part 2: --")
    print(files_to_delete[0])
