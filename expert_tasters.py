from database import Database

db = Database()

"""
Make sure all names are lower cases & phone are integers
"""

def get_experts(): 
    all_info = db.stream_all_user_info()
    result = {val.lower(): key["phone"] for val, key in all_info.items() if key["type"] == "expert"}
    return result

def get_tasters(): 
    all_info = db.stream_all_user_info()
    result = {val.lower(): key["phone"] for val, key in all_info.items() if key["type"] == "taster"}
    return result

EXPERTS = get_experts()

TASTERS = get_tasters()