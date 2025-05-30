from PIL import Image, ImageDraw, ImageFont
import base64

class CImageDrawer:
    def __init__(self, width, height):
        self.width = width
        self.height= height
        self.make_image()

    def make_image(self):
        self.img = Image.new('RGB', (self.width, self.height), (0,0,0))
        self.draw = ImageDraw.Draw(self.img)

    def GetFont(self, font_name, size):
        return ImageFont.truetype(font_name, size)

    def DrawText(self, x, y, text, color, font, font_size):
        font = self.GetFont(font, font_size)
        self.draw.text((x,y), text, color, font=font)

    def encode_base64(self):
        convert_img = self.img.resize((self.width,self.height)).convert('RGB')

        encode_arr = []
        for y in range(self.height):
            for x in range(self.width):
                r, g, b = convert_img.getpixel((x, y))
                encode_arr.append(r)
                encode_arr.append(g)
                encode_arr.append(b)
        
        encode=base64.b64encode(bytes(encode_arr))
        return encode
