import os


POSITIONS = {
    "right": "east",
    "left": "west",
    "up": "north",
    "down": "south",
    "center": "center"
}


image_name = input("image name: ")
size = input("image size (widthxheight): ")

thumb_position = ""
while thumb_position not in ["right", "left", "up", "down", "center"]:
    thumb_position = input("thumbnail position (right, left, up, down, center): ")
    if thumb_position not in ["right", "left", "up", "down", "center"]:
        print("Invalid option")

thumb_text = input("Thumbnail text: ")


os.system(
    "convert -size " + size +
    " -gravity " + POSITIONS[thumb_position] +
    " -background transparent " +
    " -fill white " +
    " -kerning -1 " +
    " caption:" + "'" + thumb_text + "'"  +
    " sentence.png"
)

os.system(
    "composite -gravity " + POSITIONS[thumb_position] + " sentence.png " +
    image_name + " converted.png"
)
