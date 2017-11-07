'''
Created on 03-Nov-2017

@author: karthikeyan
'''
from com.appranix.dbutil.DBUtil import DBUtil

class ReportService(object):
    
    def __init__(self):
        dbutil = DBUtil()
        self.connection = dbutil.create_connection()
    
    def create_cpu_report(self, component, usage, time):
        cursor = self.connection.cursor()
        insert_query = "INSERT INTO cpu_report VALUES('"+ component +"', "+ str(usage) +" , '"+ time +"')"
        cursor.execute(insert_query)
        self.connection.commit()
        
    def create_ram_report(self, component, usage, time):
        cursor = self.connection.cursor()
        insert_query = "INSERT INTO ram_report VALUES('"+ component +"', "+ str(usage) +" , '"+ time +"')"
        cursor.execute(insert_query)
        self.connection.commit()
                
    def get_all_cpu_report(self):
        cursor = self.connection.cursor()
        select_query = "SELECT * FROM cpu_report"
        cursor.execute(select_query)
        self.connection.commit()
        return cursor
    
    def get_all_ram_report(self):
        cursor = self.connection.cursor()
        select_query = "SELECT * FROM ram_report"
        cursor.execute(select_query)
        self.connection.commit()
        return cursor