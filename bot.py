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
        time.sleep(6)

    def count_followers(self, account):
        self.driver.get(f'https://www.instagram.com/{account}/')
        time.sleep(6)
        num_followers = self.driver.find_elements(By.CLASS_NAME, '_ac2a')[1]  # posts, followers
        num_followers = num_followers.get_attribute('title')
        if ',' in num_followers:
            count = int(''.join(num_followers.split(',')))
        else:
            count = int(num_followers)
        self.num_followers = count
        time.sleep(4)

    def count_following(self, account):
        self.driver.get(f'https://www.instagram.com/{account}/')
        time.sleep(6)
        num_followers = self.driver.find_elements(By.CLASS_NAME, '_ac2a')[2]  # posts, followers, following
        num_followers = num_followers.get_attribute('innerText')
        if ',' in num_followers:
            count = int(''.join(num_followers.split(',')))
        else:
            count = int(num_followers)
        print(count)
        self.num_following = count
        time.sleep(4)
        

    def follow_followers(self, account, number):
        self.driver.get(f'https://www.instagram.com/{account}/followers/')
        time.sleep(4)
        old_num_followers = 0
        follow_counter = 0
        limit = int(number)
        try:
            button = self.driver.find_elements(By.XPATH, '//*[@class=\'_acan _acap _acas\']')[2]
        except IndexError:
            button = self.driver.find_elements(By.XPATH, '//*[@class=\'_acan _acap _acat\']')[1]
        cur_num_followers = len(self.driver.find_elements(By.XPATH, '//*[@class=\' _ab8y  _ab94 _ab97 _ab9f _ab9k _ab9p _abcm\']'))
        while cur_num_followers > old_num_followers:
            attempts = 0
            old_num_followers = cur_num_followers
            list_of_followers = self.driver.find_elements(By.XPATH, '//*[@class=\'_acan _acap _acas\']')
            for item in list_of_followers[2 + follow_counter:]:
                if item.text == 'Follow':
                    print('Follow')
                    item.click()
                    time.sleep(round(random.random()) + 0.5)
                follow_counter += 1
            if follow_counter >= limit:
                break
            for _ in range(20):
                button.send_keys(Keys.PAGE_DOWN)  # message, follow, follow follower1
            time.sleep(1)
            cur_num_followers = len(self.driver.find_elements(By.XPATH, '//*[@class=\' _ab8y  _ab94 _ab97 _ab9f _ab9k _ab9p _abcm\']'))
            while cur_num_followers == old_num_followers:
                time.sleep(0.5)
                cur_num_followers = len(
                    self.driver.find_elements(By.XPATH, '//*[@class=\' _ab8y  _ab94 _ab97 _ab9f _ab9k _ab9p _abcm\']'))
                attempts += 1
                if attempts == 12:
                    break
        print(f'Followers: {cur_num_followers}')


    def get_followers(self, account):
        self.driver.get(f'https://www.instagram.com/{account}/followers/')
        time.sleep(4)
        old_num_followers = 0

        button = self.driver.find_elements(By.CSS_SELECTOR, 'button')[6]
        cur_num_followers = len(self.driver.find_elements(By.XPATH, '//*[@class=\' _ab8y  _ab94 _ab97 _ab9f _ab9k _ab9p _abcm\']'))
        while cur_num_followers > old_num_followers:
            attempts = 0
            print(f'Followers obtained: {cur_num_followers}')
            old_num_followers = cur_num_followers
            for _ in range(5):
                button.send_keys(Keys.PAGE_DOWN)  # message, follow, follow follower1
            time.sleep(1)
            cur_num_followers = len(self.driver.find_elements(By.XPATH, '//*[@class=\' _ab8y  _ab94 _ab97 _ab9f _ab9k _ab9p _abcm\']'))
            while cur_num_followers == old_num_followers:
                time.sleep(0.5)
                cur_num_followers = len(self.driver.find_elements(By.XPATH, '//*[@class=\' _ab8y  _ab94 _ab97 _ab9f _ab9k _ab9p _abcm\']'))
                attempts += 1
                if attempts == 12:
                    break
        print(f'Followers: {cur_num_followers}')

        list_of_followers = self.driver.find_elements(By.XPATH, '//*[@class=\' _ab8y  _ab94 _ab97 _ab9f _ab9k _ab9p _abcm\']')
        follower_list = []
        follow_counter = 1
        for follower in list_of_followers:
            follower_list.append(follower.text)
            print(f'Adding {follow_counter}/{cur_num_followers}: {follower.text}')
            follow_counter += 1

        time.sleep(4)
        return follower_list

    def get_following(self, account):
        self.driver.get(f'https://www.instagram.com/{account}/following/')
        time.sleep(4)
        old_num_following = 0

        button = self.driver.find_elements(By.CSS_SELECTOR, 'button')[6]
        cur_num_following = len(self.driver.find_elements(By.XPATH, '//*[@class=\' _ab8y  _ab94 _ab97 _ab9f _ab9k _ab9p _abcm\']'))
        while cur_num_following > old_num_following:
            attempts = 0
            print(f'Following obtained: {cur_num_following}')
            old_num_following = cur_num_following
            for _ in range(5):
                button.send_keys(Keys.PAGE_DOWN)  # message, follow, follow follower1
            time.sleep(1)
            cur_num_following = len(self.driver.find_elements(By.XPATH, '//*[@class=\' _ab8y  _ab94 _ab97 _ab9f _ab9k _ab9p _abcm\']'))
            while cur_num_following == old_num_following:
                time.sleep(0.5)
                cur_num_following = len(self.driver.find_elements(By.XPATH, '//*[@class=\' _ab8y  _ab94 _ab97 _ab9f _ab9k _ab9p _abcm\']'))
                attempts += 1
                if attempts == 12:
                    break
        print(f'Followers: {cur_num_following}')

        list_of_followers = self.driver.find_elements(By.XPATH, '//*[@class=\' _ab8y  _ab94 _ab97 _ab9f _ab9k _ab9p _abcm\']')
        following_list = []
        follow_counter = 1
        for follower in list_of_followers:
            following_list.append(follower.text)
            print(f'Adding {follow_counter}/{cur_num_following}: {follower.text}')
            follow_counter += 1

        time.sleep(4)
        return following_list
    
    def get_not_following_back(self, account):
        my_followers = self.get_followers(account)
        my_following = self.get_following(account)
        not_following_back_list = []
        total_following = len(my_following)
        counter = 1
        for following in my_following:
            print(f'Checking following {counter}/{total_following}')
            if following not in my_followers:
                following = following.replace('\\nVerified', '')
                not_following_back_list.append(following)
        return not_following_back_list

    def quit(self):
        self.driver.quit()

