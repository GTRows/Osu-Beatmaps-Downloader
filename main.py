from selenium import webdriver
import time
import os


def dosya_isimleri(x):
    sayac = 0
    file_list = os.listdir(r"{}".format(x))
    for i in file_list:
        if i == "Failed":
            file_list.remove("Failed")
            continue
        i = i.split(" ")
        file_list[sayac] = i[0]
        sayac += 1
    del i, sayac
    return file_list


def reading(location="osu beatmaps yedekler.txt"):
    # Path gir sürekli
    file = open("osu beatmaps yedekler.txt", "r", encoding="utf-8")
    array = file.readlines()
    file.close()
    for i in array:
        array[array.index(i)] = int(i[:7])
    return array


def map_downloader(question, location=""):
    wait = lambda: time.sleep(3)

    browser = webdriver.Chrome()
    browser.get("https://osu.ppy.sh/home")
    wait()
    input("Giriş yapınız ve hazır olunca input giriniz.")

    wait()
    # dosyaları alma yeri
    if question == 1:
        file_list = dosya_isimleri(r"C:\Users\GTRows\AppData\Local\osu!\Songs")
    else:
        file_list = reading(location)
    failled_list = list()
    # for döngüsüne alınacak
    for i in file_list:
        # Dosyadan çekilecek kodlar
        browser.get("https://osu.ppy.sh/beatmapsets?nsfw=1&q={}&s=any".format(i))
        wait()
        # js='document.getElementsByClassName("fa-download")[0].click()'
        # browser.execute_script(js)   
        try:
            download_button = browser.find_element_by_xpath(
            "/html/body/div[7]/div/div[4]/div/div[2]/div/div/div/div/div/div/div[3]/div/a")
            download_button.click()
        except:
            failled_list.append(i)
        wait()
    if failled_list:
        print("Bazı mapleri indiremedim. İndiremediğim maplerin kodlarını error_list.txt dosyasına kaydettim.")
        file = open("error_list.txt", "w", encoding="utf-8")
        for errors in failled_list:
            file.write("{}\n".format(errors))
        file.close()
    
    time.sleep(25)
    print("benden bu kadar")
    input("Tamam mı:\n")
    browser.quit()


def map_scanner():
    file_list = dosya_isimleri(r"C:/Users/GTRows/AppData/Local/osu!/Songs")
    file = open("osu beatmaps yedekler", "w", encoding="utf-8")
    for i in file_list:
        file.write("{}\n".format(i))
    file.close()


def sualx():
    while True:
        x = input("Başka istediğiniz bir şey var mı?(y/n)\n")
        if x == "n" or x == "N":
            return 0
        elif x == "y" or x == "Y":
            return 1
        else:
            print("Yanlış girdiniz tekrar deneyiniz...")


while True:
    print("1-Map downloader\n2-Map scanner")
    while True:
        try:
            question = int(input("Hangi işlemi yapacaksınız? (int)\n"))
            break
        except:
            print("Hata lütfen tekrar deneyiniz")
    if question == 1:
        question = int(
            input("1-Dosyadan id çekmek\n2-Yedek dosyasından id çekmek\n\nHangi işlemi yapacaksınız? (int)\n"))
        if question == 1:
            map_downloader(1)
        else:
            map_downloader(2, input("Herhangi bir lokasyondan çekecekseniz yazınız.\nAynı dizindeyse boş bırakınız"))
    elif question == 2:
        map_scanner()
    if 1 != sualx():
        break