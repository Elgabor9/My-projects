from PIL import Image
before=Image.open("mindcloud.jpg")
width,height=before.size
pixels=before.load() # saves the pixel values
for x in range(width // 2):
    for y in range(height // 2):
        # Set the color of the current pixel to black (RGB tuple: (0, 0, 0)).
        pixels[x, y] = (0, 0, 0)
after=before
after.save("mindcloud_black_quarter.jpg")
after.show()
