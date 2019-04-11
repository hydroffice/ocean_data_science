import os


class WaterLevel:
    """A Class for Water Level Data"""

    def __init__(self, data_path):  
        
        if not os.path.exists(data_path):
            raise RuntimeError('Unable to locate the data file: %s' % data_path)   

        self.data_path = data_path
        self.times = list()
        self.water_levels = list()
        self.metadata = dict()
        self.metadata["uom"] = "m"
        self.metadata["count"] = 0

    def __str__(self): # new method
        count_txt = "count: %d" % (self.metadata["count"])
        path_txt = "path: %s" % (self.data_path)
        txt = "WaterLevel[%s, %s]" % (count_txt, path_txt)
        return txt        
        