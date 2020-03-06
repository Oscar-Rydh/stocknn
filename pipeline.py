import pandas as pd 
import normalize
import data_labler
import matplotlib.pyplot as plt

def readData(file):
    return pd.read_csv(file)


if __name__ == "__main__":
    data = readData("MSFT.csv")
    data = data[100:200]
    baseline, labels = data_labler.moving_average_label(data["Open"], 5)
    plt.plot(data["Date"], data["Open"])
    plt.plot(data["Date"], baseline)
    plt.show()
    print(labels)
    print(baseline)
    print (data["Open"])
    gaus_data, transformer = normalize.gaussian_normalize(data["Open"].values.reshape(-1,1))
    print(gaus_data)
    std_data, transformer = normalize.standard_normalize(data["Open"].values.reshape(-1,1))
    print(std_data)