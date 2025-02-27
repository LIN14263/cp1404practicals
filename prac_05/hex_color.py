HEX_COLORS = {"alice blue": "#f0f8ff", "barn red": "#7c0a02", "blanched almond": "#ffebcd", "blueviolet": "#8a2be2",
              "bright green": "#66ff00", "british racing green": "#004225", "cadmium yellow": "#fff600",
              "canary": "#ffff99", "dark sienna": "#3c1414", "deep peach": "#ffcba4"}
length_of_color = max(len(i) for i in HEX_COLORS)
for code in HEX_COLORS:
    print(f"{code:{length_of_color}} is {HEX_COLORS[code]}")
color = input("Choose a color:").lower()
while color != "":
    try:
        print(HEX_COLORS[color])
    except KeyError:
        print("Invalid input")
    color = input("Choose a color:").lower()
print("Finished")
