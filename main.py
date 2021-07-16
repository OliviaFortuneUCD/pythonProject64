# import the necessary library
import pandas as pd
import re
import matplotlib.pyplot as plt

# import dataset
data = pd.read_csv("daft_v_2.csv")
print(data.head(5))

# convert the string in "price" col to integer.

p_list = []

for price in data["price"]:
    num = re.findall("\d+\.?\d*", price)
    num = "".join(num)
    num = int(num)

    if "Per week" in price:
        num = (num / 7) * 30  # convert the weekly rental to monthly

    p_list.append(num)

data_copy = data.copy()
data_copy["price"] = p_list
fig1 = plt.figure(figsize=(15,8))
ax1 = plt.subplot()

ax1.hist(x = data_copy["price"],bins = 100)

plt.xlim((0,15000)) # set the x limited value.
plt.xlabel("monthly rental")
plt.ylabel("count")
plt.title("Monthly Rental Histogram")
plt.show()


