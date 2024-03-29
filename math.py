import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from os import path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(path.join(path.dirname(__file__),'chromedriver.exe'))
start_time = time.time()
for j in range(0, 1001):
    driver.get("https://tbot.xyz/math/#eyJ1IjoyMDk3MDI4NjAsIm4iOiJSb2RyaWsgIiwiZyI6Ik1hdGhCYXR0bGUiLCJjaSI6Ii04MjA3MTU5MDEwMjQ2NzIyMjk3IiwiaSI6IkJBQUFBQTVmQXdETXozOE1ueEtTRlA2VU9SYyJ9ODM2NjEwYThkZmEyZTY1ZjA5ZmE5ZjljMDc1MDM4YmI=&tgShareScoreUrl=tg%3A%2F%2Fshare_game_score%3Fhash%3Du5Rj08qAKPxqHUq0_uBMbueWind7mWtjNPZKubwHgtU")

    if (j == 0):
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'button_correct')))
    else:
        task_x = int(driver.find_element_by_id('task_x').text)
        task_y = int(driver.find_element_by_id('task_y').text)
        task_op = driver.find_element_by_id('task_op').text
        task_res = int(driver.find_element_by_id('task_res').text)

        if (task_op == '/'):
            result = task_x / task_y
            if (result == task_res):
                element = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, 'button_correct')))
            else: 
                element = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, 'button_wrong')))
        elif (task_op == '+'):
            result = task_x + task_y
            if (result == task_res):
                element = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, 'button_correct')))
            else:
                element = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, 'button_wrong')))
        elif (task_op == '–'):
            result = task_x - task_y
            if (result == task_res):
                element = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, 'button_correct')))
            else:
                element = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, 'button_wrong')))
        elif (task_op == '×'):
            result = task_x * task_y
            if (result == task_res):
                element = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, 'button_correct')))
                print("correct")
            else:
                element = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, 'button_wrong')))
                print('wrong')
        print(result, task_x, task_op, task_y)

    


    element.click()
time.sleep(5)
print("-------------")
print(time.time() - start_time)
print("-------------")
