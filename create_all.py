import os
import json

with open("node_mvc.json", "r") as f:
    data = json.load(f)

src = None

def create_structure(dic):
    for key, value in dic.items():
        os.mkdir(key)
        if isinstance(value, list):
            for v in value:
                with open(key + "/" + v, "w") as f:
                    f.write("")
        else:
            os.chdir(key)
            create_structure(dic[key])
            os.chdir("..")


def start():
    global src
    if src != None:
        os.mkdir(src)
        os.chdir(src)

        create_structure(data)
        os.chdir("..")