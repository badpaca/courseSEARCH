# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 14:54:42 2015

@author: badpaca
"""
from bs4 import BeautifulSoup
import requests
import time
import smtplib
while True:        
    urlclass = "courses.students.ubc.ca/..." # UBC course url of interest
    r  = requests.get("http://" +urlclass)
    data = r.text
    soup = BeautifulSoup(data)
    tables = soup.findChildren('table')
    my_table = tables[3]
    rows = my_table.findChildren(['tr'])
    my_row = rows[3]
    cells = my_row.findChildren('td')
    my_cell = cells[1]
    value = my_cell.string
    value = int(value)
    if value > 0:
        fromaddr = 'john.doe@gmail.com'      # these two lines are for
        toaddrs  = 'john.doe@gmail.com'      # sending yourself the email
		
        msg = " ".join(('A seat has opened up in class X!', str(value)))
        username = 'john.doe@gmail.com'      # the email address username

        password = '123abc'                  # the email address password
        server = smtplib.SMTP('smtp.live.com:587')
        server.starttls()
        server.login(username,password)
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()
        break
    else:
        print("not yet!")
    time.sleep(1)                            # refresh every second