import os
import json

with open("node_mvc.json", "r") as f:
    data = json.load(f)

os.mkdir("backend")
os.chdir("backend")

def create_structor(dic):

    for key, value in dic.items():
        os.mkdir(key)
        if isinstance(value, list):
            for v in value:
                with open(key + "/" + v, "w") as f:
                    f.write("")
        else:
            os.chdir(key)
            create_structor(dic[key])
            os.chdir("..")

create_structor(data)
os.chdir("..")