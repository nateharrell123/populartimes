import populartimes
import json
from datetime import date, datetime
import calendar

# from flask import Flask, jsonify, request
# from flask_cors import CORS


# # Instantiate app
# app = Flask(__name__)
# app.config.from_object(__name__)

# # Allow Cors access
# CORS(app, resources={r'/*': {'origins': '*'}})



# @app.route('/test', methods=['POST'])
# def GetBusyness():
#     place_id = request.args.get('place')
    
#     spot = populartimes.get_id("AIzaSyDASvg4ATeMQcAsocmem5kFdTMDw_NSJwo", place_id)
    
#     for key, value in spot.items():
#         if key == "current_popularity":
#             print(value)
#             return value
#         else:
#             return 'no data'


# # idk 
# if __name__ == '__main__':
#     app.run()


# dayOfWeek = calendar.day_name[my_date.weekday()] English
#print(dayOfWeek)
dayOfWeek = datetime.today().weekday()
currentTime = datetime.now().strftime('%H:%M:%S')




# Walmart Manhattan, KS (live busyness)
#spot = populartimes.get_id("AIzaSyDASvg4ATeMQcAsocmem5kFdTMDw_NSJwo", "ChIJqa09skLSvYcR47QwBQ73ShQ")

# Dirty Dawg's (not live)
notLive = populartimes.get_id("AIzaSyDASvg4ATeMQcAsocmem5kFdTMDw_NSJwo", "ChIJOWMYXHjSvYcRSvAfdxlP8fg")

for key, value in notLive.items():
    if key == "populartimes":
        print(value[dayOfWeek])
    


#print(currentTime)


# for key, value in spot.items():
#     if key == "current_popularity":
#         if value > 0:
#             print(value)
#         else:

