import os


POSITIONS = {
    "right": "east",
    "left": "west",
    "up": "north",
    "down": "south",
    "center": "center"
}


image_name = input("image name: ")
image_size = input("image size (widthxheight): ")
size = input("text size (widthxheight): ")

thumb_position = ""
while thumb_position not in ["right", "left", "up", "down", "center"]:
    thumb_position = input("thumbnail position (right, left, up, down, center): ")
    if thumb_position not in ["right", "left", "up", "down", "center"]:
        print("Invalid option")

thumb_text = input("Thumbnail text: ")

os.system(
    "convert " + image_name + " -resize " + image_size +
    "^ -gravity north -extent " + image_size + " resized.png"
)

array_size = size.split('x')

os.system(
    "convert transparent-box.png -resize " + array_size[0] + "x" + str(int(array_size[1]) + 20) +
    "\\! transparent-box-0.png"
)

os.system(
    "convert -size " + size +
    " -gravity " + POSITIONS[thumb_position] +
    " -background transparent " +
    " -fill white " +
    " -kerning -1 " +
    " caption:" + "'" + thumb_text + "'"  +
    " sentence-1.png"
)

os.system(
    "composite  -gravity center sentence-1.png "+
    "transparent-box-0.png sentence.png"
)

os.system(
    "composite -gravity " + POSITIONS[thumb_position] + " sentence.png "
    + "resized.png converted.png"
)
