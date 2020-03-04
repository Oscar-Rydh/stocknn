import sklearn.preprocessing as prep

def gaussian_normalize(data):
    transformer = prep.PowerTransformer(method='box-cox', standardize=False)
    transformer.fit_transform(data)
    return data, transformer