import os
import fnmatch


def find_music(start, extension):
    for root, dirs, files in os.walk(start):
        for file in fnmatch.filter(files, '*.{}'.format(extension)):
            yield os.path.join(root, file)


my_music_files = find_music("music", "*.emp3")

for f in my_music_files:
    print(f)