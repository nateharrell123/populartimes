import populartimes
import json
import time
from datetime import date, datetime # Monday is 0 and Sunday is 6
import calendar
from flask import Flask, jsonify, request
from flask_cors import CORS

def timeconvert(str1):
    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]
    elif str1[-2:] == "AM":
        return str1[:-2]
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]
    else:
        return str(int(str1[:2]) + 12) + str1[2:8]

dt=datetime.datetime.now()
print("Conversion Of Time ::",timeconvert(dt.strftime("%H:%M:%S")))


# # Instantiate app
app = Flask(__name__)
app.config.from_object(__name__)

# # # Allow Cors access
CORS(app, resources={r'/*': {'origins': '*'}})

# # # look up async tasks in Flask
# # # Flask doesn't understand async tasks
# # # https://flask.palletsprojects.com/en/2.0.x/async-await/ 
@app.route('/test', methods=['POST'])
async def GetBusyness():
    dayOfWeek = datetime.today().weekday()
    currentTime = int(datetime.now().strftime('%H'))

    place_id = request.args.get('place')

    spot = populartimes.get_id("AIzaSyDASvg4ATeMQcAsocmem5kFdTMDw_NSJwo", place_id)

    for key, value in spot.items():
        if key == "current_popularity":
            if value > 0 and value < 25:
                return "Not very busy!"
            elif value > 25 and value < 50:
                return "A little busy"
            elif value > 50 and value < 75: 
                return "Moderately busy"
            elif value > 75:
                return "Very busy"
        elif key == "populartimes":
            for item, val in value[dayOfWeek].items():
                print(val)
                if item == "data":
                    print(val[currentTime])
                    if val[currentTime] == 0:
                        return ""
                    if val[currentTime] > 0 and val[currentTime] < 25:
                        return "Not very busy!"
                    elif val[currentTime] > 25 and val[currentTime] < 50:
                        return "A little busy"
                    elif val[currentTime] > 50 and val[currentTime] < 75: 
                        return "Moderately busy"
                    elif val[currentTime] > 75:
                        return "Very busy"


# # # idk 
if __name__ == '__main__':
    app.run()


# Comfort Suites (not live)
#notLive = populartimes.get_id("AIzaSyDASvg4ATeMQcAsocmem5kFdTMDw_NSJwo", "ChIJoeLKJmjSvYcRkMwiBlv7DCI")

# dayOfWeek = datetime.today().weekday()
# currentTime = int(datetime.now().strftime('%H'))

# Walmart Manhattan, KS (live busyness)
# spot = populartimes.get_id("AIzaSyDASvg4ATeMQcAsocmem5kFdTMDw_NSJwo", "ChIJqa09skLSvYcR47QwBQ73ShQ")
# for key, value in spot.items():
#     if key == "populartimes":
#         for item, val in value[dayOfWeek].items():
#             if item == "data":
#                 print(val[currentTime])