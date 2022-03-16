import pymysql.cursors
import pandas as pd
import json

from flask import Flask, jsonify
from sqlalchemy import create_engine

class db_connect:
    def select(self, sql):
        f_conn = pymysql.connect(host='localhost', user='USERNAME', password='PASSWORD', charset='utf8', autocommit=True, cursorclass=pymysql.cursors.DictCursor)
        f_curs = f_conn.cursor()
        f_curs.execute(sql)
        f_conn.close()
        rows = f_curs.fetchall()
        df = pd.DataFrame(rows)

        return df

