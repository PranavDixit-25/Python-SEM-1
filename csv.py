
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("student-dataset.csv")

sns.countplot(x='english.grade', data=data)
plt.title('english Grade Distribution')
plt.show()

sns.countplot(x='language.grade', data=data)
plt.title('language Grade Distribution')
plt.show()



sns.heatmap(data[['english.grade', 'language.grade']].corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()

