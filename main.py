from selenium import webdriver
from selenium.webdriver.common.by import By
import utils
import time
import os

# sleep time default 3
wait = lambda: time.sleep(3)


def extract_leading_number(s):
    match = re.match(r'(\d+)', s)
    return match.group(1) if match else None


def map_downloader():
    # file fetching location
    songs_id = utils.read_songs_file()
    browser = webdriver.Chrome()
    browser.get("https://osu.ppy.sh/home")
    input("Please log in and press Enter when you're ready.")
    print("Starting the process.\n")
    if not songs_id:
        print("Couldn't read the file or the file is empty.")
        return 0

    failed_list = list()

    for i in songs_id:
        browser.get(f"https://osu.ppy.sh/beatmapsets/{i.split()[0]}")
        wait()
        try:
            download_buttons = browser.find_elements(By.CSS_SELECTOR, ".btn-osu-big.btn-osu-big--beatmapset-header")
            download_button = download_buttons[0]
            download_button.click()
        except Exception as _:
            failed_list.append(i)
        wait()
    if failed_list:
        print(
            "Couldn't download some maps. The codes of the maps that could not be downloaded were saved in the error_list.txt file.")
        file = open("error_list.txt", "w", encoding="utf-8")
        for errors in failed_list:
            file.write("{}\n".format(errors))
        file.close()

    time.sleep(25)
    print("That's all from me")
    input("Is it okay? :\n")


def map_scanner():
    print("You can scan the maps in the Songs folder of the osu! game.")
    print("Select the folder where the maps are located.")

    default_path = f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\osu!\\Songs"

    try:
        files_and_folders = os.listdir(default_path)

        if not files_and_folders:
            print(f"Default path is empty.\n {default_path}")
            print("Please enter the path manually.")
            path = input(f"Path [Default: {default_path}]: ")
            files_and_folders = os.listdir(path)

            if not files_and_folders:
                print("The path you entered is empty.")
                return 0

        songs_ids = [utils.extract_leading_number(s) + "\n" for s in files_and_folders]
        # Assuming utils is a module with required functions
        utils.create_songs_file()
        utils.add_songs_to_file(songs_ids)

    except Exception as e:
        print(f"Error reading the directory: {e}")

    return 0


def map_reader():
    utils.create_songs_file()
    utils.add_songs_to_file(utils.read_text_files())


if __name__ == "__main__":
    print("1-Map downloader\n2-Map reader\n3-Map scanner\n")
    while True:
        try:
            question = int(input("Which operation do you want to perform? (int)\n"))
            break
        except:
            print("Error, please try again with an integer.")
    if question == 1:
        print("Starting the Map Downloader process.")
        map_downloader()
        print("Map Downloader process has been completed.")
    elif question == 2:
        print("Starting the Map Reader process.")
        map_reader()
        print("Map Reader process has been completed.")
    elif question == 3:
        print("Starting the Map scanner procces.")
        map_scanner()
        print("Map scanner process has been completed.")
    else:
        print("You have made an incorrect entry.")
    print("Closing the program.")
