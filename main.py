from extractionFilesAndPrinting import get_all_files_names
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep
from user import User

global USER


def extract_and_save_data():
    # When the code does what it should for me, update here option using gui to get the source folder
    songs_folder_path = "D://Softwares//programming softwares//PythonProjects//SongsTransfer//Songs"
    outputs = get_all_files_names(songs_folder_path)
    song_and_artist_found = outputs[0]
    song_might_wont_find = outputs[1]
    file_names_not_songs = outputs[2]
    # print_extracted_names(song_and_artist_found, file_names_not_songs, song_might_wont_find)


def driver_creator():
    ids = ["login-username", "login-password"]
    chrome_driver_path = "chromedriver.exe"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    sr = Service(chrome_driver_path)
    driver = webdriver.Chrome(options=chrome_options, service=sr)
    driver.get("https://open.spotify.com/")
    sleep(2)
    driver.find_element(by=By.CSS_SELECTOR, value=".Button-sc-qlcn5g-0.jsmWVV").click()
    sleep(2)
    driver.find_element(by=By.ID, value=ids[0]).send_keys(USER.email)
    sleep(2)
    driver.find_element(by=By.ID, value=ids[1]).send_keys(USER.password)
    sleep(2)
    driver.find_element(by=By.CSS_SELECTOR, value=".Button-sc-qlcn5g-0.otMlU").click()
    sleep(3)

    # likeSongsCreatePlaylist_usingFullNames(driver)
    addingSongs(driver)
    driver.close()


def likeSongsViaSearch(driver):
    driver.get("https://open.spotify.com/search")
    sleep(2)
    search_bar = driver.find_element(by=By.CSS_SELECTOR,
                                     value=".Type__TypeElement-sc-goli3j-0.hGXzYa.QO9loc33XC50mMRUCIvf")
    with open(r'./FullNames.txt', 'r', encoding="utf-8") as f:
        for title in f:
            search_bar.send_keys(f.readline())
            sleep(3)
            # enter here action for liking the song
            search_bar.clear()
    f.close()


def printFile(file):
    for line in file:
        print(line)


def likeSongsCreatePlaylist_usingFullNames(driver):
    driver.find_element(by=By.CSS_SELECTOR, value=".IPVjkkhh06nan7aZK7Bx").click()
    sleep(2)
    search_bar = driver.find_element(by=By.CSS_SELECTOR,
                                     value=".Type__TypeElement-sc-goli3j-0.hGXzYa.FeWwGSRANj36qpOBoxdx")
    with open(r'./FullNames.txt', 'r', encoding="utf-8") as f:
        with open(r'./addFailed.txt', 'w', encoding="utf-8") as f2:
            with open(r'./added.txt', 'w', encoding="utf-8") as added:
                for title in f:
                    search_bar.send_keys(title)
                    sleep(2)
                    try:
                        driver.find_element(by=By.CSS_SELECTOR, value=".Button-sc-y0gtbx-0.lprIeE").click()
                        added.write(f"{title}")
                    except:
                        f2.write(f"{title}")
                    finally:
                        sleep(2)
                        search_bar.clear()


def addingSongs(driver):
    driver.get("https://open.spotify.com/playlist/6idHhXRPg5jQUF5jXPR3zX")
    sleep(2)
    driver.find_element(by=By.CSS_SELECTOR, value=".STDuzt77yRCueC4Ohenl").click()
    sleep(2)
    search_bar = driver.find_element(by=By.CSS_SELECTOR,
                                     value=".Type__TypeElement-sc-goli3j-0.hGXzYa.FeWwGSRANj36qpOBoxdx")
    with open(r'./SongsMightFail.txt', 'r', encoding="utf-8") as f:
        with open(r'./addFailed.txt', 'w', encoding="utf-8") as f2:
            with open(r'./added.txt', 'w', encoding="utf-8") as added:
                for title in f:
                    search_bar.send_keys(title)
                    sleep(2)
                    try:
                        driver.find_element(by=By.CSS_SELECTOR, value=".Button-sc-y0gtbx-0.lprIeE").click()
                        added.write(f"{title}")
                    except:
                        f2.write(f"{title}")
                    finally:
                        sleep(2)
                        search_bar.clear()




if __name__ == '__main__':
    # extract_and_save_data()
    USER = User(input("Please enter account email: "), input("Please enter account password: "))
    driver_creator()
