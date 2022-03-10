from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def main():
    driver = webdriver.Chrome()
    driver.get("https://vk.com")
    #input("Press Enter to continue...")
    
    textBoxLogin = driver.find_element(By.ID,"index_email").click()
    textBoxLogin = driver.find_element(By.ID,"index_email").send_keys("")#вставить логин
    textBoxPass = driver.find_element(By.ID,"index_pass").click()
    textBoxPass = driver.find_element(By.ID,"index_pass").send_keys("")#вставить пароль


    loginButton = driver.find_element(By.ID,"index_login_button").click()
    
    group = driver.find_element(By.XPATH,"//li[@id='l_gr']/a[@class='left_row']").click()#проблема в взаимодействием
    group = driver.find_element(By.XPATH,"//li[@id='l_gr']").click()#проблема в взаимодействием
    
    
    input("Press Enter to continue...")
    
    
    
if __name__ == "__main__":
    main()
