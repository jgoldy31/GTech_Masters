import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from scipy.stats import gaussian_kde
def get_kde(data,x, h):
    vals = np.zeros(x.shape)
    for d in data:
        vals += norm.pdf((x - d) / h) / h
    return vals / len(data)

data = pd.read_csv('data/n90pol.csv')
amygdala_data = data['amygdala']
acc_data = data['acc']
bin_num = 12
fig, hists= plt.subplots(1, 2, figsize=(12, 6))

# Amygdala histogram
hists[0].hist(data['amygdala'], bins=bin_num, density=True, edgecolor = 'black')
hists[0].set_title('Amygdala Histogram')
hists[0].set_xlabel('Amygdala Size')
hists[0].set_ylabel('Occurrences')

# ACC histogram
hists[1].hist(data['acc'], bins=bin_num, density=True,  edgecolor = 'black')
hists[1].set_title('ACC Histogram')
hists[1].set_xlabel('ACC Size')
hists[1].set_ylabel('Occurrences')
fig.savefig('1D_histograms.png')
plt.clf()
plt.close(fig)

#played around with bandwidth, .0075 shows shape but doesn't overfit
h = 0.0075
xs = np.linspace(min(data['amygdala'].min(), data['acc'].min()),
                  max(data['amygdala'].max(), data['acc'].max()),
                  1000)
kdeam = get_kde(data['amygdala'],xs,h)
kdeacc = get_kde(data['acc'],xs, h)
fig, hists = plt.subplots(1, 2, figsize=(12, 6))
#Amagydala
hists[0].plot(xs, kdeam, color='red')
hists[0].set_title('Amygdala KDE')
hists[0].set_xlabel('Amygdala Size')
hists[0].set_ylabel('Density')
hists[0].legend()

#ACC
hists[1].plot(xs, kdeacc, color='red')
hists[1].set_title('ACC KDE')
hists[1].set_xlabel('ACC Size')
hists[1].set_ylabel('Density')
hists[1].legend()
fig.savefig('1D_KDE.png')
plt.clf()
plt.close(fig)

bin_size = 20
#2D hist
plt.figure(figsize=(10, 6))
plt.hist2d(data['amygdala'], data['acc'], bins=[bin_size, bin_size], cmap='Blues')
plt.xlabel('Amygdala Size')
plt.ylabel('ACC Size')
plt.title('2D Histogram of Amygdala and ACC')
cbar = plt.colorbar()
cbar.set_label('Occurrences')

plt.savefig('2D_Histogram.png')
plt.clf()

#2D KDE
#https://stackoverflow.com/questions/4128699/using-scipy-stats-gaussian-kde-with-2-dimensional-data
combine = np.vstack((data['amygdala'], data['acc']))
kde = gaussian_kde(combine)
xs = np.linspace(data['amygdala'].min(), data['amygdala'].max(), 1000)
ys = np.linspace(data['acc'].min(),data['acc'].max(), 1000)
#make into coordinate pairs
cor_X, cor_Y = np.meshgrid(xs, ys)
coordinates = np.vstack([cor_X.ravel(), cor_Y.ravel()])
reshaped_coors = kde(coordinates).T
density_vals = np.reshape(reshaped_coors, cor_X.shape)

plt.figure(figsize=(12, 6))
#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contour.html
contour = plt.contourf(cor_X, cor_Y, density_vals, cmap='Reds')
plt.scatter(combine[0], combine[1], color='black', alpha=0.5, label='Individual Points')
plt.colorbar(contour, label='Density')
plt.xlabel('Amygdala Size')
plt.ylabel('ACC Size')
plt.title('2D KDE')
plt.savefig('2D_KDE.png')
plt.clf()

#check joint probabilities 
df = pd.DataFrame(data)
joint = df.value_counts(["acc", "amygdala"], normalize=True)
marginals = pd.crosstab(df["acc"], df["amygdala"], margins=True, normalize=True)
prod = marginals.iloc[1, 1] * marginals.iloc[2, 2]
diffs = abs(prod - joint.iloc[0])
print(diffs)



fig, ks = plt.subplots(2, 1, figsize=(12, 12))
h = .3
for orientation in range(2, 6):
    kdeamy = gaussian_kde(data[data['orientation'] == orientation]['amygdala'], bw_method=h)
    kdeacc = gaussian_kde(data[data['orientation'] == orientation]['acc'], bw_method=h)
    #amygdala
    ks[0].plot(xs, kdeamy(xs), label=f'KDE Amygdala - {orientation}')
    #acc
    ks[1].plot(xs, kdeacc(xs), label=f'KDE ACC - {orientation}')

    am = np.mean(data[data['orientation'] == orientation]['amygdala'])
    print('Mean Amygdala Orientation ' + str(orientation))
    print(am)
    acc = np.mean(data[data['orientation'] == orientation]['acc'])
    print('Mean ACC Orientation ' + str(orientation))
    print(acc)


ks[0].set_xlabel('Amygdala Size')
ks[0].set_ylabel('Density')
ks[0].set_title('Conditional Estimates Amygdala')
ks[0].legend()

ks[1].set_xlabel('ACC Size')
ks[1].set_ylabel('Density')
ks[1].set_title('Conditional Estimates ACC')
ks[1].legend()

plt.savefig('kde_conditional.png')
plt.clf()

h = .3
plt.figure(figsize=(12, 8))
for orientation in range(2, 6):
    curr_data = data[data['orientation'] == orientation][['amygdala', 'acc']]
    kde = gaussian_kde(curr_data.T, bw_method=h)

    #Coordinates again
    xs = np.linspace(curr_data['amygdala'].min(), curr_data['amygdala'].max(), 1000)
    yss = np.linspace(curr_data['acc'].min(), curr_data['acc'].max(), 1000)
    cor_x, cor_y = np.meshgrid(xs, ys)
    coordinates = np.vstack([cor_x.ravel(), cor_y.ravel()])
    vals = kde(coordinates)
    density_vals = np.reshape(vals.T, cor_x.shape)

    space = orientation - 1
    plt.subplot(2, 2, space)
    contour = plt.contourf(cor_x, cor_y, density_vals, cmap='Reds')
    plt.colorbar(contour, label='Density')
    plt.xlabel('Amygdala Size')
    plt.ylabel('ACC Size')
    plt.title(f' Joint 2D KDE - {orientation}')

plt.tight_layout()
plt.savefig('2D_KDE_joint.png')



