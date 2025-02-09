import requests
from PIL import Image
from io import BytesIO

# Get url from user
url = input("Please paste an Image URL: ")

def main(url): 
    # gets image, throws error if no image at URL
    response = requests.get(url)
    try: 
        image = Image.open(BytesIO(response.content))
    except FileNotFoundError:
        print("Error: Image not found.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    #resizes image to a width of 128 pixels keeping original aspect ration intact
    width, height = image.size
    new_size = (128, ((height * 128) // width) // 2)

    #convert to grayscalae
    resized_image = image.resize(new_size)
    gray_image = resized_image.convert("L")

    #Calculates brightness for each pixel
    gray_width, gray_height = gray_image.size
    pixels = gray_image.load()

    #Creates grid to print ASCII text on:
    ascii = [' ', '░', '▒', '▓', '█', '▌', '▐', '▀']
    grid = [[" " for _ in range(gray_width)] for _ in range(gray_height)]
    for y in range(gray_height):
        for x in range(gray_width):
            if pixels[x, y] <= 32:
                grid[y][x] = ascii[0]
            elif pixels[x, y] <= 64:
                grid[y][x] = ascii[1]
            elif pixels[x, y] <= 96:
                grid[y][x] = ascii[2]
            elif pixels[x, y] <= 128:
                grid[y][x] = ascii[3]
            elif pixels[x, y] <= 160:
                grid[y][x] = ascii[4]
            elif pixels[x, y] <= 192:
                grid[y][x] = ascii[5]
            elif pixels[x, y] <= 224:
                grid[y][x] = ascii[6]
            elif pixels[x, y] <= 256:
                grid[y][x] = ascii[7]

    

    for row in grid:
        print("".join(row))

main(url)