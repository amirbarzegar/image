import simplejson as json
import os
if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size != 0:
    old_file=open("./ages.json" , "r+")
    data=json.loads(old_file.read())
    print("current age is " , data["age"] , "--- adding year")
    data["age"]= data["age"] +1
    print ("now the age is " , data["age"])
else:
    old_file= open("./ages.json", "w+")
    data={"name": "Amir" , "age": 27}
    print("No file found", "the difault age is " , data["age"] )
old_file.seek(0)
old_file.write(json.dumps(data))


