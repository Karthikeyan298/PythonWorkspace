'''
Created on 04-Nov-2017

@author: karthikeyan
'''
from multiprocessing import Process
from com.appranix.collector.metrics_collector import MetricsCollector
from com.appranix.controller import reports_controller
# import all other scripts as well

def start_metric_collector(*args):
    collector = MetricsCollector()
    collector.do_collect_metrics()
    
    
def start_flask(*args):
    reports_controller.start_flask()

if __name__ == '__main__':
    p = Process(target=start_metric_collector, args=("Either so", ))
    p1 = Process(target=start_flask, args=("or so", ))
    p.start()
    p1.start()
