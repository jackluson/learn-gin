# -*- coding: UTF-8 -*-

# !/usr/bin/python3
# 作者公众号：价值投机牛亦飞
import json
import requests
import xlwt
from datetime import *
import time
from bs4 import BeautifulSoup

# 牛散名单
niusan = {'钟宝申': '牛散', '郑志坤': '牛散', '郑淑芬': '牛散', '张鹏': '牛散', '莫浩礼': '牛散', '黄永山': '牛散',
          '何燕': '牛散', '高建华': '牛散', '冯民': '牛散', '冯玲': '牛散', '翟建琴': '牛散', '丁碧霞': '牛散',
          '李怡名': '牛散', '陈晓红': '牛散', '曹卫宏': '牛散', '蔡子跃': '牛散', '蔡晓东': '牛散', '梁小红': '牛散',
          '李志鹤': '牛散', '黄巍然': '摊大饼', '陈娟': '摊大饼',
          '林园': '私募', '睿郡': '私募', '盘京': '私募', '宁泉': '私募', '明汯': '私募', '兴聚': '私募',
          '通怡': '私募', '安鑫': '私募', '纽达': '私募', '平石': '私募', '盖德尔': '私募', '迎水': '私募',
          '九坤': '私募', '旌安': '私募', '君信和': '私募', '展弘': '私募', '久期': '私募', '合晟': '私募',
          '高熵': '私募'}

# 集思录列表数据
list_url = 'https://www.jisilu.cn/webapi/cb/list/'

# 需填入集思录登录cookie 可以在浏览器中获取
jsl_headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,pt;q=0.7,zh-TW;q=0.6',
    'Columns': '1,70,2,3,5,6,11,12,14,15,16,29,30,32,34,35,75,44,46,47,52,53,54,56,57,58,59,60,62,63,67',
    'Connection': 'keep-alive',
    'Cookie': '',
    'If-Modified-Since': 'Wed, 29 Jun 2022 10:13:04 GMT',
    'Init': '1',
    'Referer': 'https://www.jisilu.cn/web/data/cb/list',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"'
}

# 同花顺f10基本资料
ths_index_url = "http://basic.10jqka.com.cn/%s/%s/index.html"
# 同花顺f10债券详细
ths_detail_url = "http://basic.10jqka.com.cn/%s/%s/detail.html"

ths_headers = {
    'Host': 'basic.10jqka.com.cn',
    'Upgrade-Insecure-Requests': '1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko)',
    'Accept-Language': 'zh-cn'
}


def ths_headers_with_cookie():
    return {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,pt;q=0.7,zh-TW;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': '__bid_n=183ba96fe42c3f82e44207; FEID=v10-1eebcea39886b8db33b2c67e20c985693c313e66; __xaf_fpstarttimer__=1672040247475; __xaf_thstime__=1672040247660; __xaf_fptokentimer__=1672040247764; searchGuide=sg; BAIDU_SSP_lcr=https://www.baidu.com/link?url=gy66fehjqf5E1TBjyUnMBP2MMJppbmUSPaDUhWMZ1Dh6M6gp-cPYH0NOVreHsaoC&wd=&eqid=e0d48456001656090000000263c38a62; FPTOKEN=SPfEU6LsmHtpSpi70KZ+SxQ3iSu56rZaQ7L4IpnQIdJVHiR10n+JX3m5d7tY8AzpGAVly+9VdEUfhjKKsnJgfBYFm49D039+LW6Lwz5VxZ1YIo43t8MglD/78ugDQwA0yyqbhvPGXn9e8krZXIY8SDvFh0Gz/9Idldo9M1ZHsr/3Ndt2clDOHANZVqNSZWr2KoyNCBFfFnmBkppl276OwMmt4CflKpKJYHLmRUJ9k4CzG8ivw/WApHQ8etvR7bd/NvP1lQzicqCqrcBQRUHMI1CMxUQfDVmyGyji+n4XVq6W6OIb8FzOe+w/hOp+87WC3PBvrKOeTvrPjlE39vvhHOCEpgv77IoWOgHBVdLggzPzjzXo7ITC3lowX+OaokGWuPMZQ/CXHub6Wbw+NYOgzA==|04kWDFOnxrfrTIBhx17eFzAOZpOyERqM48ui8RT41G4=|10|c3c72fe21fd5b6b9a924acd67067e276; __utma=156575163.1422871151.1663752822.1663752822.1673759342.2; __utmc=156575163; __utmz=156575163.1673759342.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1672712372,1673338870; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1675160025; v=A8uZVqyDLGSLxHCw722O675vXGSwYN_iWXSjlj3Ip4phXOUaxTBvMmlEM-dO',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }


# 同花顺网页抓取
def get_ths_html_content(page, market, code):
    if market.upper() == 'SZ':
        market = '32'
    else:
        market = '16'
    if page == 'index':
        url = ths_index_url % (market, code)
    else:
        url = ths_detail_url % (market, code)
    # 重试3次
    for i in range(3):
        try:
            response = requests.get(url=url, headers=ths_headers_with_cookie(), verify=False)
            response.encoding = 'gbk'
            html = response.text
            return html
        except Exception as e:
            time.sleep(1)


# 字符串转化为数字
def to_number(s):
    try:
        n = float(s)
        return n
    except ValueError:
        pass
    return s


# 解析同花顺十大持有人信息
def get_ths_holder_info(market, code):
    html = get_ths_html_content('detail', market, code)
    # print(html)
    soup = BeautifulSoup(html, "html.parser")
    if not soup.select('div.m_tab_content2.clearfix'):
        return 0
    t_date = soup.select('div.m_tab_content2.clearfix')[0].get('id')[2:]
    # 上期数据
    last_dict = {}
    if len(soup.select('div.m_tab_content2.clearfix')) > 1:
        rows_last = soup.select('div.m_tab_content2.clearfix')[1].select('table > tbody > tr')
        # 上期持仓数量
        for row in rows_last:
            last_dict[row.select('td')[0].text] = to_number(row.select('td')[2].text)
    # 最新一期数据
    rows_latest = soup.select('div.m_tab_content2.clearfix')[0].select('table > tbody > tr')
    holder_info_list = []
    for row in rows_latest:
        holder_info = []
        for i in range(0, 4):
            holder_info.append(to_number(row.select('td')[i].text))
        holder_info.append(t_date)
        # 是否为新增前十大持有者
        if holder_info[0] not in last_dict:
            holder_info.append('是')
            holder_info.append(holder_info[2])
        else:
            holder_info.append('')
            holder_info.append(holder_info[2] - last_dict[holder_info[0]])
        holder_info_list.append(holder_info)
    return holder_info_list


# 抓取列表数据
def get_list_data():
    response = requests.get(url=list_url, headers=jsl_headers, data={})
    response.encoding = 'utf-8'
    return json.loads(response.text)


# 解析可转债数据
def parse_cb_data(data):
    cb_result = []
    result_list = data['data']
    for result in result_list:
        # 排除可交换债
        if result['btype'] == 'E':
            continue
        # 排除待上市
        if result['price_tips'] == '待上市':
            continue
        # 排除强赎
        if result['redeem_dt']:
            continue
        holder_list = get_ths_holder_info(result['market_cd'][:-2], result['bond_id'])
        print("holder_list", holder_list)
        # 转债代码 转债名称 持有人名称 持有人标识 是否牛散 持有数量(万张) 持有比例 更新日期
        for holder_info in holder_list:
            niusan_type = ""
            if holder_info[0] in niusan.keys():
                niusan_type = niusan.get(holder_info[0])
            else:
                for name in niusan.keys():
                    if name in holder_info[0]:
                        niusan_type = niusan.get(name)
            detail = [result['bond_id'], result['bond_nm'], holder_info[0], holder_info[1], niusan_type, holder_info[2],
                      holder_info[5], holder_info[6], holder_info[3], holder_info[4]]
            cb_result.append(detail)
        time.sleep(1)
    return cb_result


# 数据写入excel
def write_excel(path):
    list_data = get_list_data()
    # print("list_data", list_data)
    workbook = xlwt.Workbook(encoding='utf8')
    cb_sheet = workbook.add_sheet('可转债详情')
    title = ['转债代码', '转债名称', '持有人名称', '持有人标识', '是否牛散', '持有数量(万张)', '是否新增',
             '持有变化(万张)', '持有比例%', '更新日期']
    for i in range(0, len(title)):
        cb_sheet.write(0, i, title[i])
    row = 1
    cb_result = parse_cb_data(list_data)
    for detail in cb_result:
        for i in range(0, len(detail)):
            cb_sheet.write(row, i, detail[i])
        row = row + 1
    workbook.save(path)


if __name__ == '__main__':
    write_excel('./holder.xls')
