import sklearn.preprocessing as prep

def gaussian_normalize(data):
    transformer = prep.PowerTransformer(method='box-cox', standardize=False)
    transformer.fit_transform(data)
    return data, transformer

def standard_normalize(data):
    transformer = prep.StandardScaler()
    transformer.fit_transform(data)
    return data, transformer