import re

def teamdj():
    i = input('模式菜单：\n\n1.计算尺寸\n2.估算利润\n3.净利率预估产品成本\n4.净利预估产品成本\n\n输入数字选择模式：')
    global cal_profit
    if i == '1':
        print('\n===============================================================')
        print('                     重选模式按回车')
        print('===============================================================\n')
        while True:
            t = cal_size()
            
            if t == 1:
                teamdj()
                break
    elif i == '2':
        print('\n===============================================================')
        print('输入尺寸（Size），不带“cm”单位的都会转换成厘米\n'
              '重量（Weight）输入单位默认为磅，其他单位需要带上单位符号（kg/ounces）'
              '\n成本（Cost）输入为人民币\n'
              '价格（price）输入单位为美元\n'
              '只想看尺寸再按一次回车（Enter）')
        print('===============================================================\n')
        cal_profit = True
    elif i == '3':
        print('\n===============================================================')
        print('输入尺寸（Size），不带“cm”单位的都会转换成厘米\n'
              '重量（Weight）输入单位默认为磅，其他单位需要带上单位符号（kg/ounces）\n'
              '价格（price）输入单位为美元\n'
              '预估成本价格区间，默认利率15%')
        print('===============================================================\n')
        cal_profit = True
    elif i == '4':
        print('\n===============================================================')
        print('输入尺寸（Size），不带“cm”单位的都会转换成厘米\n'
              '重量（Weight）输入单位默认为磅，其他单位需要带上单位符号（kg/ounces）\n'
              '价格（price）输入单位为美元\n'
              '预估成本价格区间，默认利润￥30')
        print('===============================================================\n')
        cal_profit = True
    else:
        cal_profit = False
        teamdj()
    profit(cal_profit, i)
def cal_size():
    global pattern
    a = input('Size:')
    a = a.lower()
    if a is '':
        print('===============================================================\n')
        return 1
    if a.isalpha():
        print('===============================================================\n')
        return 0
    a = a.replace('*', 'x').replace('×', 'x').replace('X', 'x')
    
    countx = a.count("x")
    b = a
    if countx == 0 and a.isdigit():
        print('\n{0:.2f}cm\n'.format(float(a) * 2.54))
        return 0
    elif countx == 1:
        a = re.sub(pattern, '', a)
        x, y = a.split('x')
        print('\n{0:.2f} x {1:.2f}cm\n'.format(float(x) * 2.54, float(y) * 2.54))
        return 0
    elif countx == 2:
        a = re.sub(pattern, '', a)
        x, y, z = a.split('x')
        x, y, z = float(x), float(y), float(z)
        if 'cm' in b:
            q = x * y * z / 10 ** 6
            print('{0:.2f}\t{1:.2f}\t{2:.2f}'.format(x, y, z))
            x, y, z = x / 2.54, y / 2.54, z / 2.54
            return q, x, y, z
        else:
            q = x * y * z * 2.54 ** 3 / 10 ** 6
            print('{0:.2f} x {1:.2f} x {2:.2f}cm'.format(x * 2.54, y * 2.54, z * 2.54))
            # print('{0:.2f}\t{1:.2f}\t{2:.2f}'.format(x * 2.54, y * 2.54, z * 2.54))
            return q, x, y, z

def fbafee(arr, w):
    list1 = [i for i in arr[1:]]
    list1.sort()
    q = arr[0]
    sw = max([w, q * 200 / 0.454])
    sw = (sw - 0.0001) // 1 + 1
    fw = max([w * 0.454, q * 200])
    if list1[0] <= 8 and list1[1] <= 14 and list1[2] <= 18:
        if sw <= 1:
            p = 3.19
        elif sw <= 2:
            p = 4.71
        else:
            p = 4.71 + 0.38 * (sw - 1)
    else:
        if sw < 2:
            p = 8.13
        else:
            p = 8.13 + 0.38 * (sw - 1)
    return p, q, fw

def weight():
    w = input('Weight:')
    w = w.lower()
    w2 = w
    if not startover(w2):
        return
    w = re.sub(pattern, '', w)
    if w:
        w = float(w)
        if 'ounce' in w2:
            w = w / 16
        elif 'kg' in w2:
            w = w / 0.454
        print('{0:.2f}g |  {1:.2f}kg'.format(w * 454, w * 0.454))
        return w

def startover(i):
    if i == '':
        print('===============================================================\n')
        return 0
    else:
        return 1

def restart(i):
    if i == 'q':
        print('===============================================================\n')
        return 0
    else:
        return 1

def calcu_profit(pattern, fba):
    sfare = fba[1] * 1150 + fba[0] * 6.8
    ffare = fba[2] * 30 + fba[0] * 6.8
    cost = input('Cost(￥):')
    cost2 = cost
    cost = re.sub(pattern, '', cost)
    if cost is '':
        print('===============================================================\n')
        return

    while True:
        price = input('Price($);')
        if not restart(price):
            break
        price = re.sub(pattern, '', price)
        if startover(price):
            sprofit = float(price) * 6.8 * 0.78 - float(cost) * 0.97 - sfare
            fprofit = float(price) * 6.8 * 0.78 - float(cost) * 0.97 - ffare
            sinter_rate = float(sprofit) / float(price) / 6.8
            finter_rate = float(fprofit) / float(price) / 6.8
            print(' --------------------------------------------------')
            print('|     海运 Profit       |         Interest rate      |')
            print(' --------------------------------------------------')
            print('|        {0:<13.2f}  |         {1:<19.2%}|'.format(sprofit, sinter_rate))
            print(' --------------------------------------------------')
            print('|     空运 Profit       |         Interest rate      |')
            print(' --------------------------------------------------')
            print('|        {0:<13.2f}  |         {1:<19.2%}|'.format(fprofit, finter_rate))
            print(' --------------------------------------------------')
            print('输入q退出')
        else:
            teamdj()

def estimate_cost(fba):
    net_profit = input('输入想要的利润率：')
    if net_profit == '':
        net_profit = '0.15'
    net_profit = re.sub(pattern, '', net_profit)
    net_profit = float(net_profit) / 100
    sfare = fba[1] * 1150 + fba[0] * 6.8
    while True:
        price = input('Price($);')
        price = re.sub(pattern, '', price)
        if price is '':
            print('===============================================================\n')
            return 0
        cost = (float(price) * (0.78 - net_profit) * 6.8 - sfare) / 0.97
        print('Net profit is:￥{0:.2f}'.format(float(price) * 6.8 * net_profit))
        print("Cost needs to be lower than :￥{0:.2f} ".format(cost))

def estimate_cost2(fba):
    net_profit = input('输入想要的净利润：')
    if net_profit == '':
        net_profit = '30'
    net_profit = re.sub(pattern, '', net_profit)
    net_profit = float(net_profit)
    sfare = fba[1] * 1150 + fba[0] * 6.8
    while True:
        price = input('Price($);')
        price = re.sub(pattern, '', price)
        if price is '':
            print('===============================================================\n')
            return 0
        cost = (float(price) * 0.78 * 6.8 - sfare - net_profit) / 0.97
        print('Net profit rate is:{0:.2%}'.format(net_profit / float(price) / 6.8 ))
        print("Cost needs to be lower than :￥{0:.2f} ".format(cost))

def profit(cal_profit, i):
    while cal_profit:
        mode = ['计算尺寸','估算利润','毛利率预估产品成本','毛利预估产品成本']
        print('Size：输入回车返回重选模式\n')
        print(mode[int(i)-1] + ':')
        size = cal_size()
        if size == 0 or size == 1:
            teamdj()
        w = weight()
        
        #print('{0:.2f}\t{1:.2f}\t{2:.2f}\t{3:.2f}'.format(size[1] * 2.54, size[2] * 2.54, size[3] * 2.54, w * 0.454))
        if w:
            print('{0:.2f}\t{1:.2f}\t{2:.2f}\t{3:.2f}'.format(size[1] * 2.54, size[2] * 2.54, size[3] * 2.54, w * 0.454))
            fba = fbafee(size, w)
            if i == '2':
                calcu_profit(pattern, fba)
            elif i == '3':
                estimate_cost(fba)
            elif i == '4':
                estimate_cost2(fba)

if __name__ == '__main__':
    cal_profit = False
    pattern = re.compile('[zcvbnmasdfghjklqwertyuiop\"\’\'\”\(\)\%\%]')
    teamdj()
