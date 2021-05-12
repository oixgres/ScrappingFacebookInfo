from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dato import *
import time
import json
import re
from Facebook_Scraper_POST import Facebook_Scraper_POST
from managerFile import readJson,writeJson
import csv
import pymysql

if __name__ == "__main__":
    
    PATH = "chromedriver.exe"
    h = Facebook_Scraper_POST(PATH)
    h.loginSession(URL=URL_LOGIN,user=user[0],password=password[0])
    
    data=h.collectionPOST(URL_GROUP,3)
    
    #Conexion SQL
    connection = pymysql.connect(host = "174.136.52.201", user="conisoft_fb", password = "Fengoigres1094346", database = "conisoft_facebook_scraper")
    cursor = connection.cursor()
    
    #Creamos CSV
    with open('post.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONE, escapechar=";")
        
        for index in range(len(data)):
            writer.writerow(data[index])
            print(data[index][2])
            query = "INSERT INTO POST(post_id, poster_name, post_text, link) VALUES(%s, %s, %s, %s);"
            cursor.execute(query, data[index]);
    
    
    connection.close()

      
    
    '''
    PATH = "chromedriver.exe"
    h = Facebook_Scraper_POST(PATH)
    h.loginSession(URL=URL_LOGIN,user=user[2],password=password[2])
    
    data=h.collectionPOST(URL_GROUP,3)
    
    
    
    
    with open('post.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONE, escapechar=";")
        
        for index in range(len(data)):
            writer.writerow(data[index])
    
    '''
    #Obtener enlaces de los posts
    #json_post=h.collectionPOST(URL_GROUP,20)
    #writeJson(json_post,'post.json')
    
    
    '''
    json_post=readJson('post.json')
    
    dataComment=h.getComments(json_post[12]['link'])
    writeJson(dataComment,'comment.json')
    
    reactions = h.get_reactions(json_post[9]['post_id'], URL_LIKED)
    writeJson(reactions,'reactions.json')
    '''
    
    
    #PATH ="C:/Users/fhaos/Documents/FCQI/8mo/ayundantia/chromedriver.exe"
    
    #h.test_comment_POST(URL='https://m.facebook.com/groups/413938496303058/permalink/469954730701434/')
    # dataComment=h.getComments(url='https://m.facebook.com/story.php?story_fbid=2768196876764948&id=1629107234007257&anchor_composer=false')
    # writeJson(dataComment,'comment.json')

    #data=h.get_reactions(POST_ID=2789506314634004,URL_type= "https://m.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier=")
    #writeJson(data,'reactions.json')

    # datat=readJson('comment.json')
    #obtener el contenido de los post 
    #json_post=h.collectionPOST(URL_GROUP,10)
    #writeJson(json_post,'post.json')
    #json_post=readJson('post.json')
    
    
    # obtener las persona compartidas
    # list_shared_people=[]
    # for num_post in range(len(json_post)):
    #     post_shared_name=h.test_User_names(json_post[num_post]['post_id'],URL_SHARED,"shared_names")
    #     list_shared_people.append(post_shared_name)
    # writeJson(list_shared_people,'people_shared.json')

    # # # obtener las personas que dieron like
    # list_liked_people=[]
    # for num_post in range(len(json_post)):
    #     post_liked_name=h.test_User_names(json_post[num_post]['post_id'],URL_LIKED,"liked_names")
    #     list_liked_people.append(post_liked_name)
    # writeJson(list_liked_people,'people_liked.json')

    # # obtener las personas son visitados
    
    '''
    list_visited_people=[]
    for num_post in range(len(json_post)):
        post_visited_name=h.test_User_names(json_post[num_post]['post_id'],URL_VISITED,"visited_names")
        list_visited_people.append(post_visited_name)
    writeJson(list_visited_people,'people_visited.json')

    # # obtener comentarios
    list_comments_post=[]
    for num_post in range(len(json_post)):
        comment_post = h.test_comment_POST(json_post[num_post]['post_id'])
        list_comments_post.append(comment_post)
    writeJson(list_comments_post,'post_comments.json')

    
    list_likes_people=[]
    for num_post in range(len(json_post)):
        post_likes_people = h.test_User_names(json_post[num_post]['post_id'], URL_LIKED, "liked_names")
        list_likes_people.append(post_likes_people)
    writeJson(list_likes_people, 'people_likes.json')
    '''
    
    # h.get(URL_GROUP)
    # h.collectionPOST_URL_and_POST_ID(URL_GROUP,10)
    # h.Collection_Text_POST(10)
    # h.generateJson('post.json')
    
    # with open('post.json',encoding='utf-8') as f:
    #     data_json = json.loads(f.read())
    # print(str(data_json[0]['post_ID']))
    
    # print('\n *** visitas *** \n')
    # h.test_User_names(data_json[0]['post_ID'],URL_VISITED,"people_visited.json","visited_names")

    # h.test_User_names(data_json[0]['post_ID'],URL_LIKED,"people_liked.json","liked_names")
    # h.test_User_names(data_json[0]['post_ID'],URL_SHARED,"people_shared.json","shared_names")
    # print('\n *** likes *** \n')
    # h.test_User_liked(data_json[0]['post_ID'])
    # print('\n *** compartidas *** \n')
    # h.test_User_shared(data_json[0]['post_ID'])



    
    
    