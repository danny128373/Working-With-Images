from PIL import Image

# opens image and assigns to mac
mac = Image.open('images/example.jpg')
# prints mac size as tuple (width, height)
print(mac.size)
# crops image mac, argument is a tuple (starting position x, starting position y, width, height)
cropped_mac = mac.crop((0, 0, 100, 100))
# prints cropped_mac size as tuple (width, height)
print(cropped_mac.size)
# opens image and assigns to pencils
pencils = Image.open('images/pencils.jpg')
# prints pencils size as tuple (width, height)
print(pencils.size)
x = 0
y = 0
w = 1950 / 3
h = 1300 / 10
# cropping pencils image
cropped_pencils = pencils.crop((x, y, w, h))
# prints cropped_pencils size as tuple (width, height)
print(cropped_pencils.size)

bottom_cropped_pencils = pencils.crop((0, 1100, w, 1300))
print(bottom_cropped_pencils.size)

computer = mac.crop((800, 800, 1200, 1257))
mac.paste(im=computer, box=(0, 0))

blue = Image.open("images/blue_color.png").convert("RGBA")
red = Image.open("images/red_color.jpg").convert("RGBA")
# to change opacity rbga a=alpha
blue.putalpha(128)
red.putalpha(128)

# pasting red on top of blue
blue.paste(im=red, box=(0, 0), mask=red)
blue.save("images/purple.png")
