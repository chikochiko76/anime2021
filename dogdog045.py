class AImage(AShape):
    color: any

    def __init__(self, width=100, height=None, cx=None, cy=None, image='pet_darui_dog.png'):
        AShape.__init__(self, width, height, cx, cy)
        if image.startswith('http')
            self.pic = Image.open(io.BytesIO(requests.get(image).content))
        else:
            self.pic = Image.open(image)

    def render(self, canvas: ACanvas, frame: int):
        ox, oy, w, h = self.bounds()
        pic = self.pic.resize((int(w), int(h)))
        canvas.image.paste(pic, (int(ox), int(oy)), pic)
