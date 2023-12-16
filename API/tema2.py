from PIL import Image
import requests
robot_name = "superbot"
params = {
"set" : "set3",
"bgset": "bg1",
"size": "256х256"
}

res = requests.get(
    f'https://robohash.org/{robot_name}',
    stream=True,
    params=params

)
image = Image.open(res.raw)
image.show()