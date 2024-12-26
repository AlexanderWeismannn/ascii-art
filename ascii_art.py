#installs
import sys
import math
from PIL import Image


#main
def main():
    
    #get image height & width
    try:
        img = Image.open("ascii-pineapple.jpg")
        print("Succesfully Loaded Image!")
        print(img.size)
    except:
        print("[ERROR]: No Image Found")
        sys.exit()

    #Convert img to 2d array of RGB pixel values
    img = img.convert("L")
    w,h = img.size

    aspect_ratio = h/w
    new_width = 300
    new_height = int(new_width * aspect_ratio * 0.90)
    img = img.resize((new_width,new_height))

    pixel_values = list(img.getdata())
    pixel_map = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

    ascii_art = [pixel_map[(brightness * len(pixel_map)) // 256] for brightness in pixel_values]
    ascii_rows = ["".join(ascii_art[i:i+new_width]) for i in range(0,len(ascii_art),new_width)]

    ascii_string = "\n".join(ascii_rows)
    print(ascii_string)



        
    
    
    
        

if __name__ == "__main__":
    main()