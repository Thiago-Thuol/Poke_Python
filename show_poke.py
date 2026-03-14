from PIL import Image
import race as rc

def show_sprite_enemy(path, width=35,info:list=["oi","tchau"],xp:int=0,name_len:int=0):

    img = Image.open(path).convert("RGBA")

    w, h = img.size
    new_h = int((h / w) * width)

    img = img.resize((width, new_h), Image.NEAREST)

    pixels = img.load()

    for i, y in enumerate(range(0, new_h - 1, 2)):

        line = ""

        for x in range(width):
            r1,g1,b1,a1 = pixels[x,y]
            r2,g2,b2,a2 = pixels[x,y+1]

            line += (
                f"\033[38;2;{r1};{g1};{b1}m"
                f"\033[48;2;{r2};{g2};{b2}m"
                "▀"
            )

        line += "\033[0m"

        text = info[i] if i < len(info) else ""
        tamanho = len(text)
        if i == 1:
            tamanho =   39 -tamanho
        elif i == 2:
            tamanho = 48 - tamanho
        elif i == 4:
            tamanho = 39 -tamanho
        else:
            tamanho = 30 - tamanho
        print(" "*40+text + tamanho*" "+line)


def show_sprite_you(path, width=35,info:list=["oi","tchau"]):

    img = Image.open(path).convert("RGBA")

    w, h = img.size
    new_h = int((h / w) * width)

    img = img.resize((width, new_h), Image.NEAREST)

    pixels = img.load()

    for i, y in enumerate(range(0, new_h - 1, 2)):

        line = ""

        for x in range(width):
            r1,g1,b1,a1 = pixels[x,y]
            r2,g2,b2,a2 = pixels[x,y+1]

            line += (
                f"\033[38;2;{r1};{g1};{b1}m"
                f"\033[48;2;{r2};{g2};{b2}m"
                "▀"
            )

        line += "\033[0m"

        text = info[i] if i < len(info) else ""
        print(line + 10*" " + text)
 

def draw_poke_enemy(name,text,xp_np,name_len):
     show_sprite_enemy(path=f"newPoke/{rc.races_id[name]}.png",info=text,xp=len(xp_np),name_len=name_len)

def draw_poke_you(name,text):
     show_sprite_you(path=f"sprites_back_draw/{rc.races_id[name]}.png",info=text)
