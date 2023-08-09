# Osu Beatmaps Downloader & Reader

This project is a utility for automatically downloading and reading Beatmaps from
the [Osu website](https://osu.ppy.sh/home).

## Description

The Osu Beatmaps Downloader & Reader includes two main functionalities:

1. **Map Downloader**: This function automatically downloads the Beatmaps from the Osu website based on the song IDs
   provided. The maps are saved for offline usage. If there is a failure in downloading any of the maps, it will save
   the song IDs in an error list.

2. **Map Reader**: This function scans a directory for text files containing song IDs, creates a list of these IDs, and
   then writes them into a new text file. This is used to manage and organize your song IDs.
3. **Map Scanner (Upcoming)**: This upcoming feature will scan the locally installed Osu maps, retrieve their IDs, and write them to a text file. This will provide a convenient way to keep track of your currently active maps.

## Setup

### Prerequisites

You need to have Python installed on your system to run this project. Additionally, Selenium WebDriver for Python is
required.

You can install Selenium WebDriver using pip:

- pip install selenium

For Chromedriver:

1. Visit the [Chromedriver download page](https://sites.google.com/chromium.org/driver/) and download the version that corresponds to your installed Chrome version.
2. Extract the executable from the downloaded file.
3. Place the executable in the root of the project directory (same location as your main script).


### Running the project

To run the project, you first need to clone it from the GitHub repository.

- git clone https://github.com/GTRows/OsuBeatMapsDownloader.git

Then navigate to the project directory:

- cd OsuBeatMapsDownloader

Now, you can run the script:

- python main.py

When running the script, you will be prompted to choose between the Map Downloader and the Map Reader. Enter `1` for Map
Downloader and `2` for Map Reader.

## Contributing

Contributions to this project are welcome. Feel free to fork the repository, make your changes, and submit a pull
request.

## License

This project is licensed under the terms of the MIT license.