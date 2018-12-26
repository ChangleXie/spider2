#coding = utf-8
from tkinter import *
from tkinter import StringVar
import time
import re
import requests
from bs4 import BeautifulSoup
import random
from another_crawl import getfeatures, urlread, change_page_num

# a = 'session-id=134-3856831-6537631; session-id-time=2082787201l; ubid-main=130-1157931-8753215; s_fid=4FD2C3C011299EE8-021F9EAFC572E127; s_dslv_s=First%20Visit; s_vn=1572424924025%26vn%3D1; s_invisit=true; regStatus=pre-register; s_cc=true; aws-priv=eyJ2IjoxLCJzdCI6MX0=; s_depth=3; s_dslv=1540889004876; s_nr=1540889004877-New; a-ogbcbff=1; session-token="XT04m2XC5juHX3i+mD5nd1zVynI8BBpKDb2uPsWRE+8UDWUdUiXr/nsQ83416x9vEKAM8kFqdSfI+adjwQOEzJVxi7PqYJza50ac90mWk9PioGVgm9cBUYyw/nHpQq6RR4N7EnJzAJyJVPrVB2vMiQ8ky8qZG2xTzHMU1qMbjNXWylJseSVFIthckiR9U2iABztN1qw5EQtAhm7R8HpEyrRYq0l7sa1HYSM9sq3yOeo="; x-main="PoWZ3rCn6D9ji?xtgsYr8uztxg9JB6dks4iF3zSRFJjawUDjZR7eFCVj6MP0@m9q"; at-main=Atza|IwEBII5BxWpps3ravM52GNR7oLZ6VewyY4hxMykt_m94zkGp_6Wf-XPVd1DOX0ioAMGyBqPncEceKRc_9kzSZ1vdDQc5cX2juiW4rUWKnRO-U1COjGl3iqIR8Yf1JLZwnYLgjkX--FOUDEeZXtTbyHvsmNsLS0Lc8BboA7Tp8AFRVZTvgWm2EB186NJKm8wJXNgsOuj94NkFp9UbuBPlY7cfaH6iQg8W1yfjp4XTB8p_SYE1yXDr_bFbEUorcEMRgoGHz2KeBr1LIKyEEyXYgaROUBbpiAywijGPo1WA6j1S-3JAwN6oOqE96ag1dxLhqwRyaqOijDZoGJxWL6gV3bLrqCMcGHWgofOKFynd6kyfFlBIIMFDi3KROqq1y9SgnR1wbg_em19l8_DRHzXGHKccaIIk; sess-at-main="YSLtfGHW3yvMfEy/nQpu9Edyj4aXcjDnbjsfl2TT5xA="; sst-main=Sst1|PQFT0zg0UbdXrmR0ohnZgoejC-Dpn37khTJS4YoeexmrA6z1zkSSwaXBmgtWznvt8YdqG4wjh6z-zXF8r3hO6HABT6YB6W2ELV-OppbqrW1abrJNneG38MS-1G1gKvkmT-VA4e_Lx5aHxQiWkMu5WatDLZVWUhUBCcaHvHeMT8j_LddjHXZskmN9gDamMMCA9WvOJbQMl4dTZlqdRXOGNUypEiziOfSlRLe8Ojn2H9LCqNLektine0nLTIbaPJcNCHq1IEo2cc3Sx4vYLvfUnPTPij6Itghi7DxnHhDUEY9G8oPto0tKTHOQJpbXhHfihCpHc1_7KIev1Dce5MdtmREZJQ; lc-main=en_US; x-wl-uid=1gcAWcUxqoUoSCND3zabY7xQtrE1c8wWhsrfn8NwTyvWPgpjEnWfI/VBLzn0pwcamFEXs9CmGDUywbOllXHI6Aav2VQB1lVCorL+J6q0zW8vv6yhnP5wfoaQhhca7pZQTsFnftvRfpEw='
#
# print(a)
# a = a.replace(' ', '').replace('=', '\': \'').replace(';', '\', \n\'')
# print('\''+a+'\'')
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36\
#                              (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
#
# def get_ip_list():
#     print("正在获取代理列表...")
#     url = 'http://www.xicidaili.com/nn/'
#     html = requests.get(url=url, headers=headers).text
#     soup = BeautifulSoup(html, 'lxml')
#     ips = soup.find(id='ip_list').find_all('tr')
#     ip_list = []
#     for i in range(1, len(ips)):
#         ip_info = ips[i]
#         tds = ip_info.find_all('td')
#         ip_list.append(tds[1].text + ':' + tds[2].text)
#     print("代理列表抓取成功.")
#     return ip_list
#
#
# def get_random_ip(ip_list):
#     print("正在设置随机代理...")
#     proxy_list = []
#     for ip in ip_list:
#         proxy_list.append('http://' + ip)
#     proxy_ip = random.choice(proxy_list)
#     proxies = {'http': proxy_ip}
#     print("代理设置成功.")
#     return proxies
#
#
#
# print(get_random_ip(get_ip_list()))
#
# url = 'https://www.amazon.com/Plastic-Waterproof-Kennel-Outdoor-Favorite/dp/B07JKMM7Q7/ref=sr_1_11?m=A2WLZYMRRZX3ZZ&s=merchant-items&ie=UTF8&qid=1540794787&sr=1-11&th=1'
# print(getfeatures(url))
# a = 'SKJDHKAJSDH'
# a.lower()
# print(a[:-3])
url = 'https://www.amazon.co.uk/Best-Sellers-Pet-Supplies-Dog-Car-Seat-Covers/zgbs/pet-supplies/13154116031/ref=zg_bs_pg_2?_encoding=UTF8&pg=2'
url_2 = 'https://www.amazon.com/Best-Sellers-Home-Improvement-Bathroom-Hardware-Installation/zgbs/hi/6809823011/ref=zg_bs_pg_1?_encoding=UTF8&pg=1'
url_1 = change_page_num(url)
print(urlread(url).find(class_='zg_selected'))