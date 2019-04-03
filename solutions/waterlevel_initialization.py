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
