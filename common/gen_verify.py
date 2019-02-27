# -*-coding:utf-8-*-
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random, string, os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PyWebRedis.settings")
from django.conf import settings

# 字体保存位置
FONT_PATH = os.path.join(settings.STATICFILES_DIRS[0], 'common', 'fonts', 'Arial.ttf')

# 生成验证码图片的宽度和高度
IMG_SIZE = (128, 44)
# 像素类型
IMG_MODE = 'RGBA'
# 背景颜色，默认为白色
# BG_COLOR = (255, 255, 255)
BG_COLOR = '#FFFAFA'

# 生成验证码个数, 默认4个字符
NUMBER = 4
# 字体大小，默认25像素
FONT_SIZE = 25
# 字体颜色，默认为蓝色
FONT_COLOR = (0, 0, 255)
# 是否加入噪点
ADD_POINT = True
# 是否要加入干扰线
ADD_LINE = True
# 干扰线颜色。默认为红色
LINE_COLOR = (255, 0, 0)
# 加入干扰线条数的上下限
LINE_RANGE = (2, 7)

# 验证码排除的字符
STR_FLITERS = ('0', 'O', 'o', '1', 'l', 'I')
# 验证码字符范围
STR_RANGE = set(string.ascii_letters + string.digits).difference(STR_FLITERS)

# 默认保存路径
DEFAULT_SAVE_PATH = os.path.join(settings.MEDIA_ROOT, 'WebRedis/verify')

# 默认名称
DEFAULT_FILENAME = 'verify.png'


def random_chr():
    return ''.join(random.sample(STR_RANGE, NUMBER))


def draw_text(brush, xy, text, fill, font):
    return brush.text(xy, text, fill, font)


def draw_line(brush, x, y, fill):
    pointX = (random.randint(0, x), random.randint(0, y))
    pointY = (random.randint(0, x), random.randint(0, y))
    return brush.line((pointX, pointY), fill, 1)


def draw_point(brush, canvasW, canvasH):
    for i in range(0, 100):
        # 噪点绘制的范围
        xy = (random.randrange(0, canvasW), random.randrange(0, canvasH))
        # 噪点的随机颜色
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        # 绘制出噪点
        brush.point(xy, fill)


def draw_img(dirpath=DEFAULT_SAVE_PATH, filename=DEFAULT_FILENAME):
    # 创建画布
    canvas = Image.new(mode=IMG_MODE, size=IMG_SIZE, color=BG_COLOR)
    # 创建画笔
    brush = ImageDraw.Draw(canvas)
    # 设置字体样式和大小
    word = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    # 获取字符串
    verify = random_chr()
    # 获取字符串宽高
    chrW, chrH = word.getsize(verify)
    # 画布宽高
    canvasW, canvasH = IMG_SIZE
    # 字符串位置
    xy = ((canvasW - chrW) / 2, (canvasH - chrH) / NUMBER)
    # 字符绘制
    draw_text(brush=brush, xy=xy, text=verify, fill=FONT_COLOR, font=word)
    if ADD_POINT:
        draw_point(brush, canvasW, canvasH)

    if ADD_LINE:
        upline, downline = LINE_RANGE
        limite = random.randint(upline, downline)
        while limite:
            draw_line(brush, canvasW, canvasH, LINE_COLOR)
            limite -= 1
    # 删除画笔
    del brush
    # 创建扭曲
    canvas.transform(size=(canvasW + 20, canvasH + 20), method=Image.AFFINE, data=(1, 2, 10, 2, 5, 1),
                     fill=Image.BILINEAR)
    # 边界加强
    canvas.filter(ImageFilter.EDGE_ENHANCE_MORE)
    # 图片保存
    canvas.save(os.path.join(dirpath, filename))
    # 返回验证码
    return verify


if __name__ == '__main__':
    draw_img(DEFAULT_SAVE_PATH, DEFAULT_FILENAME)
