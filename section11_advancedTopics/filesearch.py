import os
import fnmatch


def find_albums(root, artist_name):
    for path, directories, files in os.walk(root):
        for artist in fnmatch.filter(directories, artist_name):
            sub_dir = os.path.join(path, artist)
            for album_path, albums, _ in os.walk(sub_dir):
                for album in albums:
                    yield os.path.join(album_path, album), album


def find_songs(albums):
    for album in albums:
        for song in os.listdir(album[0]): # we want the path, not the album name
            yield song

album_list = find_albums("music", "Aerosmith")
song_list = find_songs(album_list)

# for album in album_list:
#     print(album)
for s in song_list:
    print(s)