import os
import time
import xlrd
from selenium import webdriver

def read(a):
    data = xlrd.open_workbook(a)#打开excel文件
    table = data.sheets()[0]#读取第一个sheet的数据
    code = table.col_values(0)#以列表形式存储第一列数据
    name = table.col_values(1)#以列表形式存储第二列数据
    classname = table.col_values(2)
    return code,name,classname

def test(code,name,classname):
    #driver = webdriver.Chrome("chromedriver.exe")  # chromedriver所在路径
    driver.get(r"https://jinshuju.net/f/SsQcjx")
    
    driver.find_element_by_css_selector("input[class='ant-input sc-fzpans jciKRM text-field field field_2']").send_keys(name)
    driver.find_element_by_css_selector("input[class='ant-input sc-fzpans jciKRM text-field field field_3']").send_keys(code)
    driver.find_element_by_css_selector("input[class='ant-input sc-fzpans jciKRM text-field field field_4']").send_keys(classname)
    driver.find_element_by_css_selector("div[class='pretty-select__value-container css-55y0h0']").click()
    driver.find_element_by_css_selector("div[id='react-select-2-option-2']").click()
    driver.find_element_by_css_selector("button[class='ant-btn sc-AxhUy elBAbT published-form__submit form-theme--submit-button ant-btn-primary']").click()
    time.sleep(0.5)
#if __name__ == "__main__":
#    test()
#    os.system("pause")
if __name__ == "__main__":
    code,name,classname=read('171.xls')#加载花名册

    driver = webdriver.Chrome("chromedriver.exe")  # chromedriver所在路径

    for i in range(35):
        test(str(int(code[i])),name[i],classname[i])

    os.system("pause")
    
