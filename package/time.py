import datetime

class Time:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def get_start_time(self):
        now = datetime.datetime.now()
        self.start_time = now.strftime("%M:%S")

    def get_end_time(self):
        now = datetime.datetime.now()
        self.end_time = now.strftime("%M:%S")

    def get_delay_time(self):
        end = self.end_time.split(':')
        start = self.start_time.split(':')
        
        start_min = int(start[0])
        end_min = int(end[0])
        start_scound = int(start[1])
        end_secound = int(end[1])

        min = end_min - start_min
        if start_scound > end_secound:
            secounds = start_scound - end_secound
        else:
            secounds = end_secound - start_scound
            
        secounds = (min*60) + secounds
        return secounds
