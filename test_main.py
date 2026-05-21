from ProjectClass import ProjectClass
import json 

def serialized_date( test : ProjectClass ) -> dict:
    #Projets should be nested dictionaries?
    # try for now just to input one project
    data = {
        "project_name" : test.name,
        "time" : test.time 
    }

    return data

def get_json_data() -> dict: 
    with open('data.json', 'r') as f:
        data = json.load(f)
    return data

test = ProjectClass("test project", 5)
#data = serialized_date(test)


data = get_json_data()
print("placeholder")
    
