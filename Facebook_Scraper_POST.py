
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from element_html import *
from dato import *
import time
import re
import json
class Facebook_Scraper_POST:





    def __init__(self,path):
        self.driver = webdriver.Chrome(path)

    def get(self,URL):
        self.driver.get(URL)


    
    def loginSession(self,URL,user ,password):  
        self.driver.get(URL)                                                        # acceder page-login
        self.driver.find_element_by_id(LOGIN_EMAIL_ID).send_keys(user)             # introduce usuario
        self.driver.find_element_by_name(PASSWORD_NAME).send_keys(password)                # introduce password
        self.driver.find_element_by_name(PASSWORD_NAME).send_keys(Keys.RETURN)             # enter
        time.sleep(3)
        iniciar_seccion_no_toque = self.driver.find_element_by_xpath(INPUT_NO_TOUCH_XPATH)
        iniciar_seccion_no_toque.click()


    def collectionPOST(self,URL,number_POST):

        POST_URL =[]
        POST_ID =[]
        POSTER_NAME =[]
        POSTER_TEXT=[]

        index=0
        self.driver.get(URL)                                                 # acceder la pagina del grupo
        self.scroll_max()                                                    # mostrar todas las publicaciones
        
        links = self.driver.find_elements_by_xpath(ARTICLE_LINK_XPATH)    # Encontrar todos elementos article(enlace de la publicacion)
       
        if number_POST>len(links):   
            number_POST=len(links)                                      # Obtener los post basando en el number_POST
        for link in range(number_POST):
            js_script="return document.getElementsByTagName('article')["+str(index)+"].dataset.store"
            POST_URL.append(str(links[link].get_attribute('href').split('?')[0]))
            data_post = self.driver.execute_script(js_script)
            POST_ID.append(re.findall(r"top_level_post_id.(.+?):",str(data_post))[0])

            print(POST_ID[index])

            index+=1
        for index in range(number_POST):
            self.driver.get(POST_URL[index])
            try:
                poster_text=self.driver.find_element_by_xpath(POST_TEXT_XPATH)
                POSTER_TEXT.append(poster_text.text)
            except NoSuchElementException:
                POSTER_TEXT.append("No hay texto")
            poster_name=self.driver.find_element_by_xpath(POSTER_NAME_XPATH)
            POSTER_NAME.append(poster_name.text)
            

        
        data=[]
        for index in range(len(POST_URL)):
            element={}
            element["link"]=POST_URL[index]
            element["poster_name"]=POSTER_NAME[index]
            element["post_id"]=POST_ID[index]
            element["post_text"]=POSTER_TEXT[index]
            data.append(element)
                  
        return data
                
        
                

        



    def generateJson (self,file):
        file = open(file,'w+',encoding="utf-8")
        data=[]
        

        for index in range(len(self.POST_URL)):
            element={}
            element["link"]=self.POST_URL[index]
            element["poster_name"]=self.POSTER_NAME[index]
            element["post_id"]=self.POST_ID[index]
            element["post_text"]=self.POSTER_TEXT[index]
            data.append(element)
                  
        json.dump(data,file,indent=4, ensure_ascii=False)
        file.close()
        
    #https://m.facebook.com/ufi/group/seenby/profile/browser/?id=433655667664674
    #Obtener usuarios que visitaron el post

    # @parameter POST_ID int
    # @parameter file string
    # @parameter type_user string visited_name shared_name liked_name

    def test_User_names(self,POST_ID,URL_type,type_names):
        url=URL_type+str(POST_ID)
        self.driver.get(url)
        
        t=True
        json_data={} 
        json_data["link_ID"]=POST_ID
        while t:
            try:
                self.driver.find_element_by_xpath(BOTTOM_SEE_MORE_XPATH).click()   # clic al elemento ver mas
                time.sleep(1)
            except NoSuchElementException:  
                t=False
                pass
        list_name = self.driver.find_elements_by_xpath(LIST_NAME_XPATH)
        visited_names=[]
        
        index = 1
        for name in list_name:
            if len(name.text)>0:
                visited_name={}
                key='name'+str(index)
                visited_name[key]=name.text
                visited_names.append(visited_name)
                index+=1
                print(name.text)
        json_data["number"]=len(visited_names)
        json_data[type_names]=visited_names
        return json_data
        
    
    
    def scroll_max(self):
        t = True
        while t:
            scrollHeight_now = self.driver.execute_script("return document.body.scrollHeight;")

            for r in range(10):
                self.driver.execute_script("window.scrollBy(0,1500)")
            time.sleep(2)
            scrollHeight_scrolled=self.driver.execute_script("return document.body.scrollHeight;")
            if scrollHeight_scrolled==scrollHeight_now:
                t=False



    # https://m.facebook.com/story.php?story_fbid=2765539700363999&id=1629107234007257&anchor_composer=false
    def test_comment_POST(self,post_id):
        url=URL_POST_LINK+str(post_id)
        self.driver.get(url)
        self.scroll_to_max_height_comment()
        self.see_comments_secondary(SEE_COMMENTS_SECONDARY_CLASS_NAME)
        boxs = self.driver.find_elements_by_xpath("//div[@class='_2b04']") 
        json_post_comments={}
        comments =[]
        num_comment = 0
        for box in boxs:
            try:
                name = box.find_element_by_css_selector(" div._2b06 > div._2b05")
                comment_Text = box.find_element_by_css_selector(" div._2b06 > div:nth-child(2)")
                comment={}
                num_comment+=1
                comment['number_comment']=num_comment
                comment['name']=name.text
                comment['comment_text']=comment_Text.text
                comments.append(comment)
            except NoSuchElementException:
                print("usuario no capturado por uso de gif")
                pass
        #json_post_comment['post_id']=post_id
        json_post_comments['post_Id']=post_id
        json_post_comments['total_comments']=num_comment
        json_post_comments['comments']=comments
        return json_post_comments

    
    def see_comments_secondary(self,class_name):
        for bton in self.driver.find_elements_by_class_name(class_name):
                    bton.click()
                    time.sleep(0.5)


    def see_past_comment(self,web_elements):
        for web_element in web_elements:
            t=True
            while t:
                try:
                    web_element.find_element_by_xpath('//a[@class="async_elem"]').click()   # clic al elemento ver mas
                    time.sleep(1)
                except NoSuchElementException:  
                    t=False
                    pass


    def scroll_to_max_height_comment(self):

        t=True
        while t:
            try:
                self.driver.find_element_by_xpath('//div[@class="async_elem"]').click()   # clic al elemento ver mas
                time.sleep(2)
            except NoSuchElementException:  
                t=False
                pass
        



    