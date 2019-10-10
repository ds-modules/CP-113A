import pandas as pd

#read in the original data
original_data =  pd.read_csv('113Adata.csv')

#almost all missing values for years in 2017, so drop that column
original_data = original_data.drop(columns = ['wkswork1'])

#filter out missing values (NaNs) to produce clean dataframe
cleaned = original_data.dropna()

#reduce file size by performing stratified sampling on year, randomly select 160K rows from each year
sampled = cleaned.groupby('year', group_keys=False).apply(lambda x: x.sample(160000))

#export the dataframe as a csv file
export_csv = sampled.to_csv('cp113.csv', index = None, header=True)
