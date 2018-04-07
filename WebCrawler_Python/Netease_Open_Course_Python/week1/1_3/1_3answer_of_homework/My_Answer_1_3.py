from bs4 import BeautifulSoup
import requests
import time

def get_gender(class_):
    if class_ == "member_girl_ico":
        return female
    else:
        return male

test_url = "http://bj.xiaozhu.com/fangzi/3781218930.html"

def get_singlepage(url, data=None):
    wb_data = requests.get(url)

#    time.sleep(2)

    soup = BeautifulSoup(wb_data.text, 'lxml')
    
    titles = soup.select("body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > h4 > em")
    addresses = soup.select("body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p > span")

    print(titles, addresses)#, sep='\n=====\n')
    if data == None:
        for title, address in zip(titles, addresses):
            data = {
                "title": title.get_text(),
                "address": address.get_text()
            }
            print (data)


get_singlepage(test_url)





