print('''
 _____      __   ___            ___  ___      ___   ____________        ___           ___   
|     \    |  |  \  \          /  /  |  |    /  /  |____    ____|      |   |         |   |
|  |\  \   |  |   \  \        /  /   |  |   /  /        |  |           |   |         |   |
|  | \  \  |  |    \  \      /  /    |  |__/  /         |  |           |   |         |   |
|  |  \  \ |  |     \  \    /  /     |  |__  |          |  |      ____/    |    ____/    |
|  |   \  \|  |      \  \  /  /      |  |  \  \         |  |     /   ___   |   /   ___   |  
|  |    \  \  |       \  \/  /       |  |   \  \        |  |    |   |___|  |  |   |___|  |
|__|     \____|        \____/        |__|    \__\       |__|     \ _______/    \ _______/
''')
import os
import time

print('请先将手机插上电脑，确保手机已开启USB调试模式')
input('<enter>')
#连接adb
os.system('adb -d')
print('adb连接中...')
device_name = os .system(f'adb device') 
print('连接设备:',device_name)
#adb_shell终端指令输入
def adb_cmd(cmd):
    output_date = os.popen(f"adb shell {cmd}")
    print(output_date.read())

#模拟鼠标的点击事件，x，y为点击的坐标
def touch(x, y):
    adb_cmd(f'input tap {x} {y}')

#模拟文字输入事件，text输入字符串
def text(text):
    adb_cmd(f'input text {text}')

#模拟滑动事件，x1,y1为起始坐标,x2,y2为终点坐标，t为滑动的时间
def swipe(x1,y1,x2,y2,t):
    adb_cmd(f'input swipe {x1} {y1} {x2} {y2} {t}')

#模拟按键事件，3代表回主页按键，4代表返回按键
def keyevent(x):
    adb_cmd(f'input keyevent {x}')

#模拟拖动事件，x1,y1为起始坐标,x2,y2为终点坐标，t为拖动的时间
def draganddrop(x1,y1,x2,y2,t):
    adb_cmd(f'input draganddrop {x1} {y1} {x2} {y2} {t}')

#xinchen input
print('adb日志监测开始')
time.sleep(2)
adb_cmd('logcat -c')  
input('打开MC,进入XincChen服务器并按下Shift(潜行)键,手持钟。<enter>')

#xz = input
right_x = int(input('请输入x右键坐标:'))

right_y = int(input('请输入y右键坐标:'))

def right_click():
    touch(right_x,right_y)
    print('adb日志:模拟鼠标的点击事件')

Shop_x = int(input('请输入x商店坐标:'))
Shop_y = int(input('请输入y商店坐标:'))

def shop_click():
    touch(Shop_x,Shop_y)
    print('adb日志:模拟鼠标的点击事件')

ap_x = int(input('请输入全部物品x坐标:'))
ap_y = int(input('请输入全部物品y坐标:'))
def all_wp_click():
    touch(ap_x,ap_y)
    print('adb日志:模拟鼠标的点击事件')

diyu_x = int(input('请输入地狱岩x坐标:'))
diyu_y = int(input('请输入地狱岩y坐标:'))
def diyu_click():
    touch(diyu_x,diyu_y)
    print('adb日志:模拟鼠标的点击事件')


back_shop_x = int(input('请输入返回x坐标:'))
back_shop_y = int(input('请输入返回y坐标:'))
def back_shop_click():
    touch(back_shop_x,back_shop_y)
    print('adb日志:模拟鼠标的点击事件')

recycling_x = int(input('请输入回收x坐标:'))
recycling_y = int(input('请输入回收y坐标:'))
def recycling_click():
    touch(recycling_x,recycling_y)
    print('adb日志:模拟鼠标的点击事件')

diyu_x_recycling = int(input('请输入地狱岩回收x坐标:'))
diyu_y_recycling = int(input('请输入地狱岩回收y坐标:'))
def diyu_recycling_click():
    touch(diyu_x_recycling,diyu_y_recycling)
    print('adb日志:模拟鼠标的点击事件')

#开始循环
next = input('循环次数：0=无限循环，其他数字为循环次数')
while next != '0':
    right_click()
    time.sleep(1)
    time.sleep(1)
    all_wp_click()
    time.sleep(1)
    time.sleep(1)
    diyu_click()
    time.sleep(1)
    time.sleep(1)
    back_shop_click()
    time.sleep(1)
    recycling_click()
    time.sleep(0.5)
    diyu_recycling_click()
    time.sleep(0.5)
    print('已完成一次循环,你赚了 values: object, sep: str | None = " ", end: str 金币！')