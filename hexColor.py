HEX_COLOURS = {"aliceblue": "#f0f8ff", "antiquewhite": "	#faebd7", "azure1": "#f0ffff", "beige": "#f5f5dc",
               "bisque1": "#ffe4c4", "black": "#000000", "blanchedalmond": "#ffebcd"}


colour = input("Enter Colour name: ")
while colour != "":
    colour = colour.lower()
    if colour in HEX_COLOURS:
        print(colour, "is", HEX_COLOURS[colour])
    else:
        print("Invalid Colour")
    colour = input("Enter Colour name: ")
