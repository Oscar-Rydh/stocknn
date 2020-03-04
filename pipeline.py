import pandas as pd 
import normalize

def readData(file):
    return pd.read_csv(file)


if __name__ == "__main__":
    data = readData("MSFT.csv")
    print (data["Open"])
    gaus_data, transformer = normalize.gaussian_normalize(data["Open"].values.reshape(-1,1))
    print(gaus_data)
    std_data, transformer = normalize.standard_normalize(data["Open"].values.reshape(-1,1))
    print(std_data)