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





# Walmart Manhattan, KS
spot = populartimes.get_id("AIzaSyDASvg4ATeMQcAsocmem5kFdTMDw_NSJwo", "ChIJqa09skLSvYcR47QwBQ73ShQ")
my_date = date.today()
dayOfWeek = calendar.day_name[my_date.weekday()]

currentTime = datetime.now().strftime('%H:%M:%S')
print(currentTime)


# for key, value in spot.items():
#     if key == "current_popularity":
#         print(value)









# Code graveyard:

#days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# weekday = datetime.today().weekday()
# dayOfWeek = ""

# if weekday == 0:
#     dayOfWeek = days[0] # Monday
# if weekday == 1:
#     dayOfWeek = days[1] # Tuesday
# if weekday == 2:
#     dayOfWeek = days[2] # Wednesday
# if weekday == 3:
#     dayOfWeek = days[3] # Thursday
# if weekday == 4:
#     dayOfWeek = days[4] # Friday
# if weekday == 5:
#     dayOfWeek = days[5] # Saturday
# if weekday == 6:
#     dayOfWeek = days[6] # Sunday