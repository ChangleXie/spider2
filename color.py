from xlrd import open_workbook
from xlsxwriter import Workbook
from os.path import exists



res = ['bracket', 'shelf', 'wall', 'screw']


# 高频词上色
def format_words(book, ws, i, j, sequences, fw):
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
        if word.lower() == fw[0][0]:
            format_pairs.extend((red, str(word+' ')))
            count += 1
        elif word.lower() == fw[1][0]:
            format_pairs.extend((green, str(word+' ')))
            count += 1
        elif word.lower() == fw[2][0]:
            format_pairs.extend((orange, str(word+' ')))
            count += 1
        elif word.lower() == fw[3][0]:
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
                # ws.write(j, i+7, str(sheet2.col_values(i, j, j + 1)[0]), format)
            # 卖点和标题
            else:
                format_words(book, ws, j, i+7, str(sheet2.col_values(i, j, j + 1)[0]), res)

    ws.merge_range(0, 9, 0, 10, 'Title', format)
    for i in range(0, ncol-4, 2):
        ws.merge_range(0, i+11, 0, i+12, 'Feature_%d' % int(i/2+1), format)

    # 表格行高
    for i in range(sheet2.nrows - 1):
        ws.set_row(i + 1, 100)
    # 表格列宽
    ws.set_column(0, 0, 5)
    ws.set_column(1, 1, 10)
    ws.set_column(9, ncol + 6, 18)
    # 插入词频
    for i in range(100):
        ws.write(0, ncol+7, 'words', format)
        ws.write(0, ncol+8, 'frequency', format)
        # ws.write(i + 1, ncol+7, str(res[i][0]), format)
        # ws.write(i + 1, ncol+8, int(res[i][1]), format)
    # 图片列
    for i in range(7):
        ws.write(0, i + 2, 'pic_%s' % str(i + 1), format)
    for i in range(100):
        for j in range(7):
            if not exists(file_name + '/rank#%d_%d.jpg' % (i+1, j+1)):
                continue
            ws.insert_image(i+1, j+2, file_name + '/rank#%d_%d.jpg' % (i+1, j+1), {'x_scale': 0.2, 'y_scale': 0.2,
                                                                                   'x_offset': 10, 'y_offset': 10})
    # 图片列边框、宽度
    cell_format = book.add_format({'border': 1})
    ws.set_column(2, 8, 18, cell_format)

    book.close()
