#data preprocessing
import pandas as pd
import time
from datetime import datetime
from collections import OrderedDict
import os
import numpy as np

path = "./"
names = ['Timestamp', 'AF3 Value', 'AF3 Quality', 'AF4 Value', 'AF4 Quality', 'F3 Value', 'F3 Quality', 'F4 Value', 'F4 Quality', 'F7 Value', 'F7 Quality', 'F8 Value', 'F8 Quality', 'Label']
trials_data = OrderedDict((el, []) for el in names)
# loop through files in the current dir
for file in sorted(os.listdir(path)):
    if '.csv' in file:
        df = pd.read_csv(path+file)
        l = len(df)

        start_time = time.mktime(datetime.strptime(df['Timestamp'][0], "%Y-%m-%d %H:%M:%S.%f").timetuple())
        end_time = time.mktime(datetime.strptime(df['Timestamp'][l-1], "%Y-%m-%d %H:%M:%S.%f").timetuple())

        timestamps = []
        timestamps.append([start_time+10, False])

        t_next = timestamps[len(timestamps)-1][0]+8
        t_next_next = timestamps[len(timestamps)-1][0]+13

        while t_next_next < end_time:
            timestamps.append([t_next, True])
            timestamps.append([t_next_next, False])
            t_next = timestamps[len(timestamps)-1][0]+8
            t_next_next = timestamps[len(timestamps)-1][0]+13

        if t_next < end_time:
            timestamps.append([t_next, True])
            timestamps.append([end_time, False])
        else:
            timestamps.append([end_time, True])

        timestamp_iter = 0
        label_iter = 0

        for item, row in df.iterrows():
            if len(row['Timestamp']) == 26:
                timestamp = time.mktime(datetime.strptime(row['Timestamp'], "%Y-%m-%d %H:%M:%S.%f").timetuple())
            else:
                timestamp = time.mktime(datetime.strptime(row['Timestamp'], "%Y-%m-%d %H:%M:%S").timetuple())

            if timestamp <= timestamps[timestamp_iter][0]:
                if timestamps[timestamp_iter][1]:
                    # now save your stuff
                    for key in trials_data.keys():
                        if 'Label' not in key:
                            trials_data[key].append(row[key])
                    if label_iter % 2 == 0:
                        trials_data['Label'].append('R')
                    else:
                        trials_data['Label'].append('L')

            else:
                # we only get here if we pass from one interval to the next
                timestamp_iter += 1
                if timestamps[timestamp_iter][1]:
                    label_iter += 1
                    for key in trials_data.keys():
                        if 'Label' not in key:
                            trials_data[key].append(row[key])
                    if label_iter % 2 == 0:
                        trials_data['Label'].append('R')
                    else:
                        trials_data['Label'].append('L')