from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
import time


class FollowerBot:
    def __init__(self, driver_path):
        s = Service(driver_path)
        self.driver = webdriver.Chrome(service=s)
        self.num_followers = 0
        self.num_following = 0

    def login(self, my_username, my_password):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(4)
        username_box = self.driver.find_element(By.NAME, 'username')
        username_box.send_keys(my_username)
        password_box = self.driver.find_element(By.NAME, 'password')
        password_box.send_keys(my_password)
        password_box.send_keys(Keys.RETURN)
        time.sleep(4)

    def count_followers(self, account):
        self.driver.get(f'https://www.instagram.com/{account}/')
        time.sleep(6)
        num_followers = self.driver.find_elements(By.CLASS_NAME, '_ac2a')[1]  # posts, followers
        num_followers = num_followers.get_attribute('title')
        if ',' in num_followers:
            count = int(''.join(num_followers.split(',')))
        else:
            count = int(num_followers)
        print(count)
        self.num_followers = count
        time.sleep(4)

    def count_following(self, account):
        self.driver.get(f'https://www.instagram.com/{account}/')
        time.sleep(6)
        num_followers = self.driver.find_elements(By.CLASS_NAME, '_ac2a')[2]  # posts, followers, following
        num_followers = num_followers.get_attribute('title')
        if ',' in num_followers:
            count = int(''.join(num_followers.split(',')))
        else:
            count = int(num_followers)
        print(count)
        self.num_following = count
        time.sleep(4)

    def follow(self, account):
        self.driver.get(f'https://www.instagram.com/{account}/followers/')
        time.sleep(4)
        follow_counter = 0
        while follow_counter <= self.num_followers:
            list_of_followers = self.driver.find_elements(By.CSS_SELECTOR, 'button')
            for item in list_of_followers[6 + follow_counter:]:
                if item.text == 'Follow':
                    print('Follow')
                    item.click()
                    time.sleep(round(random.random()) + 1)
                follow_counter += 1
            # buttons = self.driver.find_elements(By.XPATH, '//*[@class=\'_aacl _aaco _aacw _adda _aad6 _aade\']')
            button = list_of_followers[6]
            print(len(button))
            time.sleep(1)
            for _ in range(5):
                button.send_keys(Keys.PAGE_DOWN)  # message, follow, follow follower1
        time.sleep(4)

    def get_followers(self, account):
        self.driver.get(f'https://www.instagram.com/{account}/followers/')
        time.sleep(4)
        follow_counter = 0
        is_true = True
        follower_list = []
        while is_true:
            list_of_followers = self.driver.find_elements(By.XPATH, '//*[@class=\' _ab8y  _ab94 _ab97 _ab9f _ab9k _ab9p _abcm\']')
            for item in list_of_followers[follow_counter:]:
                follower_list.append(item.text)
                follow_counter += 1
                if follow_counter == self.num_followers:
                    is_true = False
                    break
            # buttons = self.driver.find_elements(By.XPATH, '//*[@class=\'_aacl _aaco _aacw _adda _aad6 _aade\']')
            button = self.driver.find_elements(By.CSS_SELECTOR, 'button')[6]
            # print(len(button))
            time.sleep(1)
            for _ in range(5):
                button.send_keys(Keys.PAGE_DOWN)  # message, follow, follow follower1
        time.sleep(4)
        # print(follower_list)
        return follower_list

    def get_following(self, account):
        self.driver.get(f'https://www.instagram.com/{account}/following/')
        time.sleep(4)
        follow_counter = 0
        is_true = True
        following_list = []
        while is_true:
            list_of_following = self.driver.find_elements(By.XPATH, '//*[@class=\' _ab8y  _ab94 _ab97 _ab9f _ab9k _ab9p _abcm\']')
            for item in list_of_following[follow_counter:]:
                following_list.append(item.text)
                follow_counter += 1
                if follow_counter == self.num_following:
                    is_true = False
                    break
            # buttons = self.driver.find_elements(By.XPATH, '//*[@class=\'_aacl _aaco _aacw _adda _aad6 _aade\']')
            button = self.driver.find_elements(By.CSS_SELECTOR, 'button')[6]
            # print(len(button))
            time.sleep(1)
            for _ in range(5):
                button.send_keys(Keys.PAGE_DOWN)  # message, follow, follow follower1
        time.sleep(4)
        # print(follower_list)
        return following_list

    def quit(self):
        self.driver.quit()
