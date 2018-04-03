|BSAS| Basic Sequential Algorithmic Scheme Python Mudule
========================================================

This project is a python module for the BSAS clustering algorithm. The module bsas contains 4 diffrent 
functions three of them are required to run the algorithm one is optional. 

BSAS
This clustering algorithm sets as a cluster's representative only a single vector (for this implementation 
it is the first vector that triggers the creation of a cluster) and as a result BSAS favors the creation of
compact clusters. Also BSAS will access data only once so with every iteration over theta range it measures 
the distance between a vector and all the clusters (their representatives) created until that moment and if 
the minimum distance of them all is bigger than the theta threshold creates a new cluster with is as the 
represensative.

load_data(f_name, destination='', delimiter=','):
This is a required function and it's the one that loads the data from a csv file giving its name as 
f_name, the path of the file as destination (etc directory1/directory2/) and choosing its delimeter with 
preselcted the comma character ','. The data gets shuffled using numpy's shuffle function, that happens 
because we want to have results that aren't affected by the sequence of the data.

theta_predictions(d_min, d_max):
Is the optional function provided by the bsas module and its only use is to provide a good hypothesis about
the theta_min and theta_max limits that we will use later. Using the minimun(d_min) and the maximum(d_max) 
distance between vectors for the dataset we can find the theoritical upper and lower limits, theta_min and 
theta_max that we will use later.

theta_range_calc(theta_min, theta_max, theta_step):
Given theta_min, theta_max and theta_step this function will calculate the range for the iterations that we 
will need later for the main function that runs the BSAS algorithm.

cluster_vectors(f_name, theta_min, theta_max, theta_step, out_file, destination='',  delimiter=',', q=-1, precision=2):
This function calls both load_data and theta_range_calc inside its body. This function includes all the
theory behind BSAS and with the right algorithmic steps exports a csv file(out_file) with the results, 
the csv file gets saved in the destination folder same as the input csv. Except from the first 4 variables 
that are needed to call load_data and theta_range_calc user can set if he wants to stop the algorithm when 
it reaches a certain amount q of clusters, also he can define the name of the output file its delimeter with 
comma as preselected and the precision of the theta_value to output.

[Reference](<http://users.utcluj.ro/~ancac/Resurse/labPRS/L13_Clustering/lab_13e_clustering.pdf>) 
Sergios Theodoridis,Konstantinos Koutroumpas: Pattern Recognition