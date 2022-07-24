from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
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
    time.sleep(5)

    username_input = browser.find_element_by_css_selector("input[name='username']")
    password_input = browser.find_element_by_css_selector("input[name='password']")

    username_input.send_keys(user)
    password_input.send_keys(pwd)
    sleep_for_period_of_time()

    login_button = browser.find_element_by_xpath("//button[@type='submit']")
    login_button.click()
    sleep_for_period_of_time()

    # not_now = browser.find_element_by_xpath("//div[@class='cmbtv']/button")
    # not_now.click()
    # sleep_for_period_of_time()

    ig_user = input("Enter your instagram username: ")
    browser.get(f"https://www.instagram.com/{ig_user}")
    sleep_for_period_of_time()

    followers_link = browser.find_element_by_xpath("//ul/li[3]/a")
    followers_link.click()
    sleep_for_period_of_time()

    num_unfollow = input("How many person you want to unfollow: ")

    while(True):
        try:
            i = 0
            list_of_following = browser.find_elements(By.XPATH, '//button/div/div[contains(text(), "Following")]')
            for person in list_of_following:
                if person.text == "Following":
                    person.click()
                    time.sleep(5)
                    unfollow_btn = browser.find_element_by_xpath('//button[text()= "Unfollow"]')
                    unfollow_btn.click()
                    print("Unfollowed!")
                    i +=1
                    print(i)
                    sleep_for_period_of_time()
                else:
                    pass
                if i >= int(num_unfollow):
                    break
            
            browser.execute_script("arguments[0].scrollIntoView(true);", list_of_following[i])

            answer = input("The programm finished! Click on 'e' to exit.. ")
            if answer.lower().startswith("e"):
                browser.quit()
                exit()

        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()

