from selenium import webdriver
import selenium
import time,re,os,sys
from sys import platform

dirname = os.path.dirname(__file__)

ord_num_list = []

#this is mktplcid inpupt which we use for link
mktplcid = input("Enter marketplaceId: ")


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)


if platform == "linux" or platform == "linux2":
    # linux
    path = resource_path('driver/chromedriver')
else:
    path = resource_path('driver/chromedriver.exe')
    # Windows...


def gath_data():
    while(True):
        try:
            print("using gath_data")
            ord_per_pg = driver.find_element_by_xpath("//li[@class='a-last']/a").click()
            time.sleep(5)
            ord_per_pg = driver.find_element_by_xpath("//select[@name='myo-table-results-per-page']/option[text()='100']").click()
            time.sleep(10)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                
            time.sleep(10)
            ord_num = driver.find_elements_by_xpath("//div[@class='cell-body-title']/a")
            pattern = r'[0-9]{3}\-[0-9]{7}\-[0-9]{7}'
            for i in ord_num:
                result = re.match(pattern, i.text)
                if result:
                    ord_num_list.append(i.text)
                else:
                    pass

        except Exception as e:
            print("no more pages  - "+str(e))
            break

print("\n\nProcessing.....")

# path = resource_path('driver/chromedriver.exe')
driver =webdriver.Chrome(path)
req=driver.get('https://sellercentral.amazon.com/home')

# writing email
#em = driver.find_element_by_id('ap_email')
#write_em = em.send_keys("shijiliang@ewonder.cn")

# writing pass
# pas = driver.find_element_by_id('ap_password')
# write_pas = pas.send_keys("abs")

# remembername
# em = driver.find_element_by_name("rememberMe")

# while(True):
#     if(driver.title == "Amazon Sign-In"):
#         print("waiting for sign in...")
#         time.sleep(10)
#     else:
            
#         # click didnt recieve
#         didnt = driver.find_element_by_id("auth-get-new-otp-link").click()

#         # click text me
#         textme = driver.find_element_by_name("otpDeviceContext").click()

#         # send otp
#         sendopt = driver.find_element_by_id("auth-send-code").click()
#         break

while(True):
    # getting title
    current_title = driver.title
    if(current_title != "Amazon"):
        print("waiting for user to input at: "+current_title)
        time.sleep(10)
    else:
        print("Going for further... ")
        time.sleep(5)
        driver.get("https://sellercentral.amazon.com/orders-v3/fba/all?page=1&date-range=last-30")
        time.sleep(5)
        ord_per_pg = driver.find_element_by_xpath("//select[@name='myo-table-results-per-page']/option[text()='100']").click()
        time.sleep(10)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        
        time.sleep(10)
        ord_num = driver.find_elements_by_xpath("//div[@class='cell-body-title']/a")
        pattern = r'[0-9]{3}\-[0-9]{7}\-[0-9]{7}'
        for i in ord_num:
            result = re.match(pattern, i.text)
            if result:
                ord_num_list.append(i.text)
            else:
                pass
        gath_data()
        
        #removing dublicate elements frozensetom listt
        ord_num_list = list(dict.fromkeys(ord_num_list))
        for e in ord_num_list:
            driver.get("https://sellercentral.amazon.com/messaging/reviews?orderId="+e+"&marketplaceId="+mktplcid)
            try:
                
                time.sleep(3)
                yes_click = driver.find_element_by_xpath("//div[@class='ayb-reviews-button-container']/kat-button/button").click()
                print("clicking yes..and going to next..")
            except Exception as e:
                print("Cant find yes button or - " + str(e))
                
        break
#driver.close()
print("No. of order fetched: "+str(len(ord_num_list)))
print("\n\nComplete....")
#https://sellercentral.amazon.com/orders-v3/fba/all?page=1&date-range=last-30




