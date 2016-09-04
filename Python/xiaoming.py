# -*- coding: utf-8 -*-
height = 1.70
weight = 60
bmi = weight/(height*height)
if bmi < 18.5:
    print('过轻')
elif bmi < 25:
    print('正常')
else:
    print('过重')