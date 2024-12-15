# imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# reading data
dataset = pd.read_excel("./HousePricePrediction.xlsx")
print(dataset.head(5))

# dimensions
dataset.shape

# Numerical feature selection
num_dataset = dataset.select_dtypes(include=['number'])

# feature categorization
obj = (dataset.dtypes == 'object')
object_cols = list(obj[obj].index)
print("Categorical variables:",len(object_cols))

int_ = (dataset.dtypes == 'int')
num_cols = list(int_[int_].index)
print("Integer variables:",len(num_cols))

fl = (dataset.dtypes == 'float')
fl_cols = list(fl[fl].index)
print("Float variables:",len(fl_cols))

plt.figure(figsize=(12, 6))
sns.heatmap(num_dataset.corr(),
            cmap = 'BrBG',
            fmt = '.2f',
            linewidths = 2,
            annot = True)

# analyzing category
unique_values = []
for col in object_cols:
  unique_values.append(dataset[col].unique().size)
plt.figure(figsize=(10,6))
plt.title('No. Unique values of Categorical Features')
plt.xticks(rotation=90)
sns.barplot(x=object_cols,y=unique_values)

# separating features
plt.figure(figsize=(18, 36))
plt.title('Categorical Features: Distribution')
plt.xticks(rotation=90)
index = 1

for col in object_cols:
    y = dataset[col].value_counts()
    plt.subplot(11, 4, index)
    plt.xticks(rotation=90)
    sns.barplot(x=list(y.index), y=y)
    index += 1

# show plots
plt.show()

# data cleaning
dataset['SalePrice'] = dataset['SalePrice'].fillna(
   dataset['SalePrice'].mean()
)

new_dataset = dataset.dropna()
new_dataset.isnull().sum()
