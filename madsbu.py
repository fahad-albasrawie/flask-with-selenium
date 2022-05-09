from selenium import webdriver
#from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys




def get_player_name(playerId):
        
    #playerId = input("Muumin, geli aqoonsiga ciyaaraha geemka: ")

    s = Service("C:/Users/djkha/OneDrive/Desktop/HUPORTALProject/geckodriver/geckodriver.exe")
    browser = webdriver.Firefox(service=s)
    while True:
        try:            #"https://www.midasbuy.com/midasbuy/ot/buy/pubgm"  
            browser.get('https://www.midasbuy.com/midasbuy/ot/buy/pubgm') # data Entry page
            break
        except:
            print("Qalad baan la kulmeyna...")
    #browser.maximize_window() # For maximizing window
    browser.implicitly_wait(20) # gives an implicit wait for 20 seconds
    #while True:
    try:
        PlayerIdElem = browser.find_element(By.CLASS_NAME, 'input')
        #playerId = "5425367899"
        #x = "5425367899"
        #PlayerIdElem.send_keys("")
        
        
        PlayerIdElem.send_keys(playerId)
        print("Waan gelinay xog...")
        counter = 1
        while True:
            


            try:
                
                PlayerIdElem.send_keys(Keys.ENTER)

                class2 = "pc-show-mod"
                
                counter +=1
                print("Waan helnay...", counter)
                #nickname = browser.find_elements(By.CLASS_NAME, 'label').text
                #nickname1 = browser.find_elements(By.CLASS_NAME, 'pay-id-mess').text
                nickname2 = browser.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[3]/div/div/div/div[1]/div[1]/p")
                

                for i in nickname2:
                    print(i.text)
                    player = i.text
                    
                
                #print(f"The Nickname of {playerId} is : {nickname1, nickname1}")
                browser.quit()
                break
            except Exception as exc:
                print("Wali", exc)

                counter +=1 

    except Exception as exc:
        print("Qadalad baa jiree sug...", exc)

    return player

id = input('Geli Id-Ga: ')
player_name = get_player_name(id)


