import rubik

def shortest_path(start, end):
    """
    Using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves. 

    You can use the rubik.quarter_twists move set.
    Each move can be applied using rubik.perm_apply

    """
    parent = {start: None}
    Rparent = {end: None}
    Moves={}
    Frontier=[start]
    RFrontier=[end]
    level=0
    while level<8:
        carry=[]
        Rcarry=[]
        for u in Frontier:
            if u in Rparent:
                return output(u,parent,Rparent)
            else:
                temp=configuration(u)
                for v in temp:
                    if v not in parent:
                        parent[v]=u
                        carry.append(v)
        Frontier=carry
        for u in RFrontier:
            if u in parent:
                return output(u,parent,Rparent)
            else:
                temp=configuration(u)
                for v in temp:
                    if v not in Rparent:
                        Rparent[v]=u
                        Rcarry.append(v)
        RFrontier=Rcarry
        level+=1
    return None


def configuration(node):
    list=[]
    for i in rubik.quarter_twists:
        v=rubik.perm_apply(i,node)
        list.append(v)
    return list

def output(node,parent,Rparent):
    list = []
    temp = node
    while temp is not None:
        for i in rubik.quarter_twists:
            if parent[temp] is not None:
                v=rubik.perm_apply(i,parent[temp])
                if v==temp:
                    list.append(i)
        temp=parent[temp]
    list.reverse()
    Rtemp=node
    while Rparent[Rtemp] is not None:
        for i in rubik.quarter_twists:
            if Rtemp is not None:
                v=rubik.perm_apply(i,Rtemp)
                if v==Rparent[Rtemp]:
                    list.append(i)
        Rtemp=Rparent[Rtemp]
    return list