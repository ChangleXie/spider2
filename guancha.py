# -*-coding:utf-8-*-

from requests import Request, Session
from bs4 import  BeautifulSoup

def urlread(url):
    cookie = {'s_fid': '4FD2C3C011299EE8-021F9EAFC572E127',
              'regStatus': 'pre-register',
              's_cc': 'true',
              'aws-priv': 'eyJ2IjoxLCJzdCI6MX0=',
              'lc-main': 'en_US',
              's_sq': '%5B%5BB%5D%5D',
              's_ppv': '73',
              's_vnum': '1972898082437%26vn%3D2',
              'x-wl-uid': '1pWFR9aKNcr5mZ24tGsSCxkZ0trFWtsl24HtaScf38xBT7YQuLo4U6+ykE9eH9cpBIXiILSL1wl38Bg4BPlPm6xt2htYw3WedPj1csKfNbHTucv7x7xh+JPVZ4JZDCj0aV7gWfjBbvSM=',
              'appstore-devportal-locale': 'zh_CN',
              'AMCVS_4A8581745834114C0A495E2B%40AdobeOrg': '1',
              '_mkto_trk': 'id:365-EFI-026&token:_mch-amazon.com-1540974668299-31178',
              'AMCV_4A8581745834114C0A495E2B%40AdobeOrg': '-330454231%7CMCIDTS%7C17836%7CMCMID%7C25155120772369371358210843232415684168%7CMCOPTOUT-1540981868s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C3.1.2',
              's_lv': '1540974671016',
              'skin': 'noskin',
              's_vn': '1572424924025%26vn%3D2',
              'c_m': 'undefinedwww.google.comSearch%20Engine',
              's_dslv': '1541406758240',
              's_nr': '1541406758252-Repeat',
              'at-main': 'Atza|IwEBIGDfPjZo5hDFBQpJN9pelu1nxcxRxXlFDdkPbZJNaujrAcSHXWRyXnetIJD8-Xc0RjufK60VdzWR76e52XZF2l2K5biZ14LZ5x-WR8Z7zW0UIZD9cENkvSe93N-T3jqBI6MLLM_OEzkaBZgvqmFmYIqVwE50JFYXAaN1JOy9ZO1E5TA274nFQhPdCgkxeVq-v4wuJNK_b0xy4q2LtW3Iz7PnDFLFklclRqUgiTsmHiNe_1REedFH6zQAw5GQCMqMOgqdaKV88ABAZuk_uuGjeZBvK5Qfa3u4sr1_acP7m2nPJN9-yocaqVZCZK0L2OjBQDmcMvCilgESIQw0l-EMgsn8FISToi6RY6q72W6FS60Og3ZG6asvIHsgJYb7vVh7DaDUddvXsd4UGzKfGB42h6oV',
              'sess-at-main': '"wgcyvBZjDCBuncoS/H9VjJhOy2O+nEBp4LkKLFs8ua0="',
              'sst-main': 'Sst1|PQFl-RHLfKFhBLGI63CHtnpQC96pev6fVPbp-FLBZ62Br7c6GMrNs28Q7JXZB7wjwgBrBwUu9rl1be8lwbCyWbhu0zfCRG6bB6-_bIYtr25IGljiKCF_6DrunZCtYtSDqvbfubXSgbydAgsZ6IM586uTGnjSldtkg4_ViqQNq5DLvBhqWFhfv8lTBAiAS32TM1OCm4YoIAu92DiMCPFepL4l7Q8n6WxHxgFHmRauK4piKioYvIGyu4LAkZ_yuiSUcjp2yarN8fL-8GcQiZiHYjdEKXC3QUzlKkdDjlUHSefH4BMK4ya3ap0b8VUpHO81wUO9G9KCL4MY8jtMzacV4Eb7mg',
              'session-id-time': '2082787201l',
              'session-id': '134-3856831-6537631',
              'ubid-main': '130-1157931-8753215',
              'x-main': '"EuOuJVulAQeMD5d2Wgsy3ZlyTtNdrIzyprfny9G4tz7iJ?bQgNvPDw@A6?SP0JKu"',
              'aws-ubid-main': '146-1514507-8114676',
              'session-token': 'NKmgOI8U1Ajuq7Vtd0UCSulWJmXTw531yceI+VK5qpF/a6aKJVHcsQQvp9xgCc10DCjtjmO6JXn7lt99FHImzcI23ZCJYA/5L+T7aYvLyz0OerJWk54haMumSNoSf4NDp4pdBCdYJ8Z5bC1o697s+V5EPcsT/zUbJ72E57F9o1Fg3DUj1bXbDkFytFtx/ta7Pr1v8y0awo7WZggcGgH6j2Yjcchftsh4ZWebr8BvBVSTFhm+zJiaQRDhnBhModykRDAAa9fNkrj5mc+KZGZjWQ==',
              }
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    s = Session()
    # url = 'http://' + url[8:]
    # proxy = {'http': 'http://222.76.204.110:808'}
    request = Request('GET', url, headers=headers, cookies=cookie)
    print(request.content)
    prepared_request = s.prepare_request(request)
    settings = s.merge_environment_settings(prepared_request.url, None, None, None, None)
    response = s.send(prepared_request, **settings).text
    soup = BeautifulSoup(response, 'lxml')
    # logging.info(soup)
    return soup

url = 'https://www.amazon.com/s?marketplaceID=ATVPDKIKX0DER&me=A2WLZYMRRZX3ZZ&merchant=A2WLZYMRRZX3ZZ&redirect=true'
urlread(url)