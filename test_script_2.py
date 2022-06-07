import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def test_script_2():
  df = pd.read_csv('data_out.csv', delimiter=';')
  df2 = df.copy()

  lst = []

  for i in range(0, df2.shape[1], 2):
    lst.append(i)
  df2.drop(df2.columns[[lst]], axis=1, inplace=True) 

  posLstDraw = []

  for i in range(len(df2)):
    posLstDraw += list(df2.columns)

  df2_tmp = df.copy()
  lst2 = []

  for i in range(3, df2_tmp.shape[1], 2):
    lst2.append(i)
  df2_tmp.drop(df2_tmp.columns[[lst2]], axis=1, inplace=True)
  df2_tmp = df2_tmp.drop("Date/Pos", axis=1)
  df2_tmp = df2_tmp.drop("-1", axis=1)

  pcntLstDraw = []

  tmp = df2_tmp.values.tolist()
  for i in range(len(df2_tmp)):
    pcntLstDraw += tmp[i]

  x = posLstDraw
  y = pcntLstDraw
  plt.bar(x, y)
  plt.title("Task 2.2")
  plt.xlabel("posLstDraw")
  plt.ylabel("pcntLstDraw")

  df3 = df.copy()

  lst = []
  for i in range(2, df2.shape[1], 2):
    lst.append(i)
  df3.drop(df3.columns[[lst]], axis=1, inplace=True) 

  xLst = list(df3['Date/Pos'])

  yLst = []

  for rowIndex, row in df3.iterrows():
    sumRes = 0
    for columnIndex, value in row.items():
      if type(value) == type(float()):
        sumRes += value
    yLst.append(sumRes)

  fig, ax = plt.subplots()
  x1 = xLst
  y1 = yLst
  ax.plot(x1, y1)
  plt.grid(False) 
  ax.set(title='Task 2.1')
  plt.show()

if __name__ == '__main__':
    test_script_2()