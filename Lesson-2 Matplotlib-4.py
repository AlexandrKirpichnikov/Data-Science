plt.style.use('fivethirtyeight')
df = pd.read_csv('creditcard.csv')
df.head()
df_class = df['Class'].value_counts()
print(df_class)

df_class.plot(kind='barh')
plt.show()

df_class.plot(kind='barh', logx=True)
plt.show()

class0 = df.loc[df['Class'] == 0, ['V1']]
class1 = df.loc[df['Class'] == 1, ['V1']]

plt.hist(class0['V1'], bins=20, density=True, alpha=0.5, label='Class 0', color='grey')
plt.hist(class1['V1'], bins=20, density=True, alpha=0.5, label='Class 1', color='red')
plt.xlabel("V1")
plt.legend()
plt.show()