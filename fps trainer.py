#[name,[time],randint1,randint2,[data with lock += 2 randints],[dataHistory],[data with lock without 2 randints]]
import pickle
import os
import datetime
import random
import configparser

if os.path.isfile("config.ini"):
    config = configparser.ConfigParser()
    config.read('config.ini')
else:
    with open('config.ini', 'w') as configfile:
        config = configparser.ConfigParser(allow_no_value=True)
        config['DEFAULT'] = {'SaveFileFolder' : 'accounts/','#don\'t change the file-extention if you are not sure of what it is' : None,
            'fileExtention' : 'mcld'}
        config.write(configfile)


path = config['DEFAULT']['SaveFileFolder']
fileExtention = config['DEFAULT']['fileExtention']

def checkSave(pickledData):
    def corruptedAccount():
        exit()
    name, list1, num1, num2, data1, data2, data3 = pickledData
    if data3[1] - data3[0] != data1[1] - data1[0] or data1[0] != data3[0] + (num1 * num2):
        input('Account Data Corrupted, Please find a way to fix it or create a new one')
        corruptedAccount()
        return False
    else:
        print('Account Loaded Correctly')
        return True

def closeAccount(name, list1, data1):
    def fixData(data):
        data[1] = data[1] - data[0]
        return data
    def scrambleData(data,num1,num2,key, num):
        data[0] = key + ((num1 * num2) * num)
        data[1] += data[0]
        return data
    global startTime
    closeTime = datetime.datetime.now()
    list1[0] = round(list1[0] + ((closeTime - startTime).total_seconds()) // 60)
    num1 = random.randint(0,1000)
    num2 = random.randint(0,1000)
    key = random.randint(0,10000)
    data1 = fixData(data1)
    pickle.dump([name, list1, num1, num2, scrambleData(list(data1),num1,num2,key,1), scrambleData(list(data1),num1,num2,key,2), scrambleData(list(data1),num1,num2,key,0)], open(f'{path}{name}.{fileExtention}', "wb" ) )

def stringToSeed(seedString): #turns everything into ther ASCII value
    seedList = []
    for x in seedString:
        seedList.append(ord(x))#change every character into its ASCII value
    seedString = ''.join([str(elem) for elem in seedList])#add list together into string
    seed = int(seedString)
    return seed

search = input('please give username\n>>>')
if os.path.exists(f'accounts/{search.lower()}.mcld'):
    print('user found')
    if checkSave(pickle.load( open(f'accounts/{search}.mcld', "rb" ))) == True:
        name, list1, num1, num2, data1, data2, data3 = pickle.load( open(f'{path}{search.lower()}.{fileExtention}', "rb" ))
        startTime = datetime.datetime.now()
        #closeAccount(name, list1, data1)
else:
    while True:
        print('user not found, do you want to create a new user with this name? Y/N')
        answer = input()
        match answer.lower(): #select chosen difficulty
            case 'y':
                pickle.dump([search.lower(), [0], 69, 420, [41325, 41325], [41325, 41325], [12345, 12345]], open(f'{path}{search.lower()}.{fileExtention}', "wb" ) )
                break
            case 'n':
                exit()





