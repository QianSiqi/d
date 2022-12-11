import easygui as e
import os as o
import turtle as t
import pygame as py
import time as tm
import sys as sy
from pgzrun import *
from pgzero import *
from pgzero.builtins import Actor, animate, keyboard
from flask import Flask
from flask import render_template
try:
    f = open('sett.ngm', 'r')
    f.read()
except FileNotFoundError:
    d = input('Linux安装easygui和pygame和pgzero和flask库了吗？[安装了/还没有]')
    if d == '还没有':
        o.system('pip install easygui -i http://pypi.douban.com/simple --trusted-host pypi.douban.com')
        o.system('sudo apt-get install python3-tk')
        o.system('pip install pygame -i http://pypi.douban.com/simple --trusted-host pypi.douban.com')
        o.system('pip install numpy -i http://pypi.douban.com/simple --trusted-host pypi.douban.com')
        o.system('pip install pgzero -i http://pypi.douban.com/simple --trusted-host pypi.douban.com')
        o.system('pip install flask -i http://pypi.douban.com/simple --trusted-host pypi.douban.com')
    if d == '安装了':
        x = open('sett.ngm', 'w')
        x.write(d + '第三方库\n')
    a = input('请输入你的Linux的系统和版本（示例：Ubuntu-22.04）：')
    x.write(a + '\n')
    p = input('请输入python版本（示例：python-3.10.6-64-bit）：')
    x.write(p + '\n')
    m = open('sett.ngm', 'r')
    m.read()


def 一个一个有两个按钮窗口(文字, 标题, 第一个按钮, 第二个按钮):
    e.ccbox(文字, title=标题, choices=(第一个按钮, 第二个按钮))


def 撅(你要撅的东西):
    print(你要撅的东西)


def 一个一个只有一个按钮的窗口(文字, 标题):
    e.msgbox(文字, 标题)


def 命令(命令):
    o.system(命令)


def 下载东西(网址):
    o.system('sudo wget ' + 网址)


def 运行包(deb文件名):
    o.system('sudo dpkg -i ' + deb文件名)


def 下载并运行(包名):
    o.system('sudo apt-get install ' + 包名)


def 还是运行(包名):
    o.system('sudo apt install '+包名)


def 打开文件(文件名):
    o.system('sudo vim '+文件名)


def 把软件扔到垃圾桶里面(软件名):
    o.system('sudo apt-get remove '+软件名)


def 运行exe(exe文件):
    o.system('wine '+exe文件)


def 直走(像素):
    t.forward(像素)


def 左转(角度):
    t.left(角度)


def 右转(角度):
    t.right(角度)


def 退(像素):
    t.backward(像素)


def 你干嘛():
    t.done()


def 去(x, y):
    t.goto(x, y)


def 往上抬():
    t.up()


def 往下抬():
    t.down()


def 清空():
    t.clear()


def 写(文字, 字体, 大小):
    t.write(文字, font=(字体, 大小))


def 把图片画上去(文件名):
    t.Screen().bgpic(文件名)


def 窗口的大小(x, y):
    t.Screen().setup(x, y)


def 初始化():
    py.init()


def 游戏窗口的大小(x, y):
    py.display.set_mode((x, y))


def 游戏标题(标题):
    py.display.set_caption(标题)


def 上传图片(图片名):
    canvas = py.image.load(图片名)


def 显示图片(图片名, x, y):
    global canvas
    canvas.blit(图片名, (x, y))


def 刷新():
    py.display.update()


def 点赞():
    o.system('echo ' + '"' + "            --" + '"')
    o.system('echo ' + '"' + '           | |' + '"')
    o.system('echo ' + '"' + '           | |' + '"')
    o.system('echo ' + '"' + '           | |' + '"')
    o.system('echo ' + '"' + '           | |' + '"')
    o.system('echo ' + '"' + '|----|----|--|-' + '"')
    o.system('echo ' + '"' + '|----|----|--|-' + '"')
    o.system('echo ' + '"' + '|----|----|--|-' + '"')
    o.system('echo ' + '"' + '|----|----|--|-' + '"')
    o.system('echo ' + '"' + '--------------' + '"')
    tm.sleep(0.1)
    o.system('clear')
    o.system('echo ' + '"' + "            --" + '"')
    o.system('echo ' + '"' + '           | |' + '"')
    o.system('echo ' + '"' + '           | |' + '"')
    o.system('echo ' + '"' + '           | |' + '"')
    o.system('echo ' + '"' + '           | |' + '"')
    o.system('echo ' + '"' + '|----|----|--|-' + '"')
    o.system('echo ' + '"' + '|----|----|--|-' + '"')
    o.system('echo ' + '"' + '|----|----|--|-' + '"')
    o.system('echo ' + '"' + '|----|----|--|-' + '"')
    o.system('echo ' + '"' + '--------------' + '"')
    o.system('echo ' + '"' + '--------------' + '"')
    tm.sleep(0.1)
    o.system('clear')
    o.system('echo ' + '"' + "            --" + '"')
    o.system('echo ' + '"' + '           | |' + '"')
    o.system('echo ' + '"' + '           | |' + '"')
    o.system('echo ' + '"' + '           | |' + '"')
    o.system('echo ' + '"' + '           | |' + '"')
    o.system('echo ' + '"' + '|----|----|--|-' + '"')
    o.system('echo ' + '"' + '|----|----|--|-' + '"')
    o.system('echo ' + '"' + '|----|----|--|-' + '"')
    o.system('echo ' + '"' + '|----|----|--|-' + '"')
    o.system('echo ' + '"' + '--------------' + '"')
    o.system('echo ' + '"' + '              ' + '"')
    o.system('echo ' + '"' + '--------------' + '"')
    tm.sleep(0.1)
    o.system('clear')
    o.system('echo ' + '"' + "            --" + '"')
    o.system('echo ' + '"' + '           | |' + '"')
    o.system('echo ' + '"' + '           | |' + '"')
    o.system('echo ' + '"' + '           | |' + '"')
    o.system('echo ' + '"' + '           | |' + '"')
    o.system('echo ' + '"' + '|----|----|--|-' + '"')
    o.system('echo ' + '"' + '|----|----|--|-' + '"')
    o.system('echo ' + '"' + '|----|----|--|-' + '"')
    o.system('echo ' + '"' + '|----|----|--|-' + '"')
    o.system('echo ' + '"' + '--------------' + '"')
    o.system('clear')
    tm.sleep(0.1)
    o.system('echo ' + '"' + "            --" + '"')
    o.system('echo ' + '"' + '           | |' + '"')
    o.system('echo ' + '"' + '           | |' + '"')
    o.system('echo ' + '"' + '           | |' + '"')
    o.system('echo ' + '"' + '           | |' + '"')
    o.system('echo ' + '"' + '|----|----|--|-' + '"')
    o.system('echo ' + '"' + '|----|----|--|-' + '"')
    o.system('echo ' + '"' + '|----|----|--|-' + '"')
    o.system('echo ' + '"' + '|----|----|--|-' + '"')
    o.system('echo ' + '"' + '--------------' + '"')
    o.system('echo ' + '"' + '--------------' + '"')
    tm.sleep(0.1)
    o.system('clear')
    o.system('clear')
    o.system('echo ' + '"' + "            --" + '"')
    o.system('echo ' + '"' + '           | |' + '"')
    o.system('echo ' + '"' + '           | |' + '"')
    o.system('echo ' + '"' + '           | |' + '"')
    o.system('echo ' + '"' + '           | |' + '"')
    o.system('echo ' + '"' + '|----|----|--|-' + '"')
    o.system('echo ' + '"' + '|----|----|--|-' + '"')
    o.system('echo ' + '"' + '|----|----|--|-' + '"')
    o.system('echo ' + '"' + '|----|----|--|-' + '"')
    o.system('echo ' + '"' + '--------------' + '"')
    o.system('echo ' + '"' + '              ' + '"')
    o.system('echo ' + '"' + '--------------' + '"')
    tm.sleep(0.1)
    o.system('clear')
    o.system('echo ' + '"' + "            --" + '"')
    o.system('echo ' + '"' + '           | |' + '"')
    o.system('echo ' + '"' + '           | |' + '"')
    o.system('echo ' + '"' + '           | |' + '"')
    o.system('echo ' + '"' + '           | |' + '"')
    o.system('echo ' + '"' + '|----|----|--|-' + '"')
    o.system('echo ' + '"' + '|----|----|--|-' + '"')
    o.system('echo ' + '"' + '|----|----|--|-' + '"')
    o.system('echo ' + '"' + '|----|----|--|-' + '"')
    o.system('echo ' + '"' + '--------------' + '"')
    o.system('clear')
    tm.sleep(0.1)
    o.system('echo ' + '"' + "            --" + '"')
    o.system('echo ' + '"' + '           | |' + '"')
    o.system('echo ' + '"' + '           | |' + '"')
    o.system('echo ' + '"' + '           | |' + '"')
    o.system('echo ' + '"' + '           | |' + '"')
    o.system('echo ' + '"' + '|----|----|--|-' + '"')
    o.system('echo ' + '"' + '|----|----|--|-' + '"')
    o.system('echo ' + '"' + '|----|----|--|-' + '"')
    o.system('echo ' + '"' + '|----|----|--|-' + '"')
    o.system('echo ' + '"' + '--------------' + '"')
    o.system('echo ' + '"' + '--------------' + '"')
    o.system('clear')
    o.system('echo ' + '"' + "            --" + '"')
    o.system('echo ' + '"' + '           | |' + '"')
    o.system('echo ' + '"' + '           | |' + '"')
    o.system('echo ' + '"' + '           | |' + '"')
    o.system('echo ' + '"' + '           | |' + '"')
    o.system('echo ' + '"' + '|----|----|--|-' + '"')
    o.system('echo ' + '"' + '|----|----|--|-' + '"')
    o.system('echo ' + '"' + '|----|----|--|-' + '"')
    o.system('echo ' + '"' + '|----|----|--|-' + '"')
    o.system('echo ' + '"' + '--------------' + '"')
    o.system('echo ' + '"' + '              ' + '"')
    o.system('echo ' + '"' + '--------------' + '"')
    tm.sleep(0.1)
    o.system('clear')


def ikun():
    py.mixer.init()
    py.init()
    try:
        aa = open('3082041059.mp3', 'r')
        aa.read()
        o.system('python3 xcd.py')
    except FileNotFoundError:
        o.system('sudo wget https://other-web-ri01-sycdn.kuwo.cn/c07b483ca63c414eb283066845cad1fa/6363bea8/resource/n1/87/57/3082041059.mp3')
    py.mixer.music.load('3082041059.mp3')
    py.mixer.music.play(-1, 0)
    def event():
      for event in py.event.get():
        if event.type == py.KEYDOWN and event.key == py.K_ESCAPE:
          py.quit()
          sy.exit()
    while True:
      py.display.update()
      event()
def 等(秒数):
    tm.sleep(秒数)


def 小彩蛋():
    try:
        xcd = open('xcd.py', 'r')
    except FileNotFoundError:
        xcdxr = open('xcd.py', 'w', encoding='utf-8')
        xcdxr.write('''
import easygui as e\n
import pygame as py\n
import sys as sy\n
from pygame.locals import *\n
py.init()\n
py.mixer.init()\n
py.mixer.music.load('halls.mp3')\n
py.mixer.music.play(-1, 0)\n
canvas = py.display.set_mode((500, 500))\n
pdk = py.image.load('pdk.png')\n
sxk = py.image.load('sxk.png')\n
canvas.blit(sxk, (-200, 0))\n
canvas.blit(pdk, (200, 0))\n
pdkx = 100\n
sxkx = 100\n
\n
\n
def sc():\n
    global pdkx\n
    global sxkx\n
    for event in py.event.get():\n
        if event.type == py.QUIT:\n
            py.quit()\n
            sy.exit()\n
        elif event.type == py.KEYDOWN and event.key == py.K_SPACE:\n
            pdkx = int(pdkx)\n
            pdkx -= 10\n
            pdkx = str(pdkx)\n
            e.msgbox('派对客 减 10 滴血，还剩 ' + pdkx + ' 滴血。')\n
        elif event.type == py.KEYDOWN and event.key == py.K_h:\n
            sxkx = int(sxkx)\n
            sxkx -= 10\n
            sxkx = str(sxkx)\n 
            e.msgbox('扫兴客 减 10 滴血，还剩 ' + sxkx + ' 滴血。')\n
\n
\n
while True:\n
    sc()\n
    \n
    if sxkx == '0':\n
        e.msgbox('扫兴客 输了。')\n
        break\n
    elif pdkx == '0':\n
        e.msgbox('派对客 输了。')\n
        break\n
    py.display.update()\n

        ''')
    o.system('python3 xcd.py')


def 下载pgzero工具():
    try:
        pgzerodl = open('pgzhelper.py', 'r')
    except FileNotFoundError:
        pgzerooo = open('pgzhelper.py', 'w', encoding='utf-8')
        pgzerooo.write('''
import math
import pygame
from pgzero.actor import Actor, POS_TOPLEFT, ANCHOR_CENTER, transform_anchor
from pgzero import game, loaders
import types
import sys
import time
from pgzero.builtins import Actor, animate, keyboard

mod = sys.modules['__main__']
_fullscreen = False

def set_fullscreen():
  global _fullscreen
  mod.screen.surface = pygame.display.set_mode((mod.WIDTH, mod.HEIGHT), pygame.FULLSCREEN)
  _fullscreen = True

def set_windowed():
  global _fullscreen
  mod.screen.surface = pygame.display.set_mode((mod.WIDTH, mod.HEIGHT))
  _fullscreen = False

def toggle_fullscreen():
  if _fullscreen:
    set_windowed()
  else:
    set_fullscreen()

def hide_mouse():
   pygame.mouse.set_visible(False)

def show_mouse():
   pygame.mouse.set_visible(True)

class Actor(Actor):
  def __init__(self, image, pos=POS_TOPLEFT, anchor=ANCHOR_CENTER, **kwargs):
    self._flip_x = False
    self._flip_y = False
    self._scale = 1
    self._mask = None
    self._animate_counter = 0
    self.fps = 5
    self.direction = 0
    super().__init__(image, pos, anchor, **kwargs)

  def distance_to(self, actor):
    dx = actor.x - self.x
    dy = actor.y - self.y
    return math.sqrt(dx**2 + dy**2)

  def direction_to(self, actor):
    dx = actor.x - self.x
    dy = self.y - actor.y

    angle = math.degrees(math.atan2(dy, dx))
    if angle > 0:
      return angle

    return 360 + angle

  def move_towards(self, actor, dist):
    angle = math.radians(self.direction_to(actor))
    dx = dist * math.cos(angle)
    dy = dist * math.sin(angle)
    self.x += dx
    self.y -= dy

  def point_towards(self, actor):
    print(self.direction_to(actor))
    self.angle = self.direction_to(actor)

  def move_in_direction(self, dist):
    angle = math.radians(self.direction)
    dx = dist * math.cos(angle)
    dy = dist * math.sin(angle)
    self.x += dx
    self.y -= dy

  def move_forward(self, dist):
    angle = math.radians(self.angle)
    dx = dist * math.cos(angle)
    dy = dist * math.sin(angle)
    self.x += dx
    self.y -= dy

  def move_left(self, dist):
    angle = math.radians(self.angle + 90)
    dx = dist * math.cos(angle)
    dy = dist * math.sin(angle)
    self.x += dx
    self.y -= dy

  def move_right(self, dist):
    angle = math.radians(self.angle - 90)
    dx = dist * math.cos(angle)
    dy = dist * math.sin(angle)
    self.x += dx
    self.y -= dy

  def move_back(self, dist):
    angle = math.radians(self.angle)
    dx = -dist * math.cos(angle)
    dy = -dist * math.sin(angle)
    self.x += dx
    self.y -= dy

  @property
  def images(self):
    return self._images

  @images.setter
  def images(self, images):
    self._images = images
    if len(self._images) != 0:
      self.image = self._images[0]

  def next_image(self):
    if self.image in self._images:
      current = self._images.index(self.image)
      if current == len(self._images) - 1:
        self.image = self._images[0]
      else:
        self.image = self._images[current + 1]
    else:
      self.image = self._images[0]

  def animate(self):
    now = int(time.time() * self.fps)
    if now != self._animate_counter:
      self._animate_counter = now
      self.next_image()

  @property
  def angle(self):
    return self._angle

  @angle.setter
  def angle(self, angle):
    self._angle = angle
    self._transform_surf()

  @property
  def scale(self):
    return self._scale

  @scale.setter
  def scale(self, scale):
    self._scale = scale
    self._transform_surf()

  @property
  def flip_x(self):
    return self._flip_x

  @flip_x.setter
  def flip_x(self, flip_x):
    self._flip_x = flip_x
    self._transform_surf()

  @property
  def flip_y(self):
    return self._flip_y

  @flip_y.setter
  def flip_y(self, flip_y):
    self._flip_y = flip_y
    self._transform_surf()

  @property
  def image(self):
    return self._image_name

  @image.setter
  def image(self, image):
    self._image_name = image
    self._orig_surf = self._surf = loaders.images.load(image)
    self._update_pos()
    self._transform_surf()

  def _transform_surf(self):
    self._surf = self._orig_surf
    p = self.pos

    if self._scale != 1:
      size = self._orig_surf.get_size()
      self._surf = pygame.transform.scale(self._surf, (int(size[0] * self.scale), int(size[1] * self.scale)))
    if self._flip_x:
      self._surf = pygame.transform.flip(self._surf, True, False)
    if self._flip_y:
      self._surf = pygame.transform.flip(self._surf, False, True)

    self._surf = pygame.transform.rotate(self._surf, self._angle)

    self.width, self.height = self._surf.get_size()
    w, h = self._orig_surf.get_size()
    ax, ay = self._untransformed_anchor
    anchor = transform_anchor(ax, ay, w, h, self._angle)
    self._anchor = (anchor[0] * self.scale, anchor[1] * self.scale)

    self.pos = p
    self._mask = None

  def collidepoint_pixel(self, x, y=0):
    if isinstance(x, tuple):
      y = x[1]
      x = x[0]
    if self._mask == None:
      self._mask = pygame.mask.from_surface(self._surf)

    xoffset = int(x - self.left)
    yoffset = int(y - self.top)
    if xoffset < 0 or yoffset < 0:
      return 0

    width, height = self._mask.get_size()
    if xoffset > width or yoffset > height:
      return 0

    return self._mask.get_at((xoffset, yoffset))

  def collide_pixel(self, actor):
    for a in [self, actor]:
      if a._mask == None:
        a._mask = pygame.mask.from_surface(a._surf)

    xoffset = int(actor.left - self.left)
    yoffset = int(actor.top - self.top)

    return self._mask.overlap(actor._mask, (xoffset, yoffset))

  def collidelist_pixel(self, actors):
    for i in range(len(actors)):
      if self.collide_pixel(actors[i]):
        return i
    return -1

  def collidelistall_pixel(self, actors):
    collided = []
    for i in range(len(actors)):
      if self.collide_pixel(actors[i]):
        collided.append(i)
    return collided

  def obb_collidepoints(self, actors):
    angle = math.radians(self._angle)
    costheta = math.cos(angle)
    sintheta = math.sin(angle)
    width, height = self._orig_surf.get_size()
    half_width = width / 2
    half_height = height / 2

    i = 0
    for actor in actors:
      tx = actor.x - self.x
      ty = actor.y - self.y
      rx = tx * costheta - ty * sintheta
      ry = ty * costheta + tx * sintheta

      if rx > -half_width and rx < half_width and ry > -half_height and ry < half_height:
        return i
      i += 1

    return -1

  def obb_collidepoint(self, x, y=0):
    if isinstance(x, tuple):
      y = x[1]
      x = x[0]
    angle = math.radians(self._angle)
    costheta = math.cos(angle)
    sintheta = math.sin(angle)
    width, height = self._orig_surf.get_size()
    half_width = width / 2
    half_height = height / 2

    tx = x - self.x
    ty = y - self.y
    rx = tx * costheta - ty * sintheta
    ry = ty * costheta + tx * sintheta

    if rx > -half_width and rx < half_width and ry > -half_height and ry < half_height:
      return True

    return False

  def circle_collidepoints(self, radius, actors):
    rSquare = radius ** 2

    i = 0
    for actor in actors:
      dSquare = (actor.x - self.x)**2 + (actor.y - self.y)**2

      if dSquare < rSquare:
        return i
      i += 1

    return -1

  def circle_collidepoint(self, radius, x, y=0):
    if isinstance(x, tuple):
      y = x[1]
      x = x[0]
    rSquare = radius ** 2
    dSquare = (x - self.x)**2 + (y - self.y)**2

    if dSquare < rSquare:
      return True

    return False
      

  def draw(self):
    game.screen.blit(self._surf, self.topleft)

  def get_rect(self):
    return self._rect

        ''')


def flask模板():
  try:
    fkmb = open('flaskk.py','r')
    fkmb.read()
    o.system('python3 flaskk.py')
  except FileNotFoundError:
    fkmbb = open('flaskk.py','w')
    fkmbb.write('''
from flask import Flask
app = Flask('__name__')
@app.route('/')

def start():
    f = open('1.html','r',encoding='utf-8')
    a = f.read()
    return a
@app.route('/你干嘛点我/')

def ngmdw():
    f = open('2.html','r',encoding='utf-8')
    a = f.read()
    return a
if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8080') 
    ''')
    fkhtml = open('1.html','w')
    fkhtml.write('''
<!DOCTYPE html>
<html>
    <title>114514</title>
    <h1>你干嘛！！！！！！！！！</h1>
    <button onclick="window.location.href = 'https://www.bilibili.com/'">点我！！！！！！</button>
    <button onclick="window.location.href = '/你干嘛点我/'">别点我！！！！！！</button>
</html>
    ''')
    fkhtml2 = open('2.html','w')
    fkhtml2.write('''
<!DOCTYPE html>
<html>
    <title>1919810</title>
    <h1>你干嘛点我？？？？？？？？</h1>
    <button href="#" onclick="javascript:history.back(-1);">回去</button>
    <button onclick="window.location.href = 'https://www.bilibili.com/video/BV1754y1o743/?spm_id_from=333.788.recommend_more_video.0&vd_source=a6536909fc1cf7d1d58f68ee41137d73'">被撅</button>
</html>
    ''')
    o.system('python3 flaskk.py')