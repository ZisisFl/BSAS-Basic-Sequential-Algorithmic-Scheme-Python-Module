import numpy as np

mC = []  # List of representative vectors
results = []  # List of number of clusters per iteration
m = 1  # number of cluster(initialized with 1 for the first vector)
q = -1  # maximum number of clusters (-1 indicates no limit)


def load_data(f_name, delimiter):  # file name variable for delimiter
    data = np.genfromtxt(f_name+'.csv', delimiter=delimiter)  # Initialize array with data
    np.random.shuffle(data)  # Shuffle data
    N = data.shape[0]  # Number of vectors to cluster


def theta_predictions(d_min, d_max):
    theta_min = d_min + 0.25*(d_max - d_min)
    theta_max = d_min + 0.75*(d_max - d_min)


def theta_range(theta_min, theta_max, theta_step):
    theta_range = np.arange(theta_min, theta_max, theta_step)
    return theta_range


def cluster_vectors(theta_range, q, out_file, delimiter, precision):
    for Theta in theta_range:
        mC[:] = []  # Init/clear mC list
        mC.append(data[0])  # Initialization of cluster 1 with the first vector

        # Cluster the rest of the vectors
        for i in range(1, N):
            distance_min = np.linalg.norm(mC[0]-data[i])  # Find minimum distance between vector and clusters
            for k in range(1, m):
                distance = np.linalg.norm(mC[k]-data[i])
                if (distance_min > distance):
                    distance_min = distance

            if (q == -1):
                if (distance_min > Theta):  # If minimum distance is less than the threshold
                    m = m + 1  # Create new cluster
                    mC.append(data[i])  # Set the vector as the representative of the new cluster
            else:
                if (distance_min > Theta) and (m < q):  # If minimum distance is less than the threshold and number of cluster inside limit
                    m = m + 1  # Create new cluster
                    mC.append(data[i])  # Set the vector as the representative of the new cluster

        results.append(m)  # Add number of clusters for the current iteration
    output = np.column_stack((theta_range, results))
    np.savetxt(out_file+".csv", output, delimiter=delimiter, fmt='%.'+precision+'f')