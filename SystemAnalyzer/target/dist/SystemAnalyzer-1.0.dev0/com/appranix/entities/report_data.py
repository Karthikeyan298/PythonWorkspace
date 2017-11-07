class ReportData(object):
    
    __component = ""
    __usage = ""
    __time = ""
    
    def set_component(self, component):
        self.__component = component
        
    def set_usage(self, usage):
        self.__usage = usage
        
    def set_time(self, time):
        self.__time = time      
     
    def get_component(self):
        return self.__component 
        
    def get_usage(self):
        return self.__usage
        
    def get_time(self):
        return self.__time