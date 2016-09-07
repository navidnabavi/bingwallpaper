from requests import get
import os
import getpass

api_url = 'http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'
image_path = '/home/{}/wallpaper.jpg'.format(getpass.getuser())
image_url = 'http://www.bing.com/{}_1920x1080.jpg'
image_request = get(api_url).json()

image = get(image_url.format(image_request['images'][0]['urlbase'])).content

file = open(image_path, 'w')
file.write(image)
file.close()

command = "gsettings set org.mate.background picture-filename '{}'".format(image_path)

os.system(command)
