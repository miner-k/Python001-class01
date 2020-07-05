

from PIL import Image
import pytesseract

# 打开文件并显示文件
im = Image.open('timg.jpg')
# im.show()


# 灰度图片
gray = im.convert('L')
gray.save('c.gray2.jpg')
im.close()

# 二值化,颜色深的更深，颜色浅的更浅
threshold =200
table = []

for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

out = gray.point(table,'1')
out.save('c_th.jpg')

th = Image.open('c_th.jpg')
# print(pytesseract.image_to_string(th,lang='chi_sim+eng',))
print(pytesseract.image_to_string(th,lang='eng',))

