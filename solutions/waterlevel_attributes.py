class WaterLevel:
    """A Class for Water Level Data"""

    def __init__(self):  # new method

        self.times = list()
        self.water_levels = list()
        self.metadata = dict()
        self.metadata["uom"] = "m"
        self.metadata["count"] = 0
