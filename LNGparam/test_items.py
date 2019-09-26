# -*- coding: utf-8 -*-

import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

# !!!5. Название тестового метода внутри файла test_items.py соответствует задаче
def test_set_language_to_page(browser):
    
    # время ожидания реакции до 10 тиков
    browser.implicitly_wait(10)
    browser.get(link)
    
    # просто пауза ))
    time.sleep(30) 
    
    # !!!4. В тесте проверяется наличие кнопки добавления в корзину
    # размер массива кнопок с нужным селектором : типа 1 > 0
    assert len(browser.find_elements_by_xpath("//*[@id='add_to_basket_form']/button")) > 0, "\n!!!Button NOT found!!!"
    


