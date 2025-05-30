from ImageDrawer import CImageDrawer
from DivoomController import CDivoomController

class CMyClock:
    def __init__(self, divoom_ip):
        self.drawer = CImageDrawer(64,64)
        self.divoom = CDivoomController(divoom_ip)

    def GetTime(self, text_id):
        return {
            "TextId": text_id,
            "type": 5,
            "x": 0,
            "y": 11,
            "dir": 0,
            "font": 232,
            "TextWidth": 64,
            "Textheight": 20,
            "TextString": "",
            "speed": 100,
            "color": "#FFFFFF",
            "update_time": 1,
            "align": 2
        }
    
    def GetDate(self, text_id):

        font = 410
        month = {
            "TextId": text_id,
            "type": 9,
            "x": 0,
            "y": 1,
            "dir": 0,
            "font": font,
            "TextWidth": 16,
            "Textheight": 12,
            "TextString": "",
            "speed": 100,
            "color": "#FFFFFF",
            "update_time": 1,
            "align": 1
        }

        divide = {
            "TextId": text_id + 1,
            "type": 22,
            "x": 12,
            "y": 1,
            "dir": 0,
            "font": 418,
            "TextWidth": 8,
            "Textheight": 12,
            "TextString": "/",
            "speed": 100,
            "color": "#FFFFFF",
            "update_time": 1,
            "align": 1
        }

        day = {
            "TextId": text_id + 2,
            "type": 8,
            "x": 18,
            "y": 1,
            "dir": 0,
            "font": font,
            "TextWidth": 16,
            "Textheight": 12,
            "TextString": "",
            "speed": 100,
            "color": "#FFFFFF",
            "update_time": 1,
            "align": 1
        }

        return [month, divide, day]
    
    def GetTeperature(self, text_id):
        font = 410

        return {
            "TextId": text_id,
            "type": 17,
            "x": 40,
            "y": 1,
            "dir": 0,
            "font": font,
            "TextWidth": 22,
            "Textheight": 12,
            "TextString": "",
            "speed": 100,
            "color": "#FFFFFF",
            "update_time": 1,
            "align": 3
        }

    def DrawBackGround(self):
        self.drawer.draw.rectangle([0, 0, 64, 64], fill=(0,0,0), outline=(0,0,0), width=0)
        self.drawer.draw.line([0, 32, 64, 32], fill=(255,255,255), width=1)
        self.drawer.DrawText(0, 33, "今日のニュース", "#FF0000", "SourceHanSansHW-Regular.otf", 9)

        encode = self.drawer.encode_base64()
        self.divoom.send_image(encode, id=1)

    def DrawTime(self):
        dates = self.GetDate(2)

        text_list = [
            self.GetTime(1),
            dates[0],
            dates[1],
            dates[2],
            self.GetTeperature(5)
        ]

        self.divoom.send_text_list(text_list)
    
    def DrawText(self, text):
        self.divoom.send_text(text, 0, 47, 64, "#FFFFFF", font=7, speed=25)

    def GetText(self, filename, encoding = "UTF-8"):
        text = ""
        with open(filename, 'r', encoding=encoding) as f:
            text = f.readline()
        return text


    def Draw(self, filename):
        self.DrawBackGround()
        self.DrawTime()
        self.DrawText(self.GetText(filename))

if __name__ == "__main__":
    PIXOO_IP = "192.168.10.244"
    clock = CMyClock(PIXOO_IP)
    clock.Draw('message.txt')