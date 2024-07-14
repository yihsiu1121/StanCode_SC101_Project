"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10905209
Female Number: 7949058
---------------------------
2000s
Male Number: 12979118
Female Number: 9210073
---------------------------
1990s
Male Number: 14146775
Female Number: 10644698
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #

        # 找到包含數據的表格
        table = soup.find('table', {'class': 't-stripe'})

        male_total = 0
        female_total = 0

        # 遍歷表格行並累加數字
        for row in table.find_all('tr')[1:]:  # 跳過標題行-->第1行為標題行，table.find_all('tr') 會返回包含所有 <tr> 元素的列表
            cols = row.find_all('td')  # 找到行中的所有單元格的資料，並回傳成一個list
            if len(cols) == 5:  # 檢查行是否包含5個單元格，以確保資料是對的

                # .text 屬性會提取單元格中內容，EX:  <td>12,345</td>，那麼 cols[2].text 就會返回字符串 '12,345'
                # .replace(',', ''))-->將string轉換成整數前要移除逗號
                male_total += int(cols[2].text.replace(',', ''))
                female_total += int(cols[4].text.replace(',', ''))

        print(f'Male Number: {male_total}')
        print(f'Female Number: {female_total}')


if __name__ == '__main__':
    main()
