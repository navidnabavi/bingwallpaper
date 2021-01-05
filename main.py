from requests import get
import os
import constants

image_url = "http://www.bing.com/{}_1920x1080.jpg"
image_request = get(constants.API_URL).json()

image = get(image_url.format(image_request["images"][0]["urlbase"])).content

with open(constants.IMAGE_PATH, "wb") as f:
    f.write(image)

command = "gsettings set org.mate.background picture-filename '{}'".format(
    constants.IMAGE_PATH
)

os.system(command)
