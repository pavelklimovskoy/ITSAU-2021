from PIL import Image

game_map = Image.open('9DrvRU8.jpg')
heat_map = Image.open('Figure_1.png')
heat_map.putalpha(80)

gmap_width, gmap_height = game_map.size
heatm_resized = heat_map.resize((gmap_width, gmap_height), Image.LANCZOS)
game_map.paste(heatm_resized, None, heatm_resized)
game_map.save("map_with_heat.png")
game_map.show()





