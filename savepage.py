import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import fileinput

driver = webdriver.Chrome()
url = 'http://www.4geeks.de/cgi-bin/webgen.py'

for i in range(10):   
    f = open("/Users/francescogobbi/Desktop/Progetto_Mila/Software_Security_Project/trashcode/trash_code_%s.py"%i, "w")
    url = 'http://www.4geeks.de/cgi-bin/webgen.py'
    #url = 'https://junkcode.gehaxelt.in/'
    driver.get(url)
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    pre = (soup.pre) #ottengo il testo dalla prima pagina
    
    '''url2 = 'https://www.pythonconverter.com'
    driver.get(url2)
    res2 = requests.get(url2)
    insert = driver.find_element_by_id("python2code")
    insert.send_keys(pre)
    click = driver.find_element_by_xpath("/html/body/div[2]/div[3]/form/button").click()
    

    html_page2 = res2.content
    soup2 = BeautifulSoup(html_page, 'html.parser')
    post = (soup2.html.body.div[2].div[2].textarea) #ottengo il testo dalla seconda pagina'''

    #target = f.readline() 
    #f.write(pre.get_text())
    '''num = 'if __name__ == "__main__":'
   
    file = fileinput.input("/Users/francescogobbi/Desktop/Progetto_Mila/Software_Security_Project/trashcode/trash_code_%s.py"%i, inplace=True)

    for line in file:
        if num == line:
            for _ in range(100): # skip this line and next 4 lines
                next(file, None)
        else:
            print (line)'''
    text = pre.get_text()
    head, sep, tail = text.partition('if __name__ == "__main__":')
    f = open("/Users/francescogobbi/Desktop/Progetto_Mila/Software_Security_Project/trashcode/trash_code_%s.py"%i, "w")
    f.write(head)        
    f.close()
    driver.refresh()
driver.quit() 