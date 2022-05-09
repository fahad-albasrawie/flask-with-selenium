from flask import Flask, render_template, request
#from webscraping import get_player_name

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
    #player_name = "Fahad"
    playerInfo['plyerId'] = playerID
    #playerInfo['playerName'] = player_name
    
    
    print(playerID)
    
    return render_template("output.html", playerInfo=playerInfo)

if __name__ == "__main__":
    #app.run(debug=True)
    app.run()