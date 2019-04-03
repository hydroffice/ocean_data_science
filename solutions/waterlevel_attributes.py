class WaterLevel:
    """A Class for Water Level Data"""

    def __init__(self):  # new method

        self.epochs = list()
        self.water_levels = list()
        self.metadata = dict()
        self.metadata["units"] = "m"
        self.metadata["geoid"] = None
        self.metadata["start_time"] = None
        self.metadata["end_time"] = None
        self.metadata["count"] = 0