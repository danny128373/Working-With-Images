from PIL import Image


mac = Image.open('images/example.jpg')
print(mac.size)
cropped_mac = mac.crop((0, 0, 100, 100))
print(cropped_mac.size)

pencils = Image.open('images/pencils.jpg')
print(pencils.size)
x = 0
y = 0
w = 1950 / 3
h = 1300 / 10
cropped_pencils = pencils.crop((x, y, w, h))
print(cropped_pencils.size)
