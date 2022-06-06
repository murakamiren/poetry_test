from statistics import quantiles
from PIL import Image

img_path = "./poetry_test/E7AB8BE88AB1E99FBF.jpg"

print("hello world")

def math(x):
    doubleX = x * 2
    print(doubleX)

math(3)

img = Image.open(img_path)

img_w = img.width
img_h = img.height

res_w = 340

res_raito = 340 / img_w

res_size = (res_w, round(img_h * res_raito))

print(res_size)

res_img = img.resize(res_size)
res_img.save("dist/output.jpg", quantiles=90)
