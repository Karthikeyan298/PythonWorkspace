'''
Created on 03-Nov-2017

@author: karthikeyan
'''
import psutil
import datetime
import time
from com.appranix.entities.report_data import ReportData
from com.appranix.service.report_service import ReportService

class MetricsCollector(object):
    ram_report_data = ReportData()
    cpu_report_data = ReportData()
    
    def get_cpu_metrics(self):
        self.cpu_report_data.set_component("CPU")
        self.cpu_report_data.set_usage(psutil.cpu_percent(interval=1))
        self.cpu_report_data.set_time(str(datetime.datetime.now()))
        return self.cpu_report_data
     
    def get_ram_metrics(self):     
        self.ram_report_data.set_component("VirtualMemory")
        self.ram_report_data.set_usage(psutil.virtual_memory().percent)
        self.ram_report_data.set_time(str(datetime.datetime.now()))  
        return self.ram_report_data 
    
    def do_collect_metrics(self):
        while True:
            self.get_cpu_metrics()
            self.get_ram_metrics()
            report_service = ReportService()
            report_service.create_cpu_report(self.cpu_report_data.get_component(), self.cpu_report_data.get_usage(), self.cpu_report_data.get_time())
            report_service.create_ram_report(self.ram_report_data.get_component(), self.ram_report_data.get_usage(), self.ram_report_data.get_time())
            time.sleep(10)

if __name__ == '__main__':
    collector = MetricsCollector()
    collector.do_collect_metrics()  