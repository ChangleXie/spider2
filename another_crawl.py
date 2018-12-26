# -*- coding: utf-8 -*-

from threading import Thread, Lock
from time import clock, strftime, localtime, time, sleep
from queue import Queue
from pandas import DataFrame
from requests import Session, get
from bs4 import BeautifulSoup
from tkinter import Tk, Label, Button, Text, END, RAISED, messagebox
from re import match, compile, findall, split
from os import mkdir, listdir, remove
from os.path import exists
from shutil import copy
from xlrd import open_workbook
from xlsxwriter import Workbook
from random import random
from sys import version_info
from hashlib import sha1, sha256
from hmac import new
from urllib import parse, request
from json import loads
from binascii import b2a_base64

secretId = "AKIDU3VmspxKo6FF8qwvaaTBhcs44sK06iME"
secretKey = "udDdrMmAa2a8hIm9JH3cKya3ZzMi8Vhl"

# 解析网页
def urlread(url):
    # cookie = {'lc - main': 'en_US',
    #           '_ga': 'GA1.2.756134632.1531984968',
    #           'skin': 'noskin',
    #           's_vnum': '1966818137631%26vn%3D1',
    #           's_sq': '%5B%5BB%5D%5D',
    #           's_nr': '1534818157195 - New',
    #           's_dslv': '1534818157196',
    #           'session-id-eu': '258-4463840-9142617',
    #           'session-id-time-eu': '2166172330l',
    #           'ubid-acbuk': '257-1491900-8219228',
    #           'at-main': 'Atza|IwEBIFV5P-sIm76hFwOylP0chh70uKyT85j55Vz7dxDKQ9D17v\
    #                       9CZJ4mfydAeAIHxfIvsEdfcvTd-Y2vQp9osHeiT0-yeY1WaiEQUrgKEK1REtuAZG7ojk\
    #                       9YGjqpG1l7mwRdEWpVYfbHjstOYb - Q0NvCzZKHAv9vu - x6U1ttTTOodD3SSkG5uGqrcc\
    #                       ZBZmjPcsUMIZprLtalNCDzaqp3bEJWzzs7g1VUqjkSNp2RTiEfQ99jIMLMTQD0kyHzEKes79PtLkPa0f\
    #                       I6tgsJSaIcUgP1dKVYcAKwhiloAfHbtTX9DJa1LMYoMxEs1Wqqxf76WIeOK-NmmfHNztCLVpADZpaR4IE\
    #                       95JprxEs9jtEOdziTpuCZzHAGXFuuYxNx2_bO9XqsSCQVl7jQx9oLZdh5X7DL9uuu',
    #           'sess-at-main': '2+VbkU2crE/GD8uR2Q452ypk1LJ8J8d3ctlFlK2BuS0=',
    #           'sst-main': 'Sst1|PQH04JbkHWVGywVZDC1l1F3IC5bKyYMsW6AUuDhEZ8p0eIzuHv\
    #                        yy0gkChaoKGBA4z1OufCyRcM4-vjpVmb4IT6lXcP6b1t_jKTa2cbMJMeHJNVruiC_kzgwY\
    #                        oVP_fR-5xB6qkp9LnKYJpctTYui5rIAEvRwPABLh6ymsqlUuoW - iQ6S9YhW0_ - w6iiY\
    #                        T8n4YeaHRaBtkLXdP2hcI1HJqb8NR7K9TV0axBCUuZV3yZ1vy6F0XtyGuekcSVqoFz9QLGbz\
    #                        MGUcsLesruLM5YTSG - CzK1Im60VhGhKGccokNHFooJzcivwFAOIiyJtXMkYjYuCqPQKcjyln6jOTnB8OXedSstw',
    #           's_pers': '%20s_fid%3D2FC5ADE05BDB7F64-15749A3B11AC9F26%7C1695189768397%\
    #                      3B%20s_dl%3D1%7C1537425168398%3B%20gpv_page%3DUS%253AAS%253AFBA-pricing%7\
    #                      C1537425168402%3B%20s_ev15%3D%255B%255B%2527ASUSFBADirect%2527%252C%252715\
    #                      37423368404%2527%255D%255D%7C1695189768404%3B',
    #           's_sess': '%20s_sq%3D%3B%20ev1%3Dn%2Fa%3B%20s_cc%3Dtrue%3B%20s_ppvl%3DUS%25253AAS%252\
    #                      53AFBA-pricing%252C48%252C31%252C1681%252C1920%252C981%252C1920%252C1080%252C1%252CL%\
    #                      3B%20c_m%3DTyped%252FBookmarkedTyped%252FBookmarkedundefined%3B%20s_ppv%3DUS%25253AAS\
    #                      %25253AFBA-pricing%252C100%252C31%252C3816%252C1920%252C981%252C1920%252C1080%252C1%252CL%3B',
    #           'session-id-time': '2082787201l',
    #           'x-main': 'hx1bxR66?KB2XXxetFp29keH6JeX876wFqRpIJa0MqHTaEJ?sMqmbcebyTxS8XvN',
    #           'ubid-main': '131-0928638-4831508',
    #           'session-id': '144-1823531-9706327',
    #           'x-wl-uid': '1Jh6JJEsFMgpZqrMPOiAIp7q+6i6CK5/+AIbyvZl+IdBj9kG4uBlzUFPCqc/uzrrKBkEmsi\
    #                        TLwlhYZSOeJL9m4fAY2hn4y8IV4vnd/aCxoFlx024wecoFhk52fk0Vu3BzFkYgBoYf3ZM=',
    #           'session-token': '"3cJO0LXxF2W2D58hiXH7sl1D6BgCQ32Y4SALivT2zPz1EyUndo4UwuT1TCiFfCVtDJ\
    #                              BYvOkPPR/tZCVA3IH724jA2LSi0UuQdT6xD0ucfqHSU+V791P3zebGlbIJVyfMe1qMauheg0my90/zvqgRFJJx\
    #                              pbTvkMzng4LS55pGgovyIvkweZliNiepi7uLLpIp8Z0Qu0PbTgYLbQTD29PcgTagoTAwzXteZY3WOvx3UeLgl\
    #                              m5ZADAJ3QjW6lip/v1DTw/mB8rp/exv2MlQlyb7WQ=="',
    #           }
    cookie = {'session-id': '134-3856831-6537631',
              'session-id-time': '2082787201l',
              'ubid-main': '130-1157931-8753215',
              's_fid': '4FD2C3C011299EE8-021F9EAFC572E127',
              's_dslv_s': 'First%20Visit',
              's_vn': '1572424924025%26vn%3D1',
              's_invisit': 'true',
              'regStatus': 'pre-register',
              's_cc': 'true',
              'aws-priv': 'eyJ2IjoxLCJzdCI6MX0=',
              's_depth': '3',
              's_dslv': '1540889004876',
              's_nr': '1540889004877-New',
              'a-ogbcbff': '1',
              'session-token': "XT04m2XC5juHX3i+mD5nd1zVynI8BBpKDb2uPsWRE+8UDWUdUiXr/nsQ83416x9vEKAM8kFqdSfI+adjwQOEzJVxi7PqYJza50ac90mWk9PioGVgm9cBUYyw/nHpQq6RR4N7EnJzAJyJVPrVB2vMiQ8ky8qZG2xTzHMU1qMbjNXWylJseSVFIthckiR9U2iABztN1qw5EQtAhm7R8HpEyrRYq0l7sa1HYSM9sq3yOeo=",
              'x-main': "PoWZ3rCn6D9ji?xtgsYr8uztxg9JB6dks4iF3zSRFJjawUDjZR7eFCVj6MP0@m9q",
              'at-main': 'Atza|IwEBII5BxWpps3ravM52GNR7oLZ6VewyY4hxMykt_m94zkGp_6Wf-XPVd1DOX0ioAMGyBqPncEceKRc_9kzSZ1vdDQc5cX2juiW4rUWKnRO-U1COjGl3iqIR8Yf1JLZwnYLgjkX--FOUDEeZXtTbyHvsmNsLS0Lc8BboA7Tp8AFRVZTvgWm2EB186NJKm8wJXNgsOuj94NkFp9UbuBPlY7cfaH6iQg8W1yfjp4XTB8p_SYE1yXDr_bFbEUorcEMRgoGHz2KeBr1LIKyEEyXYgaROUBbpiAywijGPo1WA6j1S-3JAwN6oOqE96ag1dxLhqwRyaqOijDZoGJxWL6gV3bLrqCMcGHWgofOKFynd6kyfFlBIIMFDi3KROqq1y9SgnR1wbg_em19l8_DRHzXGHKccaIIk',
              'sess-at-main': '"YSLtfGHW3yvMfEy/nQpu9Edyj4aXcjDnbjsfl2TT5xA="',
              'sst-main': 'Sst1|PQFT0zg0UbdXrmR0ohnZgoejC-Dpn37khTJS4YoeexmrA6z1zkSSwaXBmgtWznvt8YdqG4wjh6z-zXF8r3hO6HABT6YB6W2ELV-OppbqrW1abrJNneG38MS-1G1gKvkmT-VA4e_Lx5aHxQiWkMu5WatDLZVWUhUBCcaHvHeMT8j_LddjHXZskmN9gDamMMCA9WvOJbQMl4dTZlqdRXOGNUypEiziOfSlRLe8Ojn2H9LCqNLektine0nLTIbaPJcNCHq1IEo2cc3Sx4vYLvfUnPTPij6Itghi7DxnHhDUEY9G8oPto0tKTHOQJpbXhHfihCpHc1_7KIev1Dce5MdtmREZJQ',
              'lc-main': 'en_US',
              'x-wl-uid': '1gcAWcUxqoUoSCND3zabY7xQtrE1c8wWhsrfn8NwTyvWPgpjEnWfI/VBLzn0pwcamFEXs9CmGDUywbOllXHI6Aav2VQB1lVCorL+J6q0zW8vv6yhnP5wfoaQhhca7pZQTsFnftvRfpEw='}
    headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0'}
    # proxy = {'http': 'http://222.76.204.110:808'}
    f = get(url, headers=headers, cookies=cookie).text
    soup = BeautifulSoup(f, 'lxml')

    return soup


# 获取卖点
def getfeatures(url):
    soup2 = urlread(url)
    #print(soup2)
    getfeat = soup2.find(id='feature-bullets')
    features = getfeat.find_all('li')
    #print(features)
    title = soup2.find(id='productTitle')
    title = list(title)
    title.extend(features)
    res = []
    q = ''
    for i in title:
        if type(i.string) != type(None):
            k = i.string.strip().lower().replace('%', 'percent').replace('&', 'and')
            # print(k)
            res.append(i.string.strip())

            try:
                q = translate(secretId, secretKey, k.encode('ascii', 'ignore')).replace('B', '').replace('‘', '').replace('b', '').replace('’', '').replace('”', '').replace('“', '')
                #print(k+'-'*20+q)

            except KeyError:
                #print('\n<Error>getfeatures failed ' + url)
                pass

        res.append(q)
        res2 = []
    for i in res:
        if i not in res2:
            res2.append(i)
    return res2


# 获取排名和链接
def getrank(url, amaurl):
    rankurl = urlread(url)
    ranks = rankurl.find_all(class_='a-section a-spacing-none aok-relative')
    prolist = []

    for rank in ranks:
        try:
            try:
                prolink = rank.find_all(class_='a-link-normal')[0]['href']
                ranknum = rank.find(class_='zg-badge-text').string.strip()
            except IndexError as e:
                print(e)
            prolist.append([ranknum, amaurl+prolink])
        except TypeError as e:
            print('\n<Error>get rank failed')
            print(e)

    return prolist


# 获取51-100名链接
def next_page(url):
    nexturl = urlread(url).find('li', class_='a-last')

    return nexturl.a['href']


# 去掉排名前的'#'，用以排序
def ranknum(list):
    return int(list[0][1:])


# 获取类目名
def get_subcat(url):
    soup = urlread(url)
    subcat = soup.find(class_='zg_selected').string.strip()
    return subcat


# 用默认图片补上缺失图片
def fix_imgs(dirname, picname):

    ress = listdir(dirname)
    list = ['rank#%d_%d.jpg' % (i, j) for i in range(1, 101) for j in range(1, 8)]
    filenames = [i for i in list if i not in ress]
    for filename in filenames:
        copy(picname, dirname + '/' + filename)


# 下载产品图片
def getimgs(item, subtitle):

    print('正在下载%s名的产品图片' % item[0])
    soup = urlread(item[1])
    sleep(1)
    pattern = r'\'colorImages\': { \'initial\': \[\{(.*?)}]}'
    reg = compile(pattern)
    res = findall(reg, str(soup))
    pattern2 = r'https://images-na.ssl-images-amazon.com/images/I/[\w%\-]+\.jpg'
    reg2 = compile(pattern2)
    res2 = findall(reg2, res[0])
    res3 = []
    for link in res2:
        if link not in res3:
            res3.append(link)
    if len(res3) > 7:
        res3 = res3[:7]

    path = subtitle + '_imgs'
    if not exists(path):
        mkdir(path)
    for i, v in enumerate(res3):
        print('Downloading:%s_%d' % (item[0], (i + 1)) + '.' * i)
        ir = get(v)
        open(r'%s/rank%s_%d.jpg' % (path, item[0], i + 1), 'wb').write(ir.content)


# 统计词频
def freq_word(arr):
    res = ''
    for i in [shit for shit in arr]:
        for j in i:
            res += str(j)
    puncs = [',', ':', '★', '(', ')', '/', '@', '=', ]
    for punc in puncs:
        res = res.replace(punc, ' ')
    freq = {}
    for word in res.lower().split():
        if word not in freq:
            freq[word] = 1
        else:
            freq[word] += 1
    words = ['and', 'to', 'the', 'for', 'of', 'is', 'your', '&', 'are', 'x', 'on', 'or',
             'that', 'in', 'from', 'you', 'any', 'a', 'no', 'which', 'it', 'when', 'can',
             '-', 'with', 'i', 'ii', 'iii', 'vi', 'needs', 'us', '.', 'we', '–', 'not',
             'this', 'will', 'be', 'all', 'so', 'also', 'up', 'our', 'them', 'have', 'an',
             '--', 'by',
             ]
    for word in freq.keys():
        if word[-1] == 's':
            if word[:-1] in freq.keys():
                freq[word[:-1]] += freq[word]
                words.append(word)

        if word[-3:] == 'ies':
            if word[:-3]+'y' in freq.keys():
                freq[word[:-3]+'y'] += freq[word]
                words.append(word)

        if len(word) == 1:
            words.append(words)
    for word in words:
        if str(word) in freq:
            freq.pop(word)

    res = sorted(freq.items(), key=lambda item: item[1], reverse=True)
    return res


# 爬取数据写入excel
def excel_writer(data, subtitle):
    maxlen = 0
    columns = ['Rank', 'URL', 'Title', 'Title']
    for item in data:
        maxlen = max(maxlen, len(item))
    colname = ['Feature_%d' % i for i in range(1, maxlen-3)]
    df = DataFrame(data, columns=columns+colname)
    sheetname = subtitle
    if len(sheetname) >= 31:
        sheetname = sheetname[:27] + '...'
    subtitle += '.xls'
    try:
        if exists(subtitle):
            remove(subtitle)
        df.to_excel(subtitle, sheet_name=sheetname, index=None)
    except PermissionError:
        subtitle += strftime('%m%d%H%M', localtime()) + '.xlsx'
        df.to_excel(subtitle, sheet_name=sheetname, index=None)


# 高频词上色
def format_words(book, ws, i, j, sequences, fw):

    def ainb(a, b):
        tails = [')', '(', ',', '\'', '"', '.', '!', '?']
        for i in tails:
            a = a.replace(i, '')
        if a.lower() == b or a.lower() == b+'s' or a[:-3].lower()+'y' == b:
            return True
        else:
            return False

    red = book.add_format({'color': 'red',
                           'bold': 1,
                           'font_name': 'Times New Roman'
                           })
    green = book.add_format({'color': 'green',
                             'bold': 1,
                             'font_name': 'Times New Roman'
                             })
    blue = book.add_format({'color': 'blue',
                            'bold': 1,
                            'font_name': 'Times New Roman'
                            })
    orange = book.add_format({'color': 'orange',
                              'bold': 1,
                              'font_name': 'Times New Roman'
                              })
    normal = book.add_format({'font_name': 'Times New Roman'})
    wraps = book.add_format({
        'align': 'center',
        'valign': 'vcenter',
        'border': 1,
        'font_name': 'Times New Roman'
    })
    wraps.set_text_wrap()
    format_pairs = []
    count = 0
    for word in sequences.split():
        if ainb(word, fw[0][0]):
            format_pairs.extend((red, str(word+' ')))
            count += 1
        elif ainb(word, fw[1][0]):
            format_pairs.extend((green, str(word+' ')))
            count += 1
        elif ainb(word, fw[2][0]):
            format_pairs.extend((orange, str(word+' ')))
            count += 1
        elif ainb(word, fw[3][0]):
            format_pairs.extend((blue, str(word+' ')))
            count += 1
        else:
            format_pairs.extend((normal, str(word+' ')))
    if count >= 1:
        ws.write_rich_string(i, j, *format_pairs, wraps)
    else:
        ws.write(i, j, sequences, wraps)


# 修饰excel，插入图片和词频
def sort_excel(res, save_path, file_name):
    book = Workbook(save_path)
    # 原始数据表格
    excel = open_workbook(save_path)
    sheet2 = excel.sheet_by_index(0)
    ncol = sheet2.ncols
    nrow = sheet2.nrows
    # 表单名
    if len(save_path) > 31:
        save_path = save_path[:31]
    else:
        save_path = save_path[:-4]
    ws = book.add_worksheet(save_path)
    # 表格格式
    format = book.add_format({
        'align': 'center',
        'valign': 'vcenter',
        'border': 1,
        'font_name': 'Times New Roman'
    })
    format.set_text_wrap()
    # 读取初始表格数据
    for i in range(ncol):
        for j in range(nrow):
            # 排名
            if i == 0:
                ws.write(j, i, str(sheet2.col_values(i, j, j + 1)[0]), format)
            # 链接
            elif i == 1 and j != 0:
                ws.write_formula(j, i, 'HYPERLINK("%s","Pro_%d")' % (str(sheet2.col_values(i, j, j + 1)[0]), j), format)
            # URL
            elif i == 1 and j == 0:
                ws.write(j, i, str(sheet2.col_values(i, j, j + 1)[0]), format)
            # features
            elif i > 1 and j == 0:
                pass
            # 卖点和标题
            else:
                format_words(book, ws, j, i+1, str(sheet2.col_values(i, j, j + 1)[0]), res)

    ws.merge_range(0, 3, 0, 4, 'Title', format)
    for i in range(0, ncol-4, 2):
        ws.merge_range(0, i+5, 0, i+6, 'Feature_%d' % int(i/2+1), format)

    # 表格行高
    for i in range(sheet2.nrows - 1):
        ws.set_row(i + 1, 100)
    # 表格列宽
    ws.set_column(0, 0, 5)
    ws.set_column(1, 1, 10)
    ws.set_column(3, ncol, 18)
    # 插入词频
    for i in range(100):
        ws.write(0, ncol+1, 'words', format)
        ws.write(0, ncol+2, 'frequency', format)
        ws.write(i + 1, ncol+1, str(res[i][0]), format)
        ws.write(i + 1, ncol+2, int(res[i][1]), format)
    # 图片列
    # for i in range(7):
    #     ws.write(0, i + 2, 'pic_%s' % str(i + 1), format)
    ws.write(0, 2, 'Picture', format)
    for i in range(100):
        if not exists(file_name + '/rank#%d_%d.jpg' % (i + 1, 1)):
            continue
        ws.insert_image(i + 1, 2, file_name + '/rank#%d_1.jpg' % (i + 1), {'x_scale': 0.2, 'y_scale': 0.2,
                                                                            'x_offset': 10, 'y_offset': 10})

    # 图片列边框、宽度
    cell_format = book.add_format({'border': 1})
    ws.set_column(2, 2, 18, cell_format)
    # 插入词频饼状图
    chart = book.add_chart({'type': 'pie'})
    chart.add_series({
        'name': 'Word Frequency Data',
        'categories': ['%s' % save_path, 1, ncol+1, 11, ncol+1],
        'values': ['%s' % save_path, 1, ncol+2, 11, ncol+2],
        'data_labels': {'value': 1,
                        'category': 1}
    })
    chart.set_title({'name': 'Word Frequency Top 10'})
    chart.set_style(10)
    ws.insert_chart(4, ncol+9, chart, {'x_offset': 25, 'y_offset': 20})
    book.close()


# 添加空白行在下载失败的产品行
def fix_excel(pro_info):
    if len(pro_info) >= 100:
        pass
    else:
        withnum = []
        for item in pro_info:
            withnum.append(int(item[0][1:]))
        for i in range(1,101):
            if i not in withnum:
                pro_info.append(['#%d' % i, 'Download failed', 'Dowload failed', 'Dowload failed', 'Dowload failed', 'Dowload failed', 'Dowload failed', 'Dowload failed'])


# 判断站点
def judge_station(link):
    a = match(r'https://www\.amazon\.(com|co\.uk)/(Best-Sellers|gp/bestsellers)[/|-][\w\-]+[/\w\-=_]+', link)
    try:
        if a.group(1) == 'com':
            amaurl = 'https://www.amazon.com'
        elif a.group(1) == 'co.uk':
            amaurl = 'https://www.amazon.co.uk'
        else:
            messagebox.showinfo('Error', '这个网址不对\n需要输入前50的页面地址\n有问题可以咨询客服')
        return amaurl
    except:
        messagebox.showinfo('Error', '这个网址不对\n需要输入前50的页面地址\n有问题可以咨询客服')
        quit(0)


# 第二页网址更改成第一页
def change_page_num(link):
    pattern = r'(=2|_2)'
    reg = compile(pattern)
    try:
        link2 = split(reg, link)
        if len(link2) == 5:

            res = link2[0] + '_1' + link2[2] + '=1'
            return res
        else:
            return link
    except:
        return link


def sign(secretKey, signStr, signMethod):
    if version_info[0] > 2:
        signStr = signStr.encode("utf-8")
        secretKey = secretKey.encode("utf-8")
    if signMethod == 'HmacSHA256':
        digestmod = sha256
    elif signMethod == 'HmacSHA1':
        digestmod = sha1
    hashed = new(secretKey, signStr, digestmod)
    base64 = b2a_base64(hashed.digest())[:-1]
    if version_info[0] > 2:
        base64 = base64.decode()
    return base64


def dictToStr(dictData):
    tempList = []
    for eveKey, eveValue in dictData.items():
        tempList.append(str(eveKey) + "=" + str(eveValue))
    return "&".join(tempList)


def translate(secretId, secretKey, source_text):
    timeData = str(int(time()))
    nonceData = int(random()*10000)
    actionData = "TextTranslate"
    uriData = "tmt.tencentcloudapi.com"
    signMethod="HmacSHA256"
    requestMethod = "GET"
    regionData = "ap-hongkong"
    versionData = '2018-03-21'
    signDictData = {
        'Action': actionData,
        'Nonce': nonceData,
        'ProjectId': 0,
        'Region': regionData,
        'SecretId': secretId,
        'SignatureMethod': signMethod,
        'Source': "en",
        'SourceText': source_text,
        'Target': "zh",
        'Timestamp': int(timeData),
        'Version': versionData,
    }
    requestStr = "%s%s%s%s%s"%(requestMethod, uriData, "/", "?", dictToStr(signDictData))
    signData = parse.quote(sign(secretKey, requestStr, signMethod))
    actionArgs = signDictData
    actionArgs["Signature"] = signData
    requestUrl = "https://%s/?" % (uriData)
    requestUrlWithArgs = requestUrl + dictToStr(actionArgs)
    responseData = request.urlopen(requestUrlWithArgs).read().decode("utf-8")
    return loads(responseData)['Response']['TargetText']


# 多线程
class Producer(Thread):
    global pro_info

    def __init__(self, pages, subtitle):
        Thread.__init__(self)
        self.pages = pages
        self.subtitle = subtitle
        self.queue = Queue()

    def run(self):
        global count
        while self.pages:
            product = self.pages.pop(0)
            try:
                link = product[1]
                features = getfeatures(link)
                print(features)
                my_lock.acquire()
                temp_list = []
                temp_list.extend([product[0], link])
                for feature in features:
                    temp_list.append(feature)
                pro_info.append(list(temp_list))
                my_lock.release()
                getimgs(product, self.subtitle)
                sleep(0.5)
            except AttributeError as e:
                print('\n<Error>Thread error')
                print(e)


# 添加'Reture'开始功能，补充缺失self属性
def main2(self):
    main()


# 主函数
def main():
    start_time = clock()
    print('Start at: %s...' % strftime('%Y/%m/%d %H:%m', localtime()))
    link = xlsbox.get('1.0', END)
    amaurl = judge_station(link)
    changed_link = change_page_num(link)
    print(changed_link)
    print("Getting Subcategory...")
    subtitle = get_subcat(changed_link)
    dirname = subtitle + '_imgs'
    print('Getting Page2\'s link...')
    picname = 'images.jpg'
    nexturl = next_page(changed_link)
    page1 = getrank(changed_link, amaurl)
    print('Getting Page1\'s links...')
    page2 = getrank(nexturl, amaurl)
    print('Getting Page2\'s links...')
    pages = page1 + page2

    threads = [Producer(pages, subtitle) for i in range(10)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    fix_excel(pro_info)
    pro_info.sort(key=ranknum)
    lists = [info[3:] for info in pro_info]
    # print(lists)
    frequency = freq_word(lists)
    excel_writer(pro_info, subtitle)
    sort_excel(frequency, subtitle + '.xls', dirname)
    end_time = clock()
    time_cost = end_time - start_time
    print('End at: %s...' % strftime('%Y/%m/%d %H:%m', localtime()))
    print('Spent time: {0:.2f}...'.format(time_cost))
    fix_imgs(dirname, picname)
    messagebox.showinfo('Done', '已完成:D 用时{0:.2f}秒'.format(time_cost))


if __name__ == '__main__':
    root = Tk()
    root.title('亚马逊BesterSellers页面标题卖点')
    root.geometry('500x150')
    l1 = Label(root, text="输入产品BestSellers的页面网址")
    l1.pack()
    xlsbox = Text(root, width=50, height=5)
    xlsbox.pack()
    my_lock = Lock()
    pro_info = []
    # pro_info = [['#1', 'pro's link', 'pro's fetures' ], ...]
    count = 0
    btn = Button(root, text="下载Excel", relief=RAISED, command=main)
    btn.pack()
    xlsbox.bind('<Return>', main2)
    root.mainloop()





