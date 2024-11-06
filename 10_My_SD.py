#
# Zach
# 11/6/24
# my sd
#

import statistics
import math

def my_sd(input):
        print(f'Input : {input}')
        length = len(input)
        sum = 0
        output = 0
        mean = statistics.mean(input)
        print(f'Mean  : {mean}')
        for x in input:
                sum += (int(x) - mean)**2
        sum = sum / length
        output = math.sqrt(sum)
        return output

answer =my_sd([10,20,30])
answer = round(answer, 2)
print(f'Answer: {answer}')