#-*- coding:utf-8 -*-
__author__ = 'carl'
'''
设方程 y = x1+x2-x3，x1是区间[-2, 5]中的整数，x2是区间[2, 6]中的整数，x3是区间[-5, 2]中的整数。使用爬山法，找到使得y取值最小的解。
'''
import random

def evaluate(x1, x2, x3):
    return x1+x2-x3


x_range = [ [-2, 5], [2, 6], [-5, 2] ]
best_sol = [random.randint(x_range[0][0], x_range[0][1]),
random.randint(x_range[1][0], x_range[1][1]),
random.randint(x_range[2][0], x_range[2][1])]

while True:
    best_evaluate = evaluate(best_sol[0], best_sol[1], best_sol[2])
    current_best_value = best_evaluate
    sols = [best_sol]

    for i in xrange(len(best_sol)):
        if best_sol[i] > x_range[i][0]:
            sols.append(best_sol[0:i] + [best_sol[i]-1] + best_sol[i+1:])
        if best_sol[i] < x_range[i][1]:
            sols.append(best_sol[0:i] + [best_sol[i]+1] + best_sol[i+1:])
    print sols
    for s in sols:
        el = evaluate(s[0], s[1], s[2])
        if el < best_evaluate:
            best_sol = s
            best_evaluate = el
    if best_evaluate == current_best_value:
        break

print 'best sol：', current_best_value, best_sol
