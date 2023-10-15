# Dictionary of color names:
COLORS = {
    "amber": "#ffbf00",
    "aqua": "#00ffff",
    "beaver": "#9f8170",
    "denim": "#1560bd",
    "crimson": "#dc143c",
    "chocolate": "#d2691e",
    "carmine": "#960018",
    "buff": "##f0dc82",
    "black": "#000000",
    "bole": "#79443b"
}


def lookup_color_code(color_name):
    return COLORS.get(color_name.lower(), "not found")


while True:
    color_name = input("Enter a color name (or blank to exit): ").strip().lower()

    if not color_name:
        break

    color_code = lookup_color_code(color_name)
    print(f"The hexadecimal code for {color_name} is {color_code}")
