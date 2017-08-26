import pickle
import math
def calc(book1, book2):
    cos = 0
    book1 = set(book1["tags"])
    book2 = set(book2["tags"])
    if (math.sqrt(len(book1)) * math.sqrt(len(book2))) != 0:
        cos = len(book1 & book2)/(math.sqrt(len(book1)) * math.sqrt(len(book2)))
    else:
        cos = 0
    return cos
print("Loading...")
with open("ehdataset",'rb') as file:
    dataset = pickle.load(file)
while True:
    print('Please enter gid:')
    gid = input()
    sample = [item for item in dataset if str(item["gid"]) == gid]
    if len(sample) == 0:
        print("Invaild gid! The dataset maximum gid is {0}".format(dataset[-1:][0]["gid"]))
        continue
    for i in dataset:
        i["cos"] = calc(sample[0], i)
    dataset.sort(key=lambda x:x["cos"], reverse=True)
    for i in dataset[0:20]:
        if i["title_jpn"]:
            print("{0}    gid:{1}    like:{2}    rate:{3}".format(i["title_jpn"],i["gid"],i["Favorited"],i["rating"]))
        else:
            print("{0}    gid:{1}    like:{2}    rate:{3}".format(i["title"],i["gid"],i["Favorited"],i["rating"]))
