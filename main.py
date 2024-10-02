from requests import get
import os
import getpass
import platform
import ctypes

# API URL to get Bing image details
api_url = "http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"
image_url = "http://www.bing.com/{}_1920x1080.jpg"

# Detect the operating system
user = getpass.getuser()
os_type = platform.system()

if os_type == "Linux":
    image_path = "/home/{}/wallpaper.jpg".format(user)
    set_wallpaper_command = "gsettings set org.gnome.desktop.background picture-uri file://{}".format(image_path)
elif os_type == "Darwin":  # macOS
    image_path = "/Users/{}/wallpaper.jpg".format(user)
    set_wallpaper_command = """osascript -e 'tell application "System Events" to set picture of every desktop to ("{}" as POSIX file)'""".format(image_path)
elif os_type == "Windows":
    image_path = os.path.join(os.getenv('USERPROFILE'), 'wallpaper.jpg')
else:
    raise NotImplementedError("Unsupported OS: {}".format(os_type))

# Fetch image details from Bing
image_request = get(api_url).json()

# Download the image
image = get(image_url.format(image_request["images"][0]["urlbase"])).content
with open(image_path, "wb") as file:
    file.write(image)

# Set the wallpaper
if os_type == "Linux" or os_type == "Darwin":
    os.system(set_wallpaper_command)
elif os_type == "Windows":
    # Use ctypes to set the wallpaper in Windows
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
