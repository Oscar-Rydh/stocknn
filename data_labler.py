import statistics

def moving_average_label(data, days):
    averaged_data = []
    idx = 0
    for datapoint in data:
        if (idx - days < 0):
            averaged_data.append(0)
        else:
            averaged_data.append(mean(data[idx - days : idx]))
            print(data[idx - days : idx])
            print(mean(data[idx - days : idx]))
        idx = idx + 1
    
    labels = []
    for _ in range(0,days):
        labels.append(-1)
    prevDataPoint = -1
    hasActed = True
    for datapoint in averaged_data[days:]:
        if (prevDataPoint < datapoint and hasActed):
            labels.append(1)
            hasActed = False
        elif(prevDataPoint < datapoint and not hasActed):
            labels.append(0)
            hasActed = True
        if (prevDataPoint > datapoint and hasActed):
            labels.append(1)
            hasActed = False
        elif (prevDataPoint > datapoint and not hasActed):
            labels.append(2)
            hasActed = True
    return averaged_data, labels