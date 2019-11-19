from selenium import webdriver
import datetime
import time
import requests


TIMEOUT = 5
URL = 'groupware url'
USERNAME = 'username'
PASSWORD = 'password'
DRIVER_PATH = 'path of chromedriver'


def check_internet():
    try:
        _ = requests.get(URL, timeout=TIMEOUT)
        return True
    except requests.ConnectionError:
        print("Internet connection is bad...")
    return False


def get_chrome():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("headless")
    chrome_options.add_argument("window-size=1920x1080")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("disable-gpu")
    driver = webdriver.Chrome(DRIVER_PATH, chrome_options=chrome_options)
    return driver


def login(driver):
    driver.get(URL)
    driver.find_element_by_name('username').send_keys(USERNAME)
    driver.find_element_by_name('password').send_keys(PASSWORD)
    driver.find_element_by_xpath('//*[@id="loginForm"]/section/fieldset/a').click()
    time.sleep(5)
    return driver


def attend_in():
    driver = get_chrome()
    driver = login(driver)
    driver.find_element_by_xpath('//*[@id="attndGadgetClockIn"]').click()
    print('attend in at %s' % str(datetime.datetime.now()))


def attend_out():
    driver = get_chrome()
    driver = login(driver)
    driver.find_element_by_xpath('//*[@id="attndGadgetClockOut"]').click()
    print('attend in out %s' % str(datetime.datetime.now()))


def main():
    is_connected = False

    while not is_connected:
        if check_internet():
            is_connected = True
            print('Internet connected')
        else:
            time.sleep(5)
            print('Waiting internet connection')

    if datetime.datetime.today().hour >= 18:
        attend_out()
    else:
        attend_in()


if __name__ == "__main__":
    main()
