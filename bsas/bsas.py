import numpy as np

mC = []  # List of representative vectors
results = []  # List of number of clusters per iteration


def load_data(f_name, delimiter=','):
    data = np.genfromtxt(f_name+'.csv', delimiter=delimiter)  # Initialize array with data
    np.random.shuffle(data)  # Shuffle data
    return data


def theta_predictions(d_min, d_max):
    theta_min = d_min + 0.25*(d_max - d_min)
    theta_max = d_min + 0.75*(d_max - d_min)
    print("Theta min prediction: " + str(theta_min))
    print("Theta max prediction: " + str(theta_max))


def theta_range_calc(theta_min, theta_max, theta_step):
    theta_range = np.arange(theta_min, theta_max, theta_step)
    return theta_range


def cluster_vectors(f_name, theta_min, theta_max, theta_step, q=-1, out_file, delimiter=",", precision=2):

    data = load_data(f_name=f_name, delimiter=delimiter)
    theta_range = theta_range_calc(theta_min=theta_min, theta_max=theta_max, theta_step=theta_step)

    n = data.shape[0]  # Number of vectors to cluster

    for Theta in theta_range:
        m = 1  # number of clusters(initialized with 1 for the first vector)
        mC[:] = []  # Init/clear mC list
        mC.append(data[0])  # Initialization of cluster 1 with the first vector

        # Cluster the rest of the vectors
        for i in range(1, n):
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
                if (distance_min > Theta) and (m < q):  # q maximum number of clusters (-1 indicates no limit)
                    m = m + 1  # Create new cluster
                    mC.append(data[i])  # Set the vector as the representative of the new cluster

        results.append(m)  # Add number of clusters for the current iteration
    output = np.column_stack((theta_range, results))
    np.savetxt(out_file+".csv", output, delimiter=delimiter, fmt='%.'+str(precision)+'f')