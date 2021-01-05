import os

API_URL = os.getenv(
    "API_URL", "http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"
)
IMAGE_PATH = os.getenv("IMAGE_PATH", "/")
IMAGE_URL = os.getenv("IMAGE_URL", None)
