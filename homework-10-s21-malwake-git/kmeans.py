from cluster import *
from point import *
#from sklearn.cluster import KMeans

def kmeans(pointdata, clusterdata) :
    #Fill in
    
    #1. Make list of points using makePointList and pointdata
    points = makePointList(pointdata)

    #2. Make list of clusters using createClusters and clusterdata

    clusters = createClusters(clusterdata)
    
    #3. As long as points keep moving:
        #A. Move every point to its closest cluster (use Point.closest and
        #   Point.moveToCluster)
        #   Hint: keep track here whether any point changed clusters by
        #         seeing if any moveToCluster call returns "True"
    check = True
    while(check):
        result = []
        for i in range(len(points)):
            closest = points[i].closest(clusters)
            result.append(points[i].moveToCluster(closest))
            for j in clusters:
                j.updateCenter()
        if not any(result):
            check = False
    #kmeans1 = KMeans(n_clusters=len(clusters)).fit(points)
    #kmeans1.labels_
        
        #B. Update the centers for each cluster (use Cluster.updateCenter)
    
    #4. Return the list of clusters, with the centers in their final positions
    return clusters
    
    
    
if __name__ == '__main__' :
    data = np.array([[0.5, 2.5], [0.3, 4.5], [-0.5, 3], [0, 1.2], [10, -5], [11, -4.5], [8, -3]], dtype=float)
    centers = np.array([[0, 0], [1, 1]], dtype=float)
    
    clusters = kmeans(data, centers)
    for c in clusters :
        c.printAllPoints()
