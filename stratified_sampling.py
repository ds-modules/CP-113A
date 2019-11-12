import pandas as pd

def takeTableSample(data, column, feature, year):
    data = data[data['year'] == year]
    percentage = data[column].value_counts(normalize=True, sort=True)[feature]
    sample_size = 160000 * percentage
    data = data[data[column] == feature]
    return data.sample(int(sample_size))

def sampledTable(data, column, year):
    sample = pd.DataFrame()
    for feature in data[data['year'] == year][column].value_counts(normalize=True, sort=True).index:
        new_sample = takeTableSample(data, column, feature, year)
        sample = pd.concat([sample, new_sample])
    return sample
