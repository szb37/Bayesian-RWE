from scipy.stats import beta as beta
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

plt.rcParams.update({'font.family': 'arial'})
sns.set_style("darkgrid")
title_fontdict = {'fontsize': 18, 'fontweight': 'bold'}
axislabel_fontdict = {'fontsize': 16}
legend_fontsize = 14
ticklabel_fontdict = {'fontsize': 14}
tick_labelsize = 14

## Psilodep1 data
a_flat=18
b_flat=4
a_skeptic=18
b_skeptic=6

x_flat = np.linspace(beta.ppf(0, a_flat, b_flat), beta.ppf(1, a_flat, b_flat), 100)
x_skeptic = np.linspace(beta.ppf(0, a_skeptic, b_skeptic),beta.ppf(1, a_skeptic, b_skeptic), 100)
y_flat = beta.pdf(x_flat, a_flat, b_flat)/sum(beta.pdf(x_flat, a_flat, b_flat))
y_skeptic = beta.pdf(x_skeptic, a_skeptic, b_skeptic)/sum(beta.pdf(x_skeptic, a_skeptic, b_skeptic))

fig, ax = plt.subplots(1, 1)
ax.plot(x_flat, y_flat, lw=3, color='blue', alpha=0.6,)
ax.plot(x_skeptic, y_skeptic , lw=3, color='red', alpha=0.6,)
ax.set_title('Psilocybin for TRD', fontdict=title_fontdict)
ax.set_xlim([0, 1])
ax.set_xlabel('Probability of treatment success', fontdict=axislabel_fontdict)
ax.set_ylabel('Posterior probability', fontdict=axislabel_fontdict)
ax.tick_params(axis='both', which='major', labelsize=tick_labelsize)
ax.legend(['Flat prior', 'Sceptical prior'], fontsize=legend_fontsize)
fig.show()


## Epilepsy data
a_flat=21
b_flat=1
a_skeptic=21
b_skeptic=3

x_flat = np.linspace(beta.ppf(0, a_flat, b_flat), beta.ppf(1, a_flat, b_flat), 100)
y_flat = beta.pdf(x_flat, a_flat, b_flat)/sum(beta.pdf(x_flat, a_flat, b_flat))
x_skeptic = np.linspace(beta.ppf(0, a_skeptic, b_skeptic),beta.ppf(1, a_skeptic, b_skeptic), 100)
y_skeptic = beta.pdf(x_skeptic, a_skeptic, b_skeptic)/sum(beta.pdf(x_skeptic, a_skeptic, b_skeptic))

fig, ax = plt.subplots(1, 1)
ax.plot(x_flat, y_flat, lw=3, color='blue', alpha=0.6,)
ax.plot(x_skeptic, y_skeptic , lw=3, color='red', alpha=0.6,)

ax.set_title('Medical cannabis for epilepsy', fontdict=title_fontdict)
ax.set_xlim([0, 1])
ax.set_xlabel('Probability of treatment success', fontdict=axislabel_fontdict)
ax.set_ylabel('Posterior probability', fontdict=axislabel_fontdict)
ax.tick_params(axis='both', which='major', labelsize=tick_labelsize)
ax.legend(['Flat prior', 'Skeptical prior'], fontsize=legend_fontsize)
fig.show()
