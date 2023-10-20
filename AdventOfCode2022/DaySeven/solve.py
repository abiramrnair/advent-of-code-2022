# Get file input
with open('input.txt') as f:
    input_lines = [line.strip() for line in f.readlines()]

# Part One
list_mode = False
file_path = []
file_system = {
    '/': {}
}
def createFile(index, system, fileToAdd):
    all_files = system[file_path[index]]
    file_size, file_name = fileToAdd
    if index == len(file_path) - 1:
        if file_name not in all_files:
            if file_size == 'dir':
                all_files[file_name] = {}
            else:
                all_files[file_name] = int(file_size)
    else:
        createFile(index + 1, all_files, fileToAdd)
less_than_partone = [0]
least_size_parttwo = [0]
def traverseTree(root, system):
    all_files = system[root]
    total_storage = 0
    for file in all_files:
        if isinstance(all_files[file], int):
            total_storage += all_files[file]
        else:
            total_storage += traverseTree(file, all_files)
    # Part One
    if total_storage <= 100000:
        less_than_partone[0] += total_storage
    # Part Two
    # if root == '/': # Need 1077191 of free space
    #     print(30000000 - (70000000 - total_storage))
    if total_storage >= 5174025:
        if not least_size_parttwo[0]:
            least_size_parttwo[0] = total_storage
        else:
            least_size_parttwo[0] = min(least_size_parttwo[0], total_storage)
    return total_storage
for line in input_lines:
    command = line.split(' ')
    if command[0] == '$':
        if command[1] == 'cd':
            if command[2] == '..':
                file_path.pop()
            else:
                file_path.append(command[2])
    else:
        createFile(0, file_system, command)
traverseTree('/', file_system)
print(less_than_partone[0]) # Answer: 1077191
print(least_size_parttwo[0]) # Answer: 5649896