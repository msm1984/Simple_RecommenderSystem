import pandas as pd
import math


user_item = pd.read_csv('u1.base',sep='\t',header=None,names=[
    "user_id",
    "item_id",
    "rating",
    "timestamp"
])


test = pd.read_csv('u1.test',sep='\t',header=None,names=[
    "user_id",
    "item_id",
    "rating",
    "timestamp"
])

print(user_item[user_item['user_id'] == 2].iloc[2]["item_id"])

itemsInfo = pd.read_csv('u.item',sep='|',header=None,encoding='latin-1',
names=[
    "movie_id",
    "movie_title",
    "release_date",
    "video_release_date",
    "IMDB_URL",
    "unknown",
    "Action",
    "Adventure",
    "Animation",
    "Children",
    "Comedy",
    "Crime",
    "Documentary",
    "Drama",
    "Fantasy",
    "Film-Noir",
    "Horror",
    "Musical",
    "Mystery",
    "Romance",
    "Sci-Fi",
    "Thriller",
    "War",
    "Western"
])

print(itemsInfo.head())


userInfo = pd.read_csv('u.user',sep='|',header=None,names=[
    "user_id",
    "age",
    "gender",
    "occupation",
    "zip_code"
])
generes = {0:"Action", 1:"Adventure", 2:"Animation", 3:"Children", 4:"Comedy", 5:"Crime", 6:"Documentary", 7:"Drama", 8:"Fantasy", 9:"Film-Noir", 10:"Horror", 11:"Musical", 12:"Mystery", 13:"Romance", 14:"Sci-Fi", 15:"Thriller", 16:"War", 17:"Western"}
def predict(user,item):
    testfilm = itemsInfo[itemsInfo["movie_id"] == item]
    dct = {}
    index = user
    testUser = user_item[user_item['user_id'] == user]
    for j in range(len(testUser)):
        film = itemsInfo[itemsInfo["movie_id"] == testUser.iloc[j]["item_id"]]
        soorat = 0
        makhraj = 0
        for z in range(18):
            #print(testfilm.iloc[0][generes[z]])
            if testfilm.iloc[0][generes[z]] == 1:
                makhraj += 1
                soorat += testfilm.iloc[0][generes[z]]*film.iloc[0][generes[z]]
        if makhraj > 0:
            dct[testUser.iloc[j]["item_id"]] = soorat/makhraj
        else:
            dct[testUser.iloc[j]["item_id"]] = 0
    dct = dict(sorted(dct.items(), key=lambda item: item[1]))
    ff = len(dct)
    dct = dict(list(dct.items())[ff-10: ff]) 
    avg = 0
    for i in dct.keys():
        avg += user_item[user_item['item_id'] == i].iloc[0]["rating"]
    return (avg/10)
'''ss = itemsInfo[itemsInfo["movie_id"] == 5]   
for z in range(18):
    print(ss.iloc[0][generes[z]])'''
summ = 0
summ2 = 0
cnt = 0
for i in range(len(userInfo)):
    gg = test[test["user_id"] == i+1]
    for j in range(len(gg)):
        cnt += 1
        fgh = predict(i+1,gg.iloc[j]["item_id"])
        summ += abs(gg.iloc[j]["rating"] - fgh)
        summ2 += abs(gg.iloc[j]["rating"] - fgh) ** 2 


print(summ/cnt)
print(math.sqrt(summ2/cnt))

