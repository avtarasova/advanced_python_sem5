
import matplotlib.pyplot as plt

import numpy as np
from scipy.interpolate import interp1d

X = [ 284.882, 286.914, 288.88, 290.894, 292.846, 297.76, 302.764, 307.974, 311.486 ]
Y = [ 7.9878, 7.9495, 7.8843, 7.7745, 7.5933, 7.1813, 7.0806, 7.0413, 7.0231 ]


cubic_interploation_model = interp1d ( X, Y, kind = "cubic" )
X_ = np.linspace ( min ( X ), max ( X ), 500 )
Y_ = cubic_interploation_model ( X_ )


plt.clf()

fig, ax = plt.subplots()
fig.set_size_inches ( ( 16, 9 ) )

ax.grid ( b = True, axis = 'both', zorder = -4, alpha = 0.4 )

ax.set_ylim ( 6.5, 8.5 )
ax.set_xlim ( 280, 315 )

# fig.suptitle ( 'graph t ( T )', fontsize = 32, horizontalalignment = 'center', verticalalignment = 'center' )
# plt.xlabel ( 'T Temperature, K', y = 6.2, fontsize = 18 )
plt.ylabel ( 't period, mks', fontsize = 16 )

ax.text ( 297, 6.3, 'T Temperature, K', fontsize = 18, horizontalalignment = 'center' )
ax.text ( 297, 8.6, 'graph t ( T )', fontsize = 32, horizontalalignment = 'center' )

# ax.plot ( X, Y, color = '#ff7f7b', lw = 12, alpha = 0.42 )
# ax.plot ( X, Y, color = '#7f007b', lw = 4, alpha = 0.42 )
ax.scatter ( X, Y, color = '#ffffff', s = 42, alpha = 1, zorder = 3 )
ax.plot ( X_, Y_, color = '#042559', lw = 8, alpha = 0.42, zorder = 2 )
ax.scatter ( X, Y, marker = '|', color = '#000000', s = 242, alpha = 1, zorder = 1 )
# ax.scatter ( X_, Y_, color = 'k', s = 3, alpha = 0.92 )

plt.savefig ( 'lec05_image.png', dpi = 300 )#, bbox_inches = 'tight'

exit()



# tuple

# list



lsA = [ 1, 2, 3, 42, 1 ]

a = len ( lsA )
print ( a )

print ( lsA )
lsA.sort () #reverse = True 
print ( lsA )


lsA += [ 19, 39 ]
print ( lsA )

# lsA.append ( [ 64, 72 ] )
# print ( lsA )

lsA.extend ( [ 64, 72 ] )
print ( lsA )



lsA.append ( 101 )
print ( lsA )



# print ( lsA[::-1] )

# print ( lsA[0:8:] )
# print ( lsA[-8:-1:] )
# print ( lsA [ len(lsA):-5:-1 ] )

st = 'abrakadabrapython'
print ( st )
print ( st[::-1] )





