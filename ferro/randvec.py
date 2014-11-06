import numpy as np
import itertools

vec = 2*np.random.random_sample((3,1))-1
norm = np.apply_along_axis(np.linalg.norm, 0, vec)
ready = np.transpose(np.round(vec/(0.5*norm),2))
ready2 = np.round(list(itertools.chain.from_iterable(ready)),2)
out = ' '.join(map(str, ready2))
print 'MAGMOM = ' + out + ' 6*0'
