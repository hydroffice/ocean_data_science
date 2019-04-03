class WaterLevel:
    """A Class for Water Level Data"""

    def __init__(self, data_path):  # new code

        self.data_path = data_path  # new code
        self.epochs = list()
        self.water_levels = list()
        self.metadata = dict()
        self.metadata["units"] = "m"
        self.metadata["geoid"] = None
        self.metadata["start_time"] = None
        self.metadata["end_time"] = None
        self.metadata["count"] = 0

    def __str__(self):
        count_txt = "count: %d" % (self.metadata["count"])
        path_txt = "path: %s" % (self.data_path)
        txt = "WaterLevel[%s, %s]" % (count_txt, path_txt)
        return txt        
        