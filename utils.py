import os
import time


def read_text_files():
    path = os.getcwd() + "\\songs\\"
    # if path doesn't exist, create it
    if not os.path.exists(path):
        os.makedirs(path)
        print("Created directory '{}'".format(path))
        return []
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


def read_songs_file():
    with open('songs.txt', 'r') as file:
        return file.readlines()


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


def get_local_osu_maps_id():
    path = os.path.join(os.getenv('LOCALAPPDATA'), 'osu!', 'Songs')
    get = lambda: os.listdir(path)
    return [folder.split(' ')[0] for folder in get() if folder.split(' ')[0].isdigit()]


def create_local_osu_maps_file(local_osu_maps_id):
    if not os.path.exists(os.path.join(os.getcwd(), 'save')):
        os.makedirs(os.path.join(os.getcwd(), 'save'))
    maps_file_path = os.path.join(os.getcwd(), 'save',
                                  'local_osu_maps_{}.txt'.format(time.strftime('%Y-%m-%d-%H-%M-%S')))
    if not os.path.isfile(maps_file_path):
        with open(maps_file_path, 'w') as _:
            # write the local osu maps id to the file
            for map_id in local_osu_maps_id:
                _.write(map_id + '\n')
    print('Created local_osu_maps.txt file')


if __name__ == '__main__':
    # create_songs_file()
    # add_songs_to_file(read_text_files())
    create_local_osu_maps_file(get_local_osu_maps_id())
