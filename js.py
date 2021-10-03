#!/usr/bin/env python

import pandas as pd
from datetime import datetime as dt
from calendar import month_abbr

URL='http://jadwalsholat.pkpu.or.id/'

def show_html(url):
    try:
        df = pd.read_html(url)
        df = df[0]
        header = df.iloc[1]
        df = df[2:-5]
        df.columns = header
        df = df.set_index('Tanggal')
        day=dt.now().day
        day=f'0{day}' if day<10 else f'{day}'
        print()
        print(f'jadwal sholat {day}-{month_abbr[dt.now().month]}-{dt.now().year}')
        print()
        print(df.T[[day]])
        print()
    except Exception as e:
        print(f'there is no internet connection or server {URL} is down')
        print(f'\n{e}\n')


if __name__=='__main__':
    show_html(URL)

