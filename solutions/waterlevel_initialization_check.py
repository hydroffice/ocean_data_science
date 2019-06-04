import os  # new code


class WaterLevel:
    """A Class for Water Level Data"""

    def __init__(self, data_path):
        
        if not os.path.exists(data_path):  # new code
            raise RuntimeError('Unable to locate the data file: %s' % data_path)  # new code

        self.data_path = data_path
        self.times = list()
        self.water_levels = list()
        self.metadata = dict()
        self.metadata["uom"] = "m"
        self.metadata["count"] = 0
