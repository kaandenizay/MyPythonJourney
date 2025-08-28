from nested_data import albums

SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

while True:
    print("Please choose your album (invalid choice exits):")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{0}: {1} - {2}".format(index+1, title, artist))
    chosen_album = int(input())
    if 1 <= chosen_album <= len(albums):
        while True:
            songs_list = albums[chosen_album-1][SONGS_LIST_INDEX]
            print("Please choose your song:")
            for (position, song_name) in songs_list:
                print("{0}: {1}".format(position, song_name))
            chosen_song = int(input())
            if 1 <= chosen_song <= len(songs_list):
                title = songs_list[chosen_song-1][SONG_TITLE_INDEX]
                print("Playing {}".format(title))
                print("=" * 25)
                break
            else:
                print("Invalid song")
    else:
        print("Invalid choice. Please try again.")
        break
