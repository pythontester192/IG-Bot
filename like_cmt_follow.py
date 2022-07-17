from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time

def sleep_for_period_of_time():
    limit = random.randint(7,10)
    time.sleep(limit)

user = input("Enter your username: ")
pwd = input("Enter your password: ")

def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--lang=en")
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    browser.get("https://www.instagram.com")
    sleep_for_period_of_time()

    username_input = browser.find_element_by_css_selector("input[name='username']")
    password_input = browser.find_element_by_css_selector("input[name='password']")

    username_input.send_keys(user)
    password_input.send_keys(pwd)
    sleep_for_period_of_time()

    login_button = browser.find_element_by_xpath("//button[@type='submit']")
    login_button.click()
    sleep_for_period_of_time()

    hashtag = input("Enter your hashtag name: ")
    browser.get(f"https://www.instagram.com/explore/tags/{hashtag}")
    sleep_for_period_of_time()

    first_pic = browser.find_element_by_xpath("//div[@class='_aaq8']/div/div/div[1]/div[1]/a")
    first_pic.click()

    num_post = input("How many post you want to like and leave a comment: ")
    cmmt = input("Type your comment: ")
    sleep_for_period_of_time()

    for i in range(int(num_post)):

        # Like a post 
        like_post = browser.find_element_by_xpath("//section[@class= '_aamu _aat0']/span[1]/button")
        like_post.click()
        print("Liked!")
        sleep_for_period_of_time()

        #Comment on a post
        cmmt_post = browser.find_element_by_xpath("//textarea[@class='_ablz _aaoc']")
        cmmt_post.click()
        cmmt_post = browser.find_element_by_xpath("//textarea[@class='_ablz _aaoc focus-visible']")
        cmmt_post.send_keys(cmmt)
        cmmt_post.send_keys(Keys.ENTER)
        print("Commented!")
        time.sleep(5)

        #Follow the user of the post
        follow_user = browser.find_element(By.XPATH, '//button/div/div[contains(text(), "Follow")]')
        if follow_user.text == "Follow":
            follow_user.click()
            print("Followed!")
            sleep_for_period_of_time()
        else:
            pass
        
        #Move on to the next Post
        next_post = browser.find_element_by_xpath("//button[@class='_abl-']//*[name()='svg' and @aria-label='Next']")
        next_post.click()
        print("post " + str(i) + " done!")
        print("Next!")
        sleep_for_period_of_time()

    #Quit the Program
    answer = input("The programm finished! Click on 'e' to exit.. ")
    if answer.lower().startswith("e"):
        browser.quit()
        exit()

if __name__ == "__main__":
    main()
