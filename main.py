import json
from pathlib import Path


def proc1():
    file = open(Path("resourses", "1.json"))
    data = json.load(file)
    for i in data["products"]:
        print("Name: ", i["name"])
        print("Price: ", i["price"])
        print("Weight: ", i["weight"])
        print("Available" if i["available"] else "Out of stock", "\n")


def proc2():
    print("Send -1 to exit")
    add_list = {"products": []}
    while (True):
        name = input("Name: ")
        if name == "-1":
            break

        price = int(input("Price: "))
        weight = int(input("Weight: "))
        available = bool(input("Is available 0/1: "))
        add_list["products"].append({"name": name, "price": price, "weight": weight, "available": available})

    file = open(Path("resourses", "1.json"))
    data = json.load(file)

    data["products"].extend(add_list["products"])
    file.close()
    file = open(Path("resourses", "1.json"), "w")
    json.dump(data, file, indent=4, ensure_ascii=False)


def proc3():
    dict = {}
    file = open(Path("resourses", "en-ru.txt"), "r")
    for line in file:
        orig = line.split("-")[0].strip()
        trans = line.split("-")[1].strip().split(',')
        for i in trans:
            i = i.strip()
            if i in dict.keys():
                dict[i] = dict[i] + ", " + orig
            else:
                dict[i] = orig
    srt = sorted(dict.keys())
    file.close
    file = open(Path("resourses", "ru-en.txt"), "w")
    for i in srt:
        file.writelines(i + "- " + dict[i] + "\n")


