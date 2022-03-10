from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def main():
    def smokeTest1(): #заходит на сайт и нажимает на кнопку
        driver = webdriver.Chrome()
        driver.get("https://castlots.org/generator-igralnyh-kart/")
        btn_elem = driver.find_element(By.CLASS_NAME,"random-button")
        btn_elem.click()
        input("Press Enter to continue...")
        
    def smokeTest2():# без трефов и бубнов
        driver = webdriver.Chrome()
        driver.get("https://castlots.org/generator-igralnyh-kart/")
        
        check_elem1 = driver.find_element(By.ID,"check-b")
        check_elem2 = driver.find_element(By.ID,"check-t")
        check_elem1.click()
        check_elem2.click()

        btn_elem = driver.find_element(By.CLASS_NAME,"random-button")
        btn_elem.click()

        input("Press Enter to continue...")
        
    def smokeTest3():# выбор формата колоды 36-54 и масти черви
        driver = webdriver.Chrome()
        driver.get("https://castlots.org/generator-igralnyh-kart/")

        check_elem1 = driver.find_element(By.ID,"check-b")
        check_elem2 = driver.find_element(By.ID,"check-t")
        check_elem1.click()
        check_elem2.click()
        
        check_elem3 = driver.find_element(By.ID,"check-p")
        check_elem3.click()
        
        check_elem4 = driver.find_element(By.NAME,"number")
        check_elem4.click()

        btn_elem = driver.find_element(By.CLASS_NAME,"random-button")
        btn_elem.click()

        input("Press Enter to continue...")
    
    def smokeTest4():
        driver = webdriver.Chrome()
        driver.get('https://castlots.org/generator-igralnyh-kart/')

        slider = driver.find_element_by_css_selector("ui-slider-handle ui-state-default ui-corner-all")
        move = ActionChains(driver)
        move.click_and_hold(slider).move_by_offset(0, 50).release().perform()
        btn_elem = driver.find_element(By.CLASS_NAME,"random-button")
        btn_elem.click()
        
        input("Press Enter to continue...")
        
    smokeTest1()
    smokeTest2()
    smokeTest3()
    smokeTest4()
    
    
if __name__ == "__main__":
    main()
