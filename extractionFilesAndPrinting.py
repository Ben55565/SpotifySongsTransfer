import os
import pandas


music_formats = ["mp3", "wav", "acc", "flac"]


def get_all_files_names(path):
    """Gets directory with music files, returns 3 lists: 1.Songs found. 2.Songs might not find. 3.Files that are not songs"""

    full_songs_names_with_types = os.listdir(path)
    full_songs_names = []
    FULL = []
    might_not_find = []
    files_not_songs = []
    songs = []
    artist = []
    for item in full_songs_names_with_types:
        index_of_dot = item.rfind(".")
        file_type = item[index_of_dot + 1:].lower()
        # condition for checking the file format is indeed audio file
        if file_type not in music_formats:
            files_not_songs.append(item)
            full_songs_names_with_types.remove(item)
        else:
            # breaks the file name for artist and song name if possible
            song_full_name = item[0: index_of_dot].lower().strip()
            index_of_dash = song_full_name.find("-")
            if index_of_dash != -1:
                part_1 = song_full_name[0: index_of_dash].lower().strip()
                part_2 = song_full_name[index_of_dash + 1:].lower().strip()
                if part_1.isnumeric():
                    FULL.append(part_2)
                    if part_2 not in might_not_find:
                        might_not_find.append(part_2)
                elif part_2.isnumeric():
                    FULL.append(part_1)
                    if part_2 not in might_not_find:
                        might_not_find.append(part_1)
                else:
                    FULL.append(part_1 + " " + part_2)
                if part_1 not in full_songs_names:
                    full_songs_names.append(part_1)
                    songs.append(part_1)
                if part_2 not in full_songs_names:
                    full_songs_names.append(part_2)
                    artist.append(part_2)
            else:
                # trims the song name as long as it won't start with letter
                while not song_full_name[0].isalpha():
                    song_full_name = song_full_name[1:]
                if song_full_name not in full_songs_names:
                    full_songs_names.append(song_full_name)
                might_not_find.append(song_full_name)

    csv_file = {"songs": songs, "artist": artist}
    create_text_files_for_songs(full_songs_names, might_not_find, FULL)
    # using the csv to automate won't be the best idea, use it as a last resort
    create_csv_file(csv_file)
    return [full_songs_names, might_not_find, files_not_songs]


def create_csv_file(songs_and_artists):
    """Receive a dict, and create a csv file from the data using pandas."""
    data = pandas.DataFrame.from_dict(songs_and_artists, orient="index")
    data = data.transpose()
    data.to_csv("data.csv")


def print_extracted_names(details_found, files_not_songs, might_not_find):
    """Prints the list of songs couldn't separate from artist, and files found that are not songs."""

    print(f"\n\nTotal number of song titles and artists found is {len(details_found)}")

    print(f"\n\nPlease note that the shown file names are not music files (total of {len(files_not_songs)}):")
    for item in files_not_songs:
        print(item)
    print(f"\n\nPlease note that the shown tracks may not be found and has to be done manually (total of {len(might_not_find)}):")
    for item in might_not_find:
        print(item)


def create_text_files_for_songs(full_songs_names, might_not_find, full):
    """Gets two lists of songs details, and creating text files with the data."""
    # with open(r'./SongsAndArtists.txt', 'w', encoding="utf-8") as f:
    #     for item in full_songs_names:
    #         if not item.isnumeric():
    #             f.write(f"{item}\n")

    with open(r'./SongsMightFail.txt', 'w', encoding="utf-8") as f:
        for item in might_not_find:
            f.write(f"{item}\n")

    with open(r'./FullNames.txt', 'w', encoding="utf-8") as f:
        for item in full:
            f.write(f"{item}\n")
