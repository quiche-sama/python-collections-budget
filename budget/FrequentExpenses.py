import collections
from budget.Expense import Expenses, Expense
import matplotlib.pyplot as plt
expenses = Expenses()
expenses.read_expenses("../data/spending_data.csv")

spending_categories = []

for expense in expenses.list:
    spending_categories.append(expense.category)

spending_counter = collections.Counter(spending_categories)
print(spending_counter)

top5 = spending_counter.most_common(5)
k, v = zip(*top5)

fig, ax = plt.subplots()
ax.bar(k, v)
ax.set_title('# of Purchases by Category')

plt.show()
