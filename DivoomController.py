import requests
import json

class CDivoomController:
    def __init__(self, ip):
        self.ip = ip

    def SendPost(self, data):
        endpoint = f"http://{self.ip}:80/post"
        header = {"Content-Type": "application/json"}
        return requests.post(endpoint,headers=header, data=json.dumps(data))
    
    def ResetPicID(self):
        send_data = {
            "Command": "Draw/ResetHttpGifId"
        }

        return self.SendPost(send_data)
    
    def send_image(self,encoded_img, pic_num=1, width=64, offset=0, id=0, speed=100):
        self.ResetPicID()
        send_data={
            "Command": "Draw/SendHttpGif",
            "PicNum": pic_num,
            "PicWidth": width,
            "PicOffset": offset,
            "PicID": id,
            "PicSpeed": speed,
            "PicData": encoded_img.decode('utf-8')
        }

        return self.SendPost(send_data)
    
    def send_text(self, text, x, y, width, color, dir=0, font=0, speed=100, align=1):
        send_data={
            "Command": "Draw/SendHttpText",
            "TextId": 0,
            "x": x,
            "y": y,
            "dir": dir,
            "font": font,
            "TextWidth": width,
            "TextString":text,
            "speed": speed,
            "color": color,
            "align": align
        }

        return self.SendPost(send_data)
    
    def send_text_list(self, text_list):
        send_data = {
            "Command": "Draw/SendHttpItemList",
            "ItemList": text_list
        }

        return self.SendPost(send_data)