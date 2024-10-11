#code for directed graph
for i in range(e):
    u,v,w = map(str,input(),split()) #we are also inputting the weight
    u=ord(u)-ord('A')
    v=ord(v)-ord('A')
    w=int(w) 
    matrix[u][v] = w # here we are taking in weight instead of 1
printmatrix(matrix)
