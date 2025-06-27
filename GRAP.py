from pandas import read_csv
import matplotlib.pyplot as plt
x=read_csv("tips (1).csv")
a=x["day"]
b=x["total_bill"]
plt.pie(a.value_counts(),autopct="%.1f%%",radius=1,labels=['sat','sun','fri','thur'])
plt.show()
