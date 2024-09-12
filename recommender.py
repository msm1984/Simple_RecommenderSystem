import copy
import math
user_dict = {}
user1_dict = {}
item_dict = {}
test_dict = {}
def predict(u,a,lst):
    soorat = 0
    makh = 0
    for i in lst.keys():
        for j in user_dict[u]:
            if j[0] == i:
                soorat += lst[i] * j[1]
                makh += lst[i]
    if makh != 0:
        return soorat/makh
    return 3

def cosineSameItem(a,b,u,use):
    soorat = 0
    makh1 = 0
    makh2 = 0
    for key in use.keys():
        if(key != u):
            aExist = 0
            aValue = -1
            bValue = -1
            for i in user1_dict[key]:
                if i[0] == a:
                    aExist = 1
                    aValue = i[1]
                    break
            if aExist == 1:
                for i in user1_dict[key]:
                    '''if i[0] > b:
                        break'''
                    if i[0] == b:
                        bValue = i[1]
                        break
            if aValue != -1 and bValue != -1:
                soorat += (aValue)*(bValue)
                makh1 += (aValue)**2
                makh2 += (bValue)**2
    if makh1 != 0 and makh2 != 0:
        return soorat/(math.sqrt(makh1)*math.sqrt(makh2))
    return -1

def sameUser(a,b):
    soorat = 0
    makh1 = 0
    makh2 = 0
    for key in user1_dict[a]:
        for kk in user1_dict[b]:
            if kk[0] == key[0]:
                soorat += (key[1]) * (kk[1])
                makh1 = (key[1]) ** 2
                makh2 = (kk[1]) ** 2
                break
    if makh1 != 0 and makh2 != 0:
        return soorat/(math.sqrt(makh1)*math.sqrt(makh2))
    return -1

            


def isAdjust():
    for key in user1_dict.keys():
        sum = 0
        for j in user1_dict[key]:
            sum += j[1]
        avg = sum/len(user1_dict[key])
        for j in user1_dict[key]:
            j[1] = j[1] - avg
        '''for j in user_dict.keys():
            for x in user_dict[j]:
                if x[0] == key:
                    x[1] = x[1] - avg'''


with open('u1.base', 'r') as file:
    for line in file:
        parts = line.split()  
        key = int(parts[0])  
        value = [int(parts[1]), int(parts[2])]  
        if key not in user1_dict.keys():
            user1_dict[key] = []
        user1_dict[key].append(value)
        
        
        key1 = int(parts[1])  
        value1 = [int(parts[0]), int(parts[2])]  
        if key1 not in item_dict.keys():
            item_dict[key1] = [] 
        item_dict[key1].append(value1)  


with open('u1.test', 'r') as file:
    for line in file:
        parts2 = line.split()  
        key2 = int(parts2[0])  
        value2 = [int(parts2[1]), int(parts2[2])]  
        if key2 not in test_dict.keys():
            test_dict[key2] = []
        test_dict[key2].append(value2)

for i in user1_dict.keys():
    ff = user1_dict[i]
    user_dict[i] = copy.deepcopy(ff[:])


def main():
    summ = 0
    summ2 = 0
    makh = 0
    isAdjust()
    for l in test_dict.keys():
        dd = {}
        ll = {}
        myUser = test_dict[l]
        
        for p in myUser:
            for jj in user1_dict.keys():
                ll[jj] = sameUser(l,jj)
            ll = dict(sorted(ll.items(), key=lambda item: item[1]))
            pp = len(ll)
            ll = dict(list(ll.items())[pp-110: pp])
            for i in user_dict[l]:
                dd[i[0]] = cosineSameItem(i[0],p[0],l,ll)
            dd = dict(sorted(dd.items(), key=lambda item: item[1]))
            ff = len(dd)
            dd = dict(list(dd.items())[ff-20: ff]) 
            makh += 1
            print(p[1])
            summ += abs(predict(l,p[0],dd) - p[1])
            summ2 += abs(predict(l,p[0],dd) - p[1]) ** 2
            print(str(l) + " " + str(p[0]) + " " + str(predict(l,p[0],dd)))
    print("abslote:  " + str(summ/makh))
    print("root:  " + str(math.sqrt(summ2/makh)))

main()

