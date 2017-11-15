import pandas as pd
import numpy as np
import cPickle

f = open('influence.p','r')
I = cPickle.load(f)
f.close()

f = open('conv_lens.p','r')
count_lens = cPickle.load(f)
f.close()

conv_lens = [sum(i) for i in count_lens]

print I[:10]
print conv_lens[:10]
print len(I), len(conv_lens)

A = np.array(I)
B = np.array(conv_lens)

df = pd.DataFrame({'A':A,'B':B})
corr = df['A'].corr(df['B'])

print corr