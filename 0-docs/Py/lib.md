## numpy

> import numpy as np



## Matplotlib

[Tutorials](https://matplotlib.org/3.1.1/tutorials/index.html) 

## pickle

> import pickle

| 函数                          | 描述                                                         |
| ----------------------------- | ------------------------------------------------------------ |
| pickle.dump(object, file, -1) | 将object对象序列化到file文件中，file= open('ModelFile.txt','wb') |
| object=pickle.load(FILE)      | 加载文件中的内容                                             |
| var = pickle.dumps(object)    | 将object对象序列化到变量中                                   |
| var1 =pickle.loads(var2)      | 加载变量中的内容                                             |



## joblib

> from sklearn.externals import joblib

| 函数    | 描述                                 |
| ----------------- | ------------------------------------ |
|joblib.dump(object, 'file.joblib')| 将object对象序列化到file.joblib文件中|
|var = joblib.load('file.joblib')| 加载文件中的内容 |



## sys

| 函数    | 描述                                 |
| ----------------- | ------------------------------------ |
|sys.argv|读取main函数调用的参数|