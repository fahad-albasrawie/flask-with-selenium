from flask import Flask, render_template, request
#from madsbu import get_player_name
#------------------------------
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#-------------------------------


'''

#---------------------
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
def get_player_name(playerId):
    while True:
        try:            #"https://www.midasbuy.com/midasbuy/ot/buy/pubgm"  
            browser.get('https://www.midasbuy.com/midasbuy/ot/buy/pubgm') # data Entry page
            break
        except:
            print("Qalad baan la kulmeyna...")
    #browser.maximize_window() # For maximizing window
    #browser.implicitly_wait(20) # gives an implicit wait for 20 seconds
    try:
        PlayerIdElem = browser.find_element(By.CLASS_NAME, 'input')
        PlayerIdElem.send_keys(playerId)
        print("Waan gelinay xog...")
        counter = 1
        while True:
            try:
                PlayerIdElem.send_keys(Keys.ENTER)
                counter +=1
                print("Waan helnay...", counter)
                #nickname = browser.find_elements(By.CLASS_NAME, 'label').text
                #nickname1 = browser.find_elements(By.CLASS_NAME, 'pay-id-mess').text
                nickname2 = browser.find_elements(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[3]/div/div/div/div[1]/div[1]/p")
                for i in nickname2:
                    print(i.text)
                    player = i.text
                # browser.quit()
                break
            except Exception as exc:
                print("Wali", exc)

                counter +=1 

    except Exception as exc:
        print("Qadalad baa jiree sug...", exc)

    return player
#---------------------
'''

app = Flask("__name__")

@app.route("/", methods=["POST", "GET"])
def home():
    # 
    return render_template("index.html")
    #return render_template("output.html", playerID=playerID)


@app.route("/output", methods=["POST", "GET"])
def check_plyer_id():
    playerInfo = {"plyerId": '', "playerName": 'Haddaan ka shaqaynaynaa...'}
    playerID = request.form.get("id_box")
    #player_name = get_player_name(playerID)
    player_name = "Fahad"
    playerInfo['plyerId'] = playerID
    playerInfo['plyerId'] = player_name
    
    
    print(playerID)
    
    return render_template("output.html", playerInfo=playerInfo)

if __name__ == "__main__":
    #app.run(debug=True)
    app.run()