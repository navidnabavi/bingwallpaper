import os
import requests

image_url = os.getenv("IMAGE_URL")
image_request = requests.get(os.getenv("API_URL")).json()

image = requests.get(image_url.format(image_request["images"][0]["urlbase"])).content

with open(os.getenv("IMAGE_PATH"), "wb") as f:
    f.write(image)

command = "gsettings set org.mate.background picture-filename '{}'".format(
    os.getenv("IMAGE_PATH")
)

os.system(command)
