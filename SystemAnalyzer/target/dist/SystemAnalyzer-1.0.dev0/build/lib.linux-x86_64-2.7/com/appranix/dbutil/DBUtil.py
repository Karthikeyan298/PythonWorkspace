'''
Created on 03-Nov-2017

@author: karthikeyan
'''
import pymysql

class DBUtil(object):
    
#database connection
    def __init__(self):
        pass
        
    def create_connection(self):
        return pymysql.connect(host="localhost", user="root", passwd="root", database="system_analyzer")      