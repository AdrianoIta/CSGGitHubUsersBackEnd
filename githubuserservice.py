import requests
import databasehelper

def get_user_by_name(user_name):
    url = f'https://api.github.com/users/{user_name}/repos'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        user_info = []
        for item in data:
            user = {
                "user_name": item["owner"]["login"],
                "name": item["name"],
                "html": item["owner"]["html_url"],
                "language": item["language"],
                "description": item["description"]
            }
            user_info.append(user)
            save_or_update(user)
        return user_info, 200
    else:
        return "user not found", 404   
    
def save_or_update(new_data):
    data = databasehelper.collection.find_one(new_data)
    if data is None:
        databasehelper.save(new_data)
    else:
        changed = changed_user_data(data, new_data)
        filter = {"id": data["_id"]} 
        databasehelper.update(filter, changed)
            
def changed_user_data(data, new_data):
    attrs = {}
    changed_data = {}
        
    if data["user_name"] != ["user_name"]:
          attrs["user_name"] = new_data["user_name"]
    if data["name"] != new_data["name"]:
        attrs["name"] = new_data["name"]
    if data["html"] != new_data["html"]:
        attrs.html = new_data["html"]  
    if data["language"] != new_data["language"]:
        attrs.language = new_data["language"]   
    if data["description"] != new_data["description"]:
        attrs.description = new_data["description"]

    changed_data["$set"] = attrs
    return changed_data