from selenium import webdriver
from selenium.webdriver.common.by import By
import utils
import time
import os

# sleep time default 3
wait = lambda: time.sleep(3)


def map_downloader():
    wait = lambda: time.sleep(3)

    browser = webdriver.Chrome()
    browser.get("https://osu.ppy.sh/home")
    input("Please log in and press Enter when you're ready.")
    print("Starting the process.\n")
    # file fetching location

    songs_id = utils.read_songs_file()
    if not songs_id:
        print("Couldn't read the file or the file is empty.")
        return 0

    failed_list = list()

    for i in songs_id:
        browser.get(f"https://osu.ppy.sh/beatmapsets/{i}")
        wait()
        try:
            download_buttons = browser.find_elements(By.CSS_SELECTOR, ".btn-osu-big.btn-osu-big--beatmapset-header")
            download_button = download_buttons[0]
            download_button.click()
        except Exception as e:
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


def map_reader():
    utils.create_songs_file()
    utils.add_songs_to_file(utils.read_text_files())


if __name__ == "__main__":
    print("1-Map downloader\n2-Map reader")
    while True:
        try:
            question = int(input("Which operation do you want to perform? (int)\n"))
            break
        except:
            print("Error, please try again")
    if question == 1:
        print("Starting the Map Downloader process.")
        map_downloader()
        print("Map Downloader process has been completed.")
    elif question == 2:
        print("Starting the Map Reader process.")
        map_reader()
        print("Map Reader process has been completed.")
    else:
        print("You have made an incorrect entry.")
    print("Closing the program.")
