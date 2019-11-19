import datetime
import time
import requests
from selenium import webdriver


TIMEOUT = 5
USERNAME = 'username'
PASSWORD = 'password'
DRIVER_PATH = 'path of chromedriver'
GW_URL = 'groupware url'
ATTEND_URL = GW_URL + '/app/home'
LOGIN_URL = GW_URL + '/login'


class AttendMachine:
    def __init__(self):
        print('Initializing attend machine...')
        self.is_connected = False
        self.driver = None

    def check_internet(self):
        print('Checking internet...')
        try:
            _ = requests.get(LOGIN_URL, timeout=TIMEOUT)
            self.is_connected = True
            print('Connected.')
            return True
        except requests.ConnectionError:
            print("Internet connection is bad...")
        return False

    def get_login_page(self):
        while not self.check_internet():
            print('Waiting connection')
            time.sleep(1)

        self.driver.get(LOGIN_URL)

        cnt = 0
        while self.driver.title != '로그인' \
                and self.driver.title != 'Sign In':
            print('Connecting to login page...')
            time.sleep(1)
            cnt += 1

            if cnt > 10:
                print('Attempts Exceed. Please check Internet connection.')
                return False

        print('Connected.')
        return True

    def get_attend_page(self):
        print('Connecting to attend page...')
        self.driver.get(ATTEND_URL)

        cnt = 0
        while str(self.driver.title).find('DaouOffice') == -1:
            time.sleep(1)
            cnt += 1

            if cnt > 10:
                print('Attempts Exceed. Please check Internet connection.')
                raise ConnectionError
        return True

    def init_chrome(self):
        if self.driver:
            return True

        print('Initializing web driver...')
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument("window-size=1920x1080")
        options.add_argument("--no-sandbox")
        options.add_argument("disable-gpu")
        self.driver = webdriver.Chrome(DRIVER_PATH, options=options)
        return True

    def login(self):
        self.get_login_page()

        print('Sending username...')
        self.driver.find_element_by_name('username').send_keys(USERNAME)

        print('Sending password...')
        self.driver.find_element_by_name('password').send_keys(PASSWORD)

        print('Signing in...')
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/section/fieldset/a').click()
        time.sleep(5)

    def attend_in(self):
        print('Attending in...')
        self.get_attend_page()
        self.driver.find_element_by_xpath('//*[@id="attndGadgetClockIn"]').click()
        print('Attended in at %s' % str(datetime.datetime.now()))

    def attend_out(self):
        print('Attending out...')
        self.get_attend_page()
        self.driver.find_element_by_xpath('//*[@id="attndGadgetClockOut"]').click()
        print('Attended out at %s' % str(datetime.datetime.now()))


def main():
    machine = AttendMachine()
    machine.init_chrome()
    machine.login()

    if not datetime.datetime.today().hour >= 18:
        machine.attend_in()
    else:
        machine.attend_out()


if __name__ == "__main__":
    main()
