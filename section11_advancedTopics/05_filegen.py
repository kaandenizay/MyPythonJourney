import os

root = 'music'

for path, directories, files in os.walk(root, topdown=True):
    # os.walk is a generator, so it doesn't try to read every single file and directory at once,
    # it's only yielding the details for a single directory at a time
    # print(path)
    # print(directories)
    # print(files)
    # for f in files:
    #     print("\t{}".format(f))
    if files:
        print(path)
        first_split = os.path.split(path)
        print(first_split)
        second_split = os.path.split(first_split[0])
        print(second_split)
        for f in files:
            song_details = f.strip('.emp3').split(' - ')
            print(song_details)
        print("*" * 28)

