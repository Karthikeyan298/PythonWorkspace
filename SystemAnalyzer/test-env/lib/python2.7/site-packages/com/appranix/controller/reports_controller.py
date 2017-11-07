'''
Created on 03-Nov-2017

@author: karthikeyan
'''
from flask import Flask 
import json
from com.appranix.service.report_service import ReportService

app = Flask(__name__)
 
# @app.route("/")
# def redirector():
#     render_template('index.html')

@app.route("/report/cpu")
def get_cpu_report():
    reportService = ReportService()
    return str([dict(zip(['name', 'usage', 'time'], row)) for row in reportService.get_all_cpu_report().fetchall()])
 
@app.route("/report/virtualmemory")
def get_virtual_memory_report():
    reportService = ReportService()
#     return json.dumps(reportService.get_all_ram_report().__dict__)
    return str([dict(zip(['name', 'usage', 'time'], row)) for row in reportService.get_all_ram_report().fetchall()])
 
def start_flask():
    app.run()