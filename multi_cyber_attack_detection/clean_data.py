import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
#from dataprep.eda import plot, plot_missing, plot_correlation
import plotly.express as px

df = pd.read_csv('cybersecurity_attacks.csv')
print('+'*100)

print(df.head())
print('+'*100)

print(df.info())
print('+'*100)

print(df.shape)
print('+'*100)

print(df.describe())
print('+'*100)

print(df.isnull().sum())
print('+'*100)


df.dropna(inplace=True)
df.shape
df.duplicated().sum() 

print(df.head())
print('+'*100)

df.to_csv('cybersecurity_attacks_updated - Copy.csv', index=False)


attack_counts = df['Attack Type'].value_counts()
print(attack_counts)
# Set a color palette for the plot
colors = sns.color_palette('viridis', len(attack_counts))

# Plotting
plt.figure(figsize=(12, 6))
sns.barplot(x=attack_counts.index, y=attack_counts, palette=colors)

# Adding data labels
for i, count in enumerate(attack_counts):
    plt.text(i, count + 0.1, str(count), ha='center', va='bottom', fontsize=10, fontweight='bold')

# Adding labels and title
plt.xlabel('Attack Type', fontsize=14, fontweight='bold')
plt.ylabel('Count', fontsize=14, fontweight='bold')
plt.title('Distribution of Attack Types', fontsize=16)

# Rotating x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Display the plot
plt.tight_layout()
plt.savefig('attacktype.png')

plt.show()

df['Severity Level'] = pd.factorize(df['Severity Level'])[0]

# Point plot for Attack Type
sns.pointplot(data=df, x="Severity Level", y="Attack Type", hue="Attack Type", markers="o", linestyles="")
plt.title("Severity Level vs Attack Type")
plt.xlabel("Severity Level")
plt.ylabel("Attack Type")
plt.legend(title="Attack Type", loc="upper right")
plt.savefig('pointplot.png')
plt.show()

#px.scatter_3d(df, x='Source Port', y='Destination Port', z='Packet Length', color='Protocol').show()
#for col in ['Protocol', 'Packet Type', 'Traffic Type', 'Severity Level', 'Log Source']:
plt.figure(figsize=(8,7))
sns.countplot(data=df, y=df['Protocol'], hue='Attack Type')
plt.savefig('Protocol.png')

plt.show()


plt.figure(figsize=(8,7))
sns.countplot(data=df, y=df['Packet Type'], hue='Attack Type')
plt.savefig('PacketType.png')

plt.show()

plt.figure(figsize=(8,7))
sns.countplot(data=df, y=df['Traffic Type'], hue='Attack Type')
plt.savefig('Traffictype.png')

plt.show()


plt.figure(figsize=(8,7))
sns.countplot(data=df, y=df['Severity Level'], hue='Attack Type')
plt.savefig('SeverityLevel.png')

plt.show()


plt.figure(figsize=(8,7))
sns.countplot(data=df, y=df['Log Source'], hue='Attack Type')
plt.savefig('Log Source.png')

plt.show()