import populartimes
import json
from flask import Flask, jsonify, request
from flask_cors import CORS


# Instantiate app
app = Flask(__name__)
app.config.from_object(__name__)

# Allow Cors access
CORS(app, resources={r'/*': {'origins': '*'}})



@app.route('/test', methods=['POST'])
def GetBusyness():
    print(request.args)
    # spot = populartimes.get_id("AIzaSyDASvg4ATeMQcAsocmem5kFdTMDw_NSJwo", "ChIJL2TntXnSvYcRvdwEv_SZehA")
    # for key, value in spot.items():
    #     if key == "current_popularity":
    #         print(value)
    return 'this works!'


# idk 
if __name__ == '__main__':
    app.run()