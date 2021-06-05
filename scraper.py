from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dato import *
import time
import json
import re
from Facebook_Scraper_POST import Facebook_Scraper_POST
from managerFile import readJson,writeJson
import phpFunctions as php

if __name__ == "__main__":
    
    PATH = "chromedriver.exe"
    h = Facebook_Scraper_POST(PATH)
    h.loginSession(URL=URL_LOGIN,user=user[3],password=password[3])
   
    res = 0
    
    '''
    #Se obtienen comentarios y respuestas
    time.sleep(1)
    dataComments = h.getComments('https://m.facebook.com/groups/413938496303058/permalink/469954730701434', '469954730701434')
    
    print(dataComments)
    
    for i in range(len(dataComments)):
        
        
        if res == -1:
            break
        print(dataComments[i]['primaryComment'])
        res = php.insert('insertComment.php',dataComments[i]['primaryComment'])
        
        if len(dataComments[i]['secondaryComment'])>0:
            for j in range(len(dataComments[i]['secondaryComment'])):
                print(dataComments[i]['secondaryComment'][j])
                if res == -1:
                    break
                res = php.insert('insertSecondaryComment.php',dataComments[i]['secondaryComment'][j])
    
    '''
    #Se obtiene el post
    data=h.collectionPOST(URL_GROUP,100)
    
    for index in range(len(data)):
        if res == -1:
            break
        res = php.insert('insertPost.php', data[index])

        #Se obtienen comentarios y respuestas
        time.sleep(1)
        dataComments = h.getComments(data[index]['url'], data[index]['id'])
    
        for i in range(len(dataComments)):
            if res == -1:
                break
            res = php.insert('insertComment.php',dataComments[i]['primaryComment'])
            
            
            if len(dataComments[i]['secondaryComment'])>0:
                for j in range(len(dataComments[i]['secondaryComment'])):
                    if res == -1:
                        break
                    res = php.insert('insertSecondaryComment.php',dataComments[i]['secondaryComment'][j])
                    
        
        
        #Se obtiene quienes vieron el post
        time.sleep(1)
        dataView = h.getUsernames(data[index]['id'], URL_VISITED, 'view_names')
        
        for i in range(len(dataView['view_names'])):
            if res == -1:
                break
            res = php.insert('insertView.php', dataView['view_names'][i])
            
        #Se obtienen las compartidas
        time.sleep(1)
        dataShares = h.getUsernames(data[index]['id'], URL_SHARED, 'shared_names')
        
        for i in range(len(dataShares['shared_names'])):
            if res == -1:
                break
            res = php.insert('insertShare.php', dataShares['shared_names'][i])
            
        
        #Se obtienen reacciones
        time.sleep(1)
        dataReactions = h.get_reactions(data[index]['id'], URL_LIKED)
        
        #Almacenamos las reacciones
        for i in range(len(dataReactions)):
            #por el momento no es necesario almacenar el total
            if dataReactions[i]['type'] == 'TOTAL':
                i = i + 1
            else:
                for j in range(len(dataReactions[i]['reactions'])):
                    if res == -1:
                        break
                    res = php.insert('insertReaction.php', dataReactions[i]['reactions'][j])
        
                    
    if res == 0:
        print("EXITO")
    else:
        print("ERROR AL EJECUTAR EL PROGRAMA")
        
