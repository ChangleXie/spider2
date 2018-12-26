from bs4 import BeautifulSoup
import requests




def get_price(url):
    Cookie = { 'lc - main' : 'en_US',
    '_ga' : 'GA1.2.756134632.1531984968',
    'skin' : 'noskin',
    's_vnum' : '1966818137631%26vn%3D1',
    's_sq' : '%5B%5BB%5D%5D',
    's_nr' : '1534818157195 - New',
    's_dslv' : '1534818157196',
    'session-id-eu' : '258-4463840-9142617',
    'session-id-time-eu' : '2166172330l',
    'ubid-acbuk' : '257-1491900-8219228',
    'at-main' : 'Atza|IwEBIFV5P-sIm76hFwOylP0chh70uKyT85j55Vz7dxDKQ9D17v9CZJ4mfydAeAIHxfIvsEdfcvTd-Y2vQp9osHeiT0-yeY1WaiEQUrgKEK1REtuAZG7ojk9YGjqpG1l7mwRdEWpVYfbHjstOYb - Q0NvCzZKHAv9vu - x6U1ttTTOodD3SSkG5uGqrccZBZmjPcsUMIZprLtalNCDzaqp3bEJWzzs7g1VUqjkSNp2RTiEfQ99jIMLMTQD0kyHzEKes79PtLkPa0fI6tgsJSaIcUgP1dKVYcAKwhiloAfHbtTX9DJa1LMYoMxEs1Wqqxf76WIeOK-NmmfHNztCLVpADZpaR4IE95JprxEs9jtEOdziTpuCZzHAGXFuuYxNx2_bO9XqsSCQVl7jQx9oLZdh5X7DL9uuu',
    'sess-at-main' : '2+VbkU2crE/GD8uR2Q452ypk1LJ8J8d3ctlFlK2BuS0=',
    'sst-main' : 'Sst1|PQH04JbkHWVGywVZDC1l1F3IC5bKyYMsW6AUuDhEZ8p0eIzuHvyy0gkChaoKGBA4z1OufCyRcM4-vjpVmb4IT6lXcP6b1t_jKTa2cbMJMeHJNVruiC_kzgwYoVP_fR-5xB6qkp9LnKYJpctTYui5rIAEvRwPABLh6ymsqlUuoW - iQ6S9YhW0_ - w6iiYT8n4YeaHRaBtkLXdP2hcI1HJqb8NR7K9TV0axBCUuZV3yZ1vy6F0XtyGuekcSVqoFz9QLGbzMGUcsLesruLM5YTSG - CzK1Im60VhGhKGccokNHFooJzcivwFAOIiyJtXMkYjYuCqPQKcjyln6jOTnB8OXedSstw',
    's_pers' : '%20s_fid%3D2FC5ADE05BDB7F64-15749A3B11AC9F26%7C1695189768397%3B%20s_dl%3D1%7C1537425168398%3B%20gpv_page%3DUS%253AAS%253AFBA-pricing%7C1537425168402%3B%20s_ev15%3D%255B%255B%2527ASUSFBADirect%2527%252C%25271537423368404%2527%255D%255D%7C1695189768404%3B',
    's_sess' : '%20s_sq%3D%3B%20ev1%3Dn%2Fa%3B%20s_cc%3Dtrue%3B%20s_ppvl%3DUS%25253AAS%25253AFBA-pricing%252C48%252C31%252C1681%252C1920%252C981%252C1920%252C1080%252C1%252CL%3B%20c_m%3DTyped%252FBookmarkedTyped%252FBookmarkedundefined%3B%20s_ppv%3DUS%25253AAS%25253AFBA-pricing%252C100%252C31%252C3816%252C1920%252C981%252C1920%252C1080%252C1%252CL%3B',
    'session - id - time' : '2082787201l',
    'x - main' : 'hx1bxR66?KB2XXxetFp29keH6JeX876wFqRpIJa0MqHTaEJ?sMqmbcebyTxS8XvN',
    'ubid - main' : '131-0928638-4831508',
    'session - id' : '144-1823531-9706327',
    'x - wl - uid' : '1Jh6JJEsFMgpZqrMPOiAIp7q+6i6CK5/+AIbyvZl+IdBj9kG4uBlzUFPCqc/uzrrKBkEmsiTLwlhYZSOeJL9m4fAY2hn4y8IV4vnd/aCxoFlx024wecoFhk52fk0Vu3BzFkYgBoYf3ZM=',
    'session - token' : '"3cJO0LXxF2W2D58hiXH7sl1D6BgCQ32Y4SALivT2zPz1EyUndo4UwuT1TCiFfCVtDJBYvOkPPR/tZCVA3IH724jA2LSi0UuQdT6xD0ucfqHSU+V791P3zebGlbIJVyfMe1qMauheg0my90/zvqgRFJJxpbTvkMzng4LS55pGgovyIvkweZliNiepi7uLLpIp8Z0Qu0PbTgYLbQTD29PcgTagoTAwzXteZY3WOvx3UeLglm5ZADAJ3QjW6lip/v1DTw/mB8rp/exv2MlQlyb7WQ=="',
    }
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    html1 = requests.get(url, headers=headers, cookies=Cookie).text
    soup1 = BeautifulSoup(html1, 'lxml')
    try:
        price = soup1.find(id='priceblock_ourprice')
        dollar = price.string
    # print(dollar)
        return dollar
    except:
        return 0
url = 'https://www.amazon.com/Control-Organizer-Compartments-Multiuse-Supplies/dp/B07DCPP18F/ref=sr_1_3?m=A2WLZYMRRZX3ZZ&s=merchant-items&ie=UTF8&qid=1542770494&sr=1-3'
print(get_price(url))