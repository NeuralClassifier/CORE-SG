# CORE-SG: Efficient Computation of Multiple MSTs for Density-Based Methods
Authors: Antonio Cavalcante Araujo Neto, Murilo Coelho Naldi, Ricardo J. G. B. Campello, and Jörg Sander

Published in ICDE'2022

## Abstract
Several popular density-based methods for unsupervised and semi-supervised learning tasks, including clustering and classification, can be formulated as instances of a framework that is based on the processing of a minimum spanning tree of the data, where the edge weights correspond to a form of (unnormalized) density estimate w.r.t. a smoothing parameter mpts. While density-based methods are considered to be robust w.r.t. mpts in the sense that small changes in its value usually lead to slight or no changes in the resulting structure, wider ranges of mpts values may lead to different results that a user would like to analyze before choosing the most suitable value for a given data set or application. However, to explore multiple results for a range of mpts values, until recently, one had to re-run the density-based method for each value in the range independently, which is computationally inefficient. This paper proposes a new computationally efficient approach to compute multiple densitybased minimum spanning trees w.r.t. a set of mpts values by leveraging a graph obtained from a single run of the densitybased algorithm, without the need for re-runs of the original algorithm. We present theoretical and experimental results that show that our approach overcomes the drawbacks of the previous state-of-the-art, and it is considerably superior in runtime and graph size while being easier to implement. Our experimental evaluation using synthetic and real data shows that our strategy can lead to speed-up factors of hundreds to thousands of times on the computation of density-based minimum spanning trees.


Paper Link: **LINK** 

## Content

This repository contains the source code and real-life datasets.

  * `CORE-SG.py`: This python file gives only the source code for CORE-SG.
  * `CORE-SG_implement.py`: This script implements the CORE-SG on real-life datasets.
  * `df_to_consider`: This folder has eight different real-life datasets to test CORE-SG.
  
# Instructions
The program is written in Python 3.8:
* Using conda:
```
conda install -c conda-forge jupyterlab
```
* or using pip:
```
pip install jupyterlab
```
## Dependencies
The program requires the following Python libraries:
* scikit-learn v1.0.1
* pandas v1.3.4
* scipy v1.7.3

# Contributors

* Kushankur Ghosh, [kushanku@ualberta.ca](mailto:kushanku@ualberta.ca)

