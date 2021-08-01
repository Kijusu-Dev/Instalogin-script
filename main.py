from selenium import webdriver
import time

def InstaLogin(driver, name='', passw=''):
    driver.get("https://www.instagram.com/?hl=fr")
    try:
        driver.find_element_by_css_selector(
            "button.aOOlW.bIiDR"
        ).click()

        time.sleep(0.5)

        driver.find_element_by_name(
            "username"
        ).send_keys(
            name
        )
        driver.find_element_by_name(
            "password"
        ).send_keys(
            passw
        )

        driver.find_element_by_css_selector(
            "button.sqdOP.L3NKy.y3zKF"
        ).click()
        time.sleep(1)
    except:
        error = print("User or password incorrect")
        return error

n= input("\nEmail or\nUsername or\nPhone number\n\nEnter -> ")
p= input("Password -> ")
driver = webdriver.Chrome(executable_path="chromedriver.exe")
InstaLogin(driver, name=n, passw=p)