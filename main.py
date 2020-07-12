import os


size = input("image size (widthxheight): ")
thumb_text = input("Thumb text: ")


os.system(
    "convert -size " + size +
    " -gravity center" +
    " -background transparent " +
    " -fill white " +
    " -kerning -1 " +
    " caption:" + "'" + thumb_text + "'"  +
    " sentence.png"
)

os.system(
    "composite  -gravity south sentence.png "+
    "original.png converted.png"
)
