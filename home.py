import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
lst2 = []
lst3 = []
for i in lst:
  if i == 'robot':
    lst2 += ['1']
    lst3 += ['0']
  else:
    lst2 += ['0']
    lst3 += ['1']
data2 = pd.DataFrame({'robot':lst2, 'human':lst3})
data2.head()