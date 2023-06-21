from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_pytest:

    def test_credence(self):
        driver = webdriver.Chrome()
        driver.get("https://credence.in/")
        driver.find_element(By.XPATH,"//img[@src='/website/images/enquiry.png']").click()
        l = len(driver.find_elements(By.XPATH,"//div[@class = 'quickfinder-description gem-text-output']//p//a"))
        print(l)
        contact_Number_list = []
        for r in range(1,l+1):
            contact_Number = driver.find_element(By.XPATH, "//div[@class='quickfinder-description gem-text-output']//p//a[" + str(r) + "]").text
            print(contact_Number)
            contact_Number_list.append(contact_Number)
        mn = "+91 8983282704"
        if mn in contact_Number_list:
            print(contact_Number_list.index(mn))
            assert True
        else:
            assert False