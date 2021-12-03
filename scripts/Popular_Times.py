import populartimes
from datetime import date, datetime # Monday is 0 and Sunday is 6
from flask import Flask, jsonify, request
from flask_cors import CORS

# Instantiate app
app = Flask(__name__)
app.config.from_object(__name__)

# Allow Cors access
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/test', methods=['POST'])
async def GetBusyness():
    dayOfWeek = datetime.today().weekday()
    currentTime = int(datetime.now().strftime('%H'))

    place_id = request.args.get('place')

    spot = populartimes.get_id("AIzaSyDASvg4ATeMQcAsocmem5kFdTMDw_NSJwo", place_id)

    for key, value in spot.items():
        if key == "current_popularity":
            if value >= 0 and value <= 20:
                return "Not busy."
            elif value > 20 and value <= 40:
                return "A little busy."
            elif value > 40 and value <= 60: 
                return "Moderately busy."
            elif value > 60 and value <= 80:
                return "Very busy."
            elif value > 80:
                return "Extremely busy."
        elif key == "populartimes":
            for item, val in value[dayOfWeek].items():
                if item == "data":
                    if val[currentTime] > 0 and val[currentTime] <= 20:
                        return "Not busy."
                    elif val[currentTime] > 20 and val[currentTime] <= 40:
                        return "A little busy."
                    elif val[currentTime] > 40 and val[currentTime] <= 60: 
                        return "Moderately busy."
                    elif val[currentTime] > 60 and val[currentTime] <= 80:
                        return "Very busy."
                    elif val[currentTime] > 80:
                        return "Extremely busy."
                        

if __name__ == '__main__':
    app.run()