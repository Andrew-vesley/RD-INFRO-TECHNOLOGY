import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = {
    'Student': ['Amit', 'Bina', 'Chitra', 'Deepak', 'Esha'],
    'Math': [88, 92, 79, 93, 85],
    'Science': [90, 85, 82, 95, 87]
}


df = pd.DataFrame(data)

sns.set(style="whitegrid")

plt.figure(figsize=(8, 5))
sns.barplot(x='Student', y='Math', data=df, palette='Blues_d')
plt.title('Math Scores by Student')
plt.ylabel('Score')
plt.xlabel('Student')
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(x='Math', y='Science', data=df, hue='Student', s=100)
plt.title('Math vs Science Scores')
plt.xlabel('Math Score')
plt.ylabel('Science Score')
plt.tight_layout()
plt.show()
