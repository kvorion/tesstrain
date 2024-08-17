from PIL import Image, ImageDraw, ImageFont

rupee_prefix = "₹"
amounts = [123.44, 665.45, 555.5, 123.55, 100.20, 333.45, 5.5,
           23.2, 24.56, 99.9, 99.88, 3.33, 5.7]
width = 200 
height = 50
counter = 1
for font_size in range(14, 20):
    for amount in amounts:
        font = ImageFont.truetype("data/fonts/font.ttf", size=font_size)
        img = Image.new('RGB', (width, height), color='white')
        imgDraw = ImageDraw.Draw(img)
        message = rupee_prefix + str(amount)
        textWidth = imgDraw.textlength(message, font=font)
        xText = textWidth 
        yText = font_size 

        imgDraw.text((xText, yText), message, font=font, fill="#000000")

        img.save(f'data/invoices-ground-truth/{counter}.png')
        with open(f'data/invoices-ground-truth/{counter}.gt.txt', "w+") as gt:
            print(message, file=gt)

        counter += 1