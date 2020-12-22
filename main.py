import pickle
import pandas as pd
import numpy as np
from datetime import datetime

# 단어인가? 아닌가? 명사인가? 아닌가?

thought = input('생각을 적어보시오: ')

print('my answer :', thought)

# 전처리
thought = thought.strip('. ')
words = thought.split()

print('words : ', words)

noun = []
for x in words:
    tmp = ''
    while len(x):
        print("'{}'은 명사입니까?".format(x))
        answer = input('1/0 : ')
        if answer == '1':
            tmp = x
            break
        else:
            x = x[:-1]
    if len(tmp):
        noun.append(tmp)


