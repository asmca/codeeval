import sys

dict1={
        '#':0,
        '_':1,
        'C':2
        }

map1=[]
test_case = open(sys.argv[1],'r')

for test in test_case:
    if '#' not in test:
        continue
    line=[dict1[i]  for i in test.strip() if i in dict1]
    map1.append(line)

test_case.close()    


width,height=len(line),len(map1)

#for i in range(height):
#    print map1[i]

mypath={}

for x in range(height):
    for y in range(width):
        if map1[x][y] >0:
            #x+1 y-1    x+1 y    x+1 y+1
            if x+1 >=height:
                break
            if y-1 >= 0:
                if map1[x+1][y-1]>0:
                    if (x,y) not in mypath:
                        mypath[(x,y)]=[(x+1,y-1)]
                    else:
                        mypath[(x,y)].append((x+1,y-1))
            if y+1<=width:
                if map1[x+1][y+1]>0:
                    if (x,y) not in mypath:
                        mypath[(x,y)]=[(x+1,y+1)]
                    else:
                        mypath[(x,y)].append((x+1,y+1))
            if map1[x+1][y]>0:
                if (x,y) not in mypath:
                    mypath[(x,y)]=[(x+1,y)]
                else:
                    mypath[(x,y)].append((x+1,y))


start=(0,map1[0].index(1))
end=(height-1,map1[height-1].index(1))


find_path(mypath,start,end)



def find_path(graph,start,end,path=[]):
    path=path+[start]
    if start==end:
        return path
    if not graph.has_key(start):
        return None
    for node in graph(start):
        if node not in path:
             newpath = find_path(graph, node, end, path)
             if newpath:
                 return newpath
             return None




