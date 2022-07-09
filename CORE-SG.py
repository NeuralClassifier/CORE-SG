#!/usr/bin/env python
# coding: utf-8




import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
import sklearn
from scipy.sparse.csgraph import minimum_spanning_tree
import time



class CORE_SG():
    
    def __init__(self, df,max_mpts):
        self.df = df
        self.K = max_mpts #minimum can be 2
        self.kmax_NearestNeighbourG = None
        self.pairwise_distances = None
        self.MutualReachabilityG_kmax = None
        self.MinSpanningTree_kmax = None
        self.nearest_neighbors = None
        self.kmax_DistWeightdNearestNeighbourG = None
        self.kmax_MRDWeightdNearestNeighbourG = None
        self.core_sg = None
    
    def k_max_NNG(self):
        dist = {}
        euclidean_pairwise_dist = sklearn.metrics.pairwise.euclidean_distances(self.df.iloc[:,:-1], Y=None)
        self.pairwise_distances = euclidean_pairwise_dist
        kmax_NNG = np.zeros(euclidean_pairwise_dist.shape)
        kmax_NNG_mrd = np.zeros(euclidean_pairwise_dist.shape)
        core_dist = []
        nearest_negh = []

        for can in range(len(euclidean_pairwise_dist)):
            candidate = euclidean_pairwise_dist[can]
            neighbors = sorted(range(len(candidate)), key = lambda sub: candidate[sub])[:self.K]
        
            nearest_negh.append(np.array(neighbors[1:]))
            
            for nn in neighbors:
                if can!=nn:
                    kmax_NNG[can,nn] = 1

                    
        
        self.nearest_neighbors = np.array(nearest_negh)
        self.kmax_NearestNeighbourG = kmax_NNG
        self.create_dist_weighted_kmax_NNG()
        
        for can in range(kmax_NNG.shape[0]):
            for nn in range(kmax_NNG.shape[1]):
                if kmax_NNG[can,nn] == 1:
                    kmax_NNG_mrd[can,nn]=max(self.find_core_distance(can,self.K),self.find_core_distance(nn,self.K))
        
        self.kmax_MRDWeightdNearestNeighbourG = kmax_NNG_mrd

    
    def find_core_distance(self,idx,mpts):
        return self.pairwise_distances[idx,self.nearest_neighbors[idx,mpts-2]]

    def mutual_reachability_distance(self,idx1,idx2,mpts):
        
        return max(self.find_core_distance(idx1,mpts),self.find_core_distance(idx2,mpts),self.pairwise_distances[idx1,idx2])

    def G_kmax(self):
        g_kmx = np.zeros(self.pairwise_distances.shape)
        for inst1 in range(self.pairwise_distances.shape[0]):
            for inst2 in range(self.pairwise_distances.shape[0]):
                if inst1 != inst2:
                    mrd_kmx = self.mutual_reachability_distance(inst1,inst2,self.K)
                else:
                    mrd_kmx = 0
                g_kmx[inst1,inst2] = mrd_kmx
        
        self.MutualReachabilityG_kmax = g_kmx
        mst_kmax = minimum_spanning_tree(g_kmx)
        self.MinSpanningTree_kmax=mst_kmax.toarray().astype(float) #Kruskal Algorithm
        
        
    def create_dist_weighted_kmax_NNG(self):
        weightedkmax_NNG = np.zeros(self.kmax_NearestNeighbourG.shape)
        for row in range(self.kmax_NearestNeighbourG.shape[0]):
            for col in range(self.kmax_NearestNeighbourG.shape[1]):
                if self.kmax_NearestNeighbourG[row,col] == 1:
                    weightedkmax_NNG[row,col] = max(self.find_core_distance(row,self.K),self.find_core_distance(col,self.K))
        
        self.kmax_DistWeightdNearestNeighbourG = weightedkmax_NNG    
    
    
    def union(self):
        self.core_sg = self.kmax_MRDWeightdNearestNeighbourG
        for row in range(self.MinSpanningTree_kmax.shape[0]):
            for col in range(self.MinSpanningTree_kmax.shape[1]):
                if self.MinSpanningTree_kmax[row,col] != 0:
                    if self.core_sg[row,col] == 0:
                        ## Combining MST
                        self.core_sg[row,col] = self.MinSpanningTree_kmax[row,col]
        
    
    
    def compute_core_sg(self):
        start_time = time.time()
        self.k_max_NNG()
        self.G_kmax()
        self.union()
        print("--- %s seconds ---" % (time.time() - start_time))