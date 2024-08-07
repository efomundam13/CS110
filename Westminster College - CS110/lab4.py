#Problem 1a
def translate(p, dx, dy):
    x, y = p
    return (x + dx, y + dy)

#Problem 1b
import math

def rotate(p, theta):
    theta_rad = math.radians(theta)

    x, y = p

    x_new = x * math.cos(theta_rad) - y * math.sin(theta_rad)
    y_new = x * math.sin(theta_rad) + y * math.cos(theta_rad)

    return (x_new, y_new)

#Problem 2
#a) len(s)
    #5
#b) s | t
    #{'t', 'o', 'n', 'c', 'y', 'h', 'p', 'm'}
#c) s & t
    #{'n', 'y', 't'}
#d) s - t
    #{'c', 'm'}
#e) t - s
    #{'p', 'h', 'o'}
#f) s ^ t
    #{'o', 'c', 'h', 'p', 'm'}
#g) s < t
    #False
#h) (s - t) < t
    #False
#i) (t - s) < t
    #True
#j) (s - t)|(t-s) <= (t^s)
    #true
#k) t after t.add('s')
    #{'p', 'y', 't', 'h', 'o', 'n', 's'}
#l) t after t.add('t')
    #{'p', 'y', 't', 'h', 'o', 'n'}

#Problem 3
def num_unique_words(fname):
    with open(fname, 'r') as f:
        words = f.read().split()
        unique_words = set(words)
        return len(unique_words)
