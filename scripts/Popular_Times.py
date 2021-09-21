import populartimes
import json

spot = populartimes.get_id("AIzaSyDASvg4ATeMQcAsocmem5kFdTMDw_NSJwo", "ChIJL2TntXnSvYcRvdwEv_SZehA")

for key, value in spot.items():
    if key == "current_popularity":
        print(value)
        