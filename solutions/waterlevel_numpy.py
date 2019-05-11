import matplotlib.pyplot as plt
import numpy as np
import os
from datetime import datetime, timezone


class WaterLevel:
    """A Class for Water Level Data"""

    def __init__(self, data_path):
        
        if not os.path.exists(data_path):
            raise RuntimeError("Unable to locate the data file: %s" % data_path)   

        self.data_path = data_path
        self.data = None
        self.metadata = dict()
        self.metadata["uom"] = "m"
        self.metadata["count"] = 0

    def __str__(self):
        count_txt = "count: %d" % (self.metadata["count"])
        path_txt = "path: %s" % (self.data_path)
        txt = "WaterLevel[%s, %s]" % (count_txt, path_txt)
        return txt        
        
    def read(self):
        # Open, read the content, and close the file
        wl_file = open(self.data_path)
        wl_content = wl_file.read()
        wl_file.close()
        
        # Create temporary lists
        times = list()
        water_levels = list()

        # Tokenize the contents
        wl_lines = wl_content.splitlines()
        count = 0  # initialize the counter for the number of rows read
        for wl_line in wl_lines:
            observations = wl_line.split()  # Tokenize the string
            time = datetime.fromtimestamp(float(observations[5]), timezone.utc)
            times.append(time)
            water_levels.append(float(observations[6]))
            count += 1
            
        self.data = np.array([times, water_levels])
        self.metadata["count"] = count
        
    def plot(self):
        
        if self.metadata["count"] == 0:
            raise RuntimeError("No data to plot!")
        
        avg_wl = self.data[1, :].mean()  # average water level
        
        plt.plot(self.data[0, :], self.data[1, :], label='data')
        plt.axhline(y=avg_wl, color='orange', linestyle='dashed', label='avg')
        plt.title("Water Levels")
        plt.xlabel("Time")
        plt.ylabel("Level[m]")
        plt.grid()
        plt.gcf().autofmt_xdate()  # beautify the x-labels
        plt.legend()
        plt.show()
