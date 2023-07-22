import os


def read_text_files():
    path = os.getcwd() + "\\songs\\"
    text_files = [file for file in os.listdir(path) if file.endswith('.txt')]
    text_files.sort()
    songs_id = []
    for text_file in text_files:
        print("Reading text file '{}'".format(text_file))
        with open(path + text_file, 'r') as file:
            songs_id.extend(file.readlines())
    songs_id = list(set(songs_id))
    songs_id.sort()
    return songs_id


def create_songs_file():
    song_file_path = os.path.join(os.getcwd(), 'songs.txt')
    if not os.path.isfile(song_file_path):
        with open(song_file_path, 'w') as _:
            pass


def add_songs_to_file(song_ids):
    with open('songs.txt', 'r') as file:
        existing_ids = file.readlines()
    with open('songs.txt', 'a') as file:
        for song_id in song_ids:
            if song_id not in existing_ids:
                file.write(song_id)


if __name__ == '__main__':
    create_songs_file()
    add_songs_to_file(read_text_files())
