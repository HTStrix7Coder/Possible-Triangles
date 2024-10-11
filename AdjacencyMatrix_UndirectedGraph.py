#function for printing the matrix
def printmatrix(matrix):
    r,c=len(matrix),len(matrix[0]) #intializing the rows and columns
    for i in range(r):
        for j in range(c):
            print(matrix[i][j],end="\t")
        print()
#code for undirected graph
count = 0
v,e = map(int,input().split()) #inputing the vertices and edges of the graph
matrix = [[0]*v for i in range(v)] #generating a matrix of V^2
degrees = [0]*v  # Initialize a list to store the degrees of each node
for i in range(e):
    u,v = map(str,input().split())
    u = ord(u) - ord('A') #subtract the ASCII value of the Characters to get the index value for matrix operation
    v = ord(v) - ord('A')
    matrix[u][v] = 1 #setting value 1 for where edges are present
    matrix[u][v] = 1 #since the graph is undirected we have to set this also
    degrees[u] += 1  # Increment the degree of node u
    degrees[v] += 1  # Increment the degree of node v
    count=count+1
# Calculate the number of triangles
#iterating through all possible triplets of a node and if three nodes are connected they form a triangle
triangles = 0
for i in range(v):
    for j in range(i + 1, v):
        for k in range(j + 1, v):
            if matrix[i][j] == 1 and matrix[j][k] == 1 and matrix[k][i] == 1:
                triangles += 1
print("Degree of each node",degrees)
print("Number of edges",count)
print("Number of Triangles",triangles)
printmatrix(matrix) #here the printing matrix function is called by passing the parameter 'matrix'
