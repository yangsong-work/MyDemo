

import numpy as np
from PIL import Image

#以下的脚本被import时不执行
if __name__ == '__main__':
    #获取文件
    image_file = '../lz.jpg'
    #定义输出文本char高度
    height = 100
    #打开图片
    img = Image.open(image_file)
    #获取图片的宽和高
    image_width, image_height = img.size
    #算出要生成图片的宽度
    width =int (2 * height * image_width // image_height)

    #设置要生成图片的宽和高
    img = img.resize((width,height),Image.ANTIALIAS)

    #L为转成灰度图像
    pixels = np.array(img.convert("L"))

    #定义替换字母
    chars = "MNHQ$OC?7>!:-;. "
    #均分灰度阶级
    N = len(chars)
    step = 256 // N
    #
    result = ''
    for i in range(height):
        for j in range(width):
            #每个数值替换为对应的字母
            result += chars[pixels[i][j] // step]
            #换行
        result += '\n'
    with open('../text.txt', mode ='w') as f:
        f.write(result)

