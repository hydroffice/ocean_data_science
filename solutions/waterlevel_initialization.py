class WaterLevel:
    """A Class for Water Level Data"""

    def __init__(self, data_path):  # new code
        
        self.data_path = data_path  # new code
        self.times = list()
        self.water_levels = list()
        self.metadata = dict()
        self.metadata["uom"] = "m"
        self.metadata["count"] = 0
