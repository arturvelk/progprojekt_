import gspread
import pandas as pd
from aocd.models import Puzzle as pz
import aocd
import yagmail
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import requests
import browser_cookie3
import re
import os
from contextlib import contextmanager
from oauth2client.service_account import ServiceAccountCredentials


#getting the aoc_data spreadsheet.
def get_spreadsheet_instance(json_name):
    # define the scope
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    # add credentials to the account
    creds = ServiceAccountCredentials.from_json_keyfile_name(json_name, scope)

    # authorize the clientsheet 
    client = gspread.authorize(creds)
    # get the instance of the Spreadsheet
    sheet = client.open('aoc_data')

    # get the first sheet of the Spreadsheet
    sheet_instance = sheet.get_worksheet(0)


    return sheet_instance
def get_df(sheet_instance):
    df = sheet_instance.get_all_records()
    df = pd.DataFrame.from_dict(df)
    return df

def update_spreadsheet(df,instance_name):
    update_values = [df.columns.values.tolist()] + df.values.tolist()
    instance_name.update(update_values)
    
#dictbe szedi hogy melyik napra hány csillagod van.
def csillagok(year):
    name = []
    for _ in range(25):
        name.append(0)
    parts = ["a","b"]
    for i in range(25):
        print(i) #lassu, valahogy gyorsitani.
        puzzle = pz(year = year, day = i+1)
        for x in parts:
            try:
                puzzle._get_answer(x)
            except Exception:
                 pass
            else:
                if name[i] == 1:
                    name[i]+= 1
                else:
                    name[i] = 1
    return name
def send_email_update(user, app_password, receiver, pdf):
    
    subject = 'AOC csillagok, 2020'
    content = ['Sziasztok! Itt láthatjátok a csillagok mostani állását, nem akartam zavarni a többieket a dolgozásban, ezért csak Andort, jómagamat és Sebit látjátok jelenleg, határidő után majd belerakok mindenkit! Köszi és hali! Artúr',pdf]

    with yagmail.SMTP(user, app_password) as yag:
        yag.send(receiver, subject, content)
        print('Sent email successfully')
def to_pdf(df):
    #https://stackoverflow.com/questions/32137396/how-do-i-plot-only-a-table-in-matplotlib
    fig, ax =plt.subplots(figsize=(12,4))
    ax.axis('tight')
    ax.axis('off')
    the_table = ax.table(cellText=df.values,colLabels=df.columns,loc='center')

    #https://stackoverflow.com/questions/4042192/reduce-left-and-right-margins-in-matplotlib-plot
    pp = PdfPages("current_standing.pdf")
    pp.savefig(fig, bbox_inches='tight')
    pp.close()
    
def get_session(browser):
    if browser == "chrome":
        cookies = list(browser_cookie3.chrome())
    elif browser == "firefox":
        cookies = list(browser_cookie3.firefox())
    elif browser == "opera":
        cookies = list(browser_cookie3.opera())
    elif browser == "edge":
        cookies = list(browser_cookie3.edge())
    elif browser == "chromium":
        cookies = list(browser_cookie3.chromium())
    else:
        return print("kérlek, stringként, kisbetűvel írd a böngésződ nevét, köszi")
        
    
    cookie_dict = {}
    for i in cookies:
        if "adventofcode.com" in i.domain:
            cookie_dict[i.name] = i.value
    return cookie_dict["session"]
    
    
def set_session(session_id):
    os.environ["AOC_SESSION"] = session_id
    return print("sikerült")

@contextmanager
def idomegmondo():
    startTime = time.time()
    yield
    elapsedTime = time.time() - startTime
    print('A függvény {} ms-be telt hogy lefusson'.format(int(elapsedTime *1000)))