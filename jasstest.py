from PIL import Image, ImageDraw
def visualize_map(datafile, outimg):
    clrs = {
        'S': (25, 25, 25),  
        'R': (128, 200, 200),  
        'C': (255, 0, 0),      
        'G': (0, 255, 0),      
        'B': (0, 0, 255),      
        'P': (255, 255, 0),    
        'T': (255, 165, 0)    
    }
    with open(datafile, 'r') as file:
        lines = file.readlines()
    wdh = len(lines[0].strip())
    hgt = len(lines)
    img = Image.new('RGB', (wdh * 30, hgt * 30), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    for y, line in enumerate(lines):
        for x, symbol in enumerate(line.strip()):
            color = clrs.get(symbol, (0, 0, 0))
            draw.rectangle([x * 30, y * 30, (x + 1) * 30, (y + 1) * 30], fill=color)
    img.save(outimg)
    print(f"saved!! {outimg}")
datafile = 'data.txt'
outimg = 'map.png'
visualize_map(datafile, outimg)