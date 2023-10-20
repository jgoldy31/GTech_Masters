import numpy as np
from scipy.io import loadmat
from scipy.stats import multivariate_normal
from sklearn.decomposition import PCA
import numpy as np
import numpy.matlib
import pandas as pd
from scipy.stats import multivariate_normal as mvn
import matplotlib.pyplot as plt
from sklearn import preprocessing
import seaborn as sb
from sklearn.cluster import KMeans

#modified demo code and added computations
# Load data and labels
data = loadmat('data/data.mat',squeeze_me=True)['data'].T # each image is a row
labels = loadmat('data/label.mat',squeeze_me=True)['trueLabel']
m,n = data.shape
y = labels[0]
# Standardize the data
ndata = preprocessing.scale(data)
C = np.matmul(data.T, data)/m
# pca the data
d = 4  # reduced dimension
V,Sig,_ = np.linalg.svd(C)
V = V[:, :d]

# project the data to the top 4 principal directions
pdata = np.dot(data,V)

# Plot the projected data
plt.scatter(pdata[np.where(y == 1), 0], pdata[np.where(y == 1), 1])
plt.scatter(pdata[np.where(y == 2), 0], pdata[np.where(y == 2), 1])
plt.scatter(pdata[np.where(y == 3), 0], pdata[np.where(y == 3), 1])

# EM-GMM for wine data
K = 2  # Number of mixtures

# Random seed
seed = 2
np.random.seed(seed)

# Initialize prior
pi = np.random.random(K)
pi = pi / np.sum(pi)

# Initialize mean and covariance
mu = np.random.randn(K, d)
mu_old = mu.copy()

sigma = []
for ii in range(K):
    # Ensure the covariance is positive semidefinite
    dummy = np.random.randn(d, d)
    sigma.append(dummy @ dummy.T)

# Initialize the posterior
tau = np.full((m, K), fill_value=0.)

maxIter = 100
tol = 1e-3
track_log = []

for ii in range(maxIter):
    # E-step
    for kk in range(K):
        tau[:, kk] = pi[kk] * mvn.pdf(pdata, mu[kk], sigma[kk])
        

    # Normalize tau
    sum_tau = np.sum(tau, axis=1)
    sum_tau.shape = (m, 1)
    tau = np.divide(tau, np.tile(sum_tau, (1, K)))

    # M-step
    for kk in range(K):
        # Update prior
        pi[kk] = np.sum(tau[:, kk]) / m

        # Update component mean
        mu[kk] = pdata.T @ tau[:, kk] / np.sum(tau[:, kk], axis=0)

        # Update cov matrix
        dummy = pdata - np.tile(mu[kk], (m, 1))  # X-mu
        sigma[kk] = dummy.T @ np.diag(tau[:, kk]) @ dummy / np.sum(tau[:, kk], axis=0)

    print('-----iteration---', ii)
    this_log = np.sum(np.log(sum_tau))
    track_log.append(this_log)
    if np.linalg.norm(mu - mu_old) < tol:
        print('Training converged')
        break

    mu_old = mu.copy()

    if ii == maxIter - 1:
        print('Max iteration reached')

num = [i for i in range(0, ii+1)]
plt.clf()
plt.plot(num,track_log, linestyle='-')
plt.title('Log Likelihood over iterations')
plt.savefig('log_likelihood.png')


#print out weights and means
print('Weights')
print(pi)
print('Means')
print(mu)


#reconstruct images using mean data
im = np.dot(np.dot(V, np.diag(np.sqrt(Sig[:d]))), mu[1])
im = im.reshape(28, 28)
flip = np.fliplr(im)
turn = np.rot90(flip)
plt.clf()
plt.imshow(turn, cmap='gray')
plt.savefig('reconstruct_2.png')

im = np.dot(np.dot(V, np.diag(np.sqrt(Sig[:d]))), mu[0])
im = im.reshape(28, 28)
flip = np.fliplr(im)
turn = np.rot90(flip)
plt.clf()
plt.imshow(turn, cmap='gray')
plt.savefig('reconstruct_6.png')
plt.clf()
#covariance heatmaps
#https://stackoverflow.com/questions/39409866/correlation-heatmap
two = sb.heatmap(sigma[0], cmap="Reds", annot=True)
fig = two.get_figure()
fig.savefig("cov_two.jpg") 
fig.clf()
six = sb.heatmap(sigma[1], cmap="Reds", annot=True)
fig = six.get_figure()
fig.savefig("cov_six.jpg") 
fig.clf()
#compute mismatch rate
act = np.array([np.argmax(row) for row in tau])
act = np.where(act == 0, 2, act)
act = np.where(act == 1, 6, act)

rate = 1 - len(act[act != labels])/len(labels)
print('Mismatch Rate: ' + str(rate))


# kmeans
model_kmeans= KMeans(n_clusters=2)
model_kmeans.fit(data)
#get vals
model_preds = model_kmeans.predict(data)
model_centers = model_kmeans.cluster_centers_


kmeans_two= model_centers[0].reshape(28,28)

plt.clf()
flip = np.fliplr(kmeans_two)
turn = np.rot90(flip)
plt.imshow(turn, cmap='gray')
plt.savefig('two_kmeans.png')

kmeans_six = model_centers[1].reshape(28,28)

plt.clf()
flip = np.fliplr(kmeans_six)
turn = np.rot90(flip)
plt.imshow(turn, cmap='gray')
plt.savefig('six_kmeans.png')


#compute mismatch rate
model_preds= np.where(model_preds == 0, 2, model_preds)
model_preds= np.where(model_preds == 1, 6, model_preds)

rate = 1 - len(model_preds[model_preds != labels])/len(labels)
print('Mismatch Rate: ' + str(rate))