import populartimes
import json
import time
from datetime import date, datetime # Monday is 0 and Sunday is 6
import calendar
from flask import Flask, jsonify, request
from flask_cors import CORS


# Instantiate app
app = Flask(__name__)
app.config.from_object(__name__)

# Allow Cors access
CORS(app, resources={r'/*': {'origins': '*'}})

# look up async tasks in Flask
# Flask doesn't understand async tasks
# https://flask.palletsprojects.com/en/2.0.x/async-await/ 
@app.route('/test', methods=['POST'])
async def GetBusyness():
    dayOfWeek = datetime.today().weekday()
    currentTime = int(datetime.now().strftime('%H'))

    place_id = request.args.get('place')
    spot = populartimes.get_id("AIzaSyDASvg4ATeMQcAsocmem5kFdTMDw_NSJwo", "ChIJqa09skLSvYcR47QwBQ73ShQ")

    print(spot)

    for key, value in spot.items():
        if key == "current_popularity":
            print(value)
            if value > 0 and value < 25:
                return "Not very busy!"
            elif value > 25 and value < 50:
                return "A little busy"
            elif value > 50 and value < 75: 
                return "Moderately busy"
            elif value > 75:
                return "Very busy"
        if key == "populartimes":
            for item, val in value[dayOfWeek].items():
                if item == "data":
                    # return val[currentTime]
                    return "asdf"
        else:
            return "No population data for this establishment."


# idk 
if __name__ == '__main__':
    app.run()

# Dirty Dawg's (not live)
#notLive = populartimes.get_id("AIzaSyDASvg4ATeMQcAsocmem5kFdTMDw_NSJwo", "ChIJOWMYXHjSvYcRSvAfdxlP8fg")

# Walmart Manhattan, KS (live busyness)
# spot = populartimes.get_id("AIzaSyDASvg4ATeMQcAsocmem5kFdTMDw_NSJwo", "ChIJqa09skLSvYcR47QwBQ73ShQ")
# for key, value in spot.items():
#     if key == "current_popularity":
#         if value > 0 and value < 25:
#             print(value)
#         elif value > 25 and value < 50:
#             print(value)
#         elif value > 50 and value < 75: 
#             print(value)
#         elif value > 75:
#             print(value)