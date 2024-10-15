import pandas as pd
import numpy as np

exam_data = {'name': ['Anastastia', 'Dina', 'James', 'John', 'Loveth', 'Mark', 'King', 'Emily', 'Jonas', 'Laura'], 'score': [13.6, 8, 15.4, 10, np.nan, 15, 12.8, 9, np.nan, 20], 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 'qualify': ['yes', 'no', 'yes', 'no', 'yes', 'yes', 'no', 'no', 'yes', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)
print("Summary of the basic information about this DataFrame and its data:")
print(df.info())