import random
def getNeighbours(solution,nb_vistided_list):
    neighbours = []
    for i in range(len(solution)):
        for j in range(len(solution)):
            neighbour = solution.copy()
            neighbour[j] = i
            if neighbour != solution and neighbour not in nb_vistided_list:
                neighbours.append(neighbour)
    return neighbours

def best_nb(nbs):
    nb_con = []    
    for i in nbs:
        nb_con.append(fitness(i))
    best_nb_id = np.argmax(nb_con)
    best_nb = nbs[best_nb_id]
    best_nb_con = nb_con[best_nb_id]

    return best_nb, best_nb_con


def fitness(ind):
    conflicts = 0

    for i in range(len(ind)):
        for j in range(len(ind)):
            if i!=j:
                # Check same column conflict
                if ind[i] == ind[j]:
                    conflicts +=1
                
                # Check diagonal conflict 
                if abs(ind[i]-ind[j]) == abs(i-j):
                    conflicts +=1

    return -conflicts

if __name__ == "__main__":
    result_con = []
    result_ite = []
    for i in range(30):
        import numpy as np
        import random
        # primeira vez
        best_nb_list = []
        for i in range(0,30):
            n = random.randint(0,29)
            best_nb_list.append(n)
        best_nb_con = (fitness(best_nb_list))
        n = 1000
        i_count = 0
        # salvar lugares ja visitados para não entrarem na fronteira dnv
        nb_vistided_list = []
        nb_vistided_list.append(best_nb_list)
        # loop
        for i in range(0,n):
            if best_nb_con != 0:
                i_count += 1
                nbs = getNeighbours(best_nb_list,nb_vistided_list)
                best_nb_list,  best_nb_con = best_nb(nbs)
                nb_vistided_list.append(best_nb_list)
                # print(best_nb_list, nbs)
        result_con.append(best_nb_con)
        result_ite.append(i_count)
    
    
        # print(best_nb_list, best_nb_con, i_count)    
    print(result_con)
    print(sum(result_con)/len(result_con))
    print(result_ite)
    print(sum(result_ite)/len(result_ite))
