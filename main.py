import pandas as pd
from get_price import get_price
import time
import numpy as np
from threading import Thread, Lock, current_thread
from queue import Queue
from intocm import weight, fbafee, cal_size, calcu_profit
import xlsxwriter
import xlrd
import os
import re


def price_info(pro_info):
        price = get_price(pro_info)
        print('Getting \'s price: %s' % (price))
        return price


class Producer(Thread):
    global price_group

    def __init__(self):
        Thread.__init__(self)
        self.pages = pro_infos
        self.queue = Queue()

    def run(self):
        while self.pages:
            product = self.pages.pop(0)
            print(product)
            try:
                price_group.append((int(product[0]), price_info(product[1])))
            except AttributeError as e:
                # product = self.pages.pop(0)
                # print(product)
                # self.pages.append(product)
                print(e)


def main():
    threads = [Producer() for i in range(10)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    price_group.sort(key=lambda x: x[0])
    price_res = [i[1] for i in price_group]
    ncols = worksheet.ncols
    nrows = worksheet.nrows
    for i in range(ncols):
        for j in range(nrows):
            ws.write(j, i, str(worksheet.col_values(i, j, j+1)[0]))
    ws.write_column(1, 16, price_res)
    cost = worksheet.col_values(17, 1)
    print(type(cost))
    ps = worksheet.col_values(14, 1)
    w = worksheet.col_values(15, 1)
    sea = worksheet.col_values(21, 1)
    profit = []
    for i in range(len(price_res)):
        price_res[i] = str(price_res[i]).replace('$', '')
        size = cal_size(ps[i])
        wt = weight(w[i])
        freight = fbafee(size, wt)
        pf = calcu_profit(freight, str(cost[i]), str(price_res[i]))
        profit.append(pf[0]) if sea[i] == '√' else profit.append(pf[1])
    output = [int(i) for i in profit]
    for i in range(len(output)):
        ws.write(i+1, 18, '%.02f' % profit[i])
    for i in range(len(dict2)):
        try:
            ws.write(i+1, 10, '%d' % list(dict2.values())[i])
        except TypeError as e:
            print(dict2.values())
    wb.close()


if __name__ == '__main__':

    excel_path = 'pro_info_backup.xls'
    save_path = 'pro_info.xls'

    workbook = xlrd.open_workbook(excel_path)
    worksheet = workbook.sheet_by_index(0)

    wb = xlsxwriter.Workbook(save_path)
    ws = wb.add_worksheet('Pro_info')

    pro_links = worksheet.col_values(5, 1)
    pro_asins = worksheet.col_values(4, 1)
    pro_sku = worksheet.col_values(3, 1)
    pro_id =worksheet.col_values(0, 1)
    asins = [i for i in pro_asins if str(i).strip() != '']
    print(asins)
    links = [i for i in pro_links if i != '']
    print(len(asins))
    sku = [i for i in pro_sku][:len(asins)]
    print(sku)

    pro_infos = list(zip(pro_id, links))
    my_lock = Lock()
    price_group = []

    sales_path = r'Z:/8销控表+库存盘点/销控表/'
    file_names = os.listdir(sales_path)
    rep = r'\d{0,2}\.\d{0,2}英国.*?\.xlsx'
    for i in file_names:
        if re.match(rep, i):
            file_name = re.match(rep, i).group(0)
    file_path = sales_path + file_name

    print('opening sales excel')
    start_time = time.time()
    workbook2 = xlrd.open_workbook(file_path)
    worksheet2 = workbook2.sheet_by_index(1)
    ncols = worksheet2.ncols
    nrows = worksheet2.nrows
    print(time.time() - start_time)

    sku2 = worksheet2.col_values(4, 1, nrows - 2)
    sales = worksheet2.col_values(ncols - 4, 1, nrows - 2)

    dict = {}
    dict2 = {}
    for i in range(len(sku2)):
        dict[sku2[i]] = sales[i]
    for i in range(len(sku)):
        if sku[i] in dict:
            dict2[sku[i]] = dict[sku[i]]
        else:
            dict2[sku[i]] = 0
    main()



