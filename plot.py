import glob 
import numpy
import matplotlib.pyplot

filenames = glob.glob('data/inflammation*.csv')
filenames = filenames[0:3]

def analyse(filename):
    print(filename)
    
    data = load_data(filename)
    detect_problems(data)
    plot(data)
    
def load_data(filename):
    return(numpy.loadtxt(fname=filename, delimiter=','))


def detect_problems(data):  
    
    if data.max(axis=0)[0] == 0 and data.max(axis=0)[20] == 20:
        print('Suspicious looking maxima!')
    elif data.min(axis=0).sum() == 0:
        print('Minima add up to zero!')
    else:
        print('Seems OK!')
        
    
def plot(filename):  
    data = numpy.loadtxt(fname=f, delimiter=',')
    
    fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    axes1.set_ylabel('average')
    axes1.plot(data.mean(axis=0))

    axes2.set_ylabel('max')
    axes2.plot(data.max(axis=0))

    axes3.set_ylabel('min')
    axes3.plot(data.min(axis=0))

    fig.tight_layout()
    matplotlib.pyplot.show()

def center(data, desired):
    '''Return a new array containing the origional data
    centered around the desired value. '''
    return(data - data.mean()) + desired

z = numpy.zeros((2,2))
print(z)
print(center(z,3))

data = load_data('data/inflammation-01.csv')
print('original min, mean, and max are:', data.min(), data.mean(), data.max())
centered = center(data, 0)
print('min, mean, and and max of centered data are:', centered.min(), centered.mean(), centered.max())

print('difference in standard deviations before and after:', data.std() - centered.std())


help(center)
# print(center(data,0))

# for f in filenames[:3]:
#     print(f)
#     analyse(f)
#
#