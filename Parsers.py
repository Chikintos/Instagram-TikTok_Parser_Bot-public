import datetime
import requests
import json
import instaloader

import calendar
import time
from datetime import datetime
import os
from PIL import Image
import json
from bs4 import BeautifulSoup
import requests
import urllib.request


#  scraper initialization



# TikTok post pasrsr
class TTParse:
    def DownloadfrTikTok(video_url:str):
        base_url="https://proxitok.pabloferreiro.es/@placeholder/video/"
        if video_url.count("vm.tiktok.com")!=0:
            video_id=video_url.split("/")[-2]
        else:
            video_id=video_url.split("/")[-1]
            try:
                video_id=video_id[0:video_id.index("?")]
            except:
                video_id=video_id
        print(video_id)
        req=requests.get(base_url+video_id)
        soup=BeautifulSoup(req.text)
        url=soup.find("video").find("source").get("src")

        urllib.request.urlretrieve(url, f"{video_id}.mp4")
        with open(f"{video_id}.mp4","rb")as file:
            video=file.read()
        os.remove(f"{video_id}.mp4")
        return video

        
        




# Instagram Posts parser
class InstaParse:
    def Reconect(login,password):
        loader.login(login,password)
        loader.save_session_to_file()
    def DownloadfrInstagram(message):
        try:
            message=json.loads(str(message))
            post_url=message["text"]
            message_id=message["message_id"]
            extent_list=['jpg']
            id=post_url.split("/")[-2]


            post = instaloader.Post.from_shortcode(loader.context, id)
            loader.download_post(post,f"{message_id}")

            post_list=[]
            file_list=os.listdir(f"{message_id}")
            for file in file_list:
                if file.split(".")[-1] in extent_list:
                    file_name=file.split(".")[0]
                    if file_list.count(file_name+".mp4"):
                        post_list.append({"url":f"{message_id}/{file_name}.mp4","isPhoto":"False"})
                    else :
                        post_list.append({"url":f"{message_id}/{file}","isPhoto":"True"})        
            return post_list
        except Exception:
            InstaParse.Reconect(login["login"],login["password"])
            print(Exception)

# Delete tresh after download
    
    def CoverTracks(id): 
        for file in os.listdir(id):
            os.remove(id+"/"+file)
        os.rmdir(id)
        return True





login={"login": "Your_log","password":"Your_pass"}
loader = instaloader.Instaloader()
try:
    loader.load_session_from_file(login["login"])
    loader.login(login["login"],login["password"])
    print("Test login",loader.test_login())
except:
    InstaParse.Reconect(login["login"],login["password"])
if loader.test_login()==None:
    loader.login(login["login"],login["password"])
    loader.save_session_to_file()
    print("Test login",loader.test_login())


if __name__=="__main__":
    url="https://www.instagram.com/p/CokssjmjBfC/?utm_source=ig_web_copy_link"
    tt_url="https://vm.tiktok.com/ZMYrNDNuA/" #Краб
    TTParse.DownloadfrTikTok("https://www.tiktok.com/@rusalochka.xl/video/7197134273843973382?is_from_webapp=1&sender_device=pc")
    TTParse.DownloadfrTikTok("https://vm.tiktok.com/ZMYrNDNuA/")
    TTParse.DownloadfrTikTok("https://www.tiktok.com/@_liolik_fan_9/video/7179958866447256838")
# https://www.tiktok.com/@rusalochka.xl/video/7197134273843973382?is_from_webapp=1&sender_device=pc
# https://vm.tiktok.com/ZMYrNDNuA/
# https://www.tiktok.com/@_liolik_fan_9/video/7179958866447256838
