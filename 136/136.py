import sys


def find_path(graph,start,end,path=[]):
    path=path+[start]
    if start==end:
        return path
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if node not in path:
             newpath = find_path(graph, node, end, path)
             if newpath:
                 return newpath
             return None


dict1={
        '#':0,
        '_':1,
        'C':2
        }

map1,map0=[],[]
test_case = open(sys.argv[1],'r')

for test in test_case:
    if '#' not in test:
        continue
    map0.append(test.strip())
    line=[dict1[i]  for i in test.strip() if i in dict1]
    map1.append(line)

test_case.close()


width,height=len(line),len(map1)


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


#following sort follows the requirement C>_
for i in mypath:
    mypath[i]=sorted(mypath[i],cmp=lambda x,y: cmp(map1[x[0]][x[1]], map1[y[0]][y[1]]),reverse=True)


final_way=find_path(mypath,start,end)

for i in final_way:
    x,y=i[0],i[1]
    if x==0:
        map0[x]=map0[x][:y]+'|'+map0[x][y+1:]
    else:
        last=final_way[final_way.index(i)-1]
        if y>last[1]:
            map0[x]=map0[x][:y]+'\\'+map0[x][y+1:]
        elif y<last[1]:
            map0[x]=map0[x][:y]+'/'+map0[x][y+1:]
        else:
            map0[x]=map0[x][:y]+'|'+map0[x][y+1:]


print '\n'.join(w for w in map0)


