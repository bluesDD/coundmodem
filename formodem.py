# -*- coding: utf-8 -*-

import re           #正規表現モジュールre
import datetime     #
import csv          #csvモジュール


#日付の抽出と、各ファイル名の変数化
today1= datetime.date.today()
today2= "{0:%Y%m%d}".format(today1)
logfile_name_log = today2 + "_howmany.log"
logfile_name_csv = today2 + "_howmany.csv"

#ログファイルとCSVファイルを開く
fr = open(logfile_name_log)
fw = open(logfile_name_csv, 'w')
line = fr.readline()

#fline = line.split(",")

while line:
    
    fw.write(line)
    line = fr.readline()

"""
while line:
    fline = re.findall(r'\\b[1,4]', line)
    fw.write(fline)
    line = fr.readline()
"""

#開いた両ファイルを閉じる
fr.close()
fw.close()
