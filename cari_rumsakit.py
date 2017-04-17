 
map =  {'A':set(['RS1','C','E']),
         'B':set(['E','D']),
         'C':set(['A','B','RS2']),
         'D':set(['B','F','K','RS3']),
         'E':set(['A','B']),
         'F':set(['D','G']),
         'G':set(['H','F','I']),
         'H':set(['G']),
         'I':set(['G','J']),
         'J':set(['I']),
         'K':set(['D','L','M']),
         'L':set(['RS2','K']),
         'M':set(['K']),
         'RS1':set(['A']),
         'RS2':set(['C','L']),
         'RS3':set(['D'])}
    

def bfs(graf, mulai):
    queue = [[mulai]]
    tujuan1 = 'RS1'
    tujuan2 = 'RS2'
    tujuan3 = 'RS3'
    visited = set()

    while queue:     
        jalur = queue.pop(0)
        state = jalur[-1]
        if state == tujuan1:
            return jalur
        elif state == tujuan2:
            return jalur
        elif state == tujuan3:
            return jalur
        elif state not in visited:
            for cabang in graf.get(state, []): 
                jalur_baru = list(jalur) 
                jalur_baru.append(cabang) 
                queue.append(jalur_baru) 

            visited.add(state)

        isi = len(queue)
        if isi == 0:
            print("Tidak ditemukan")

def dfs(graf, mulai):
    stack = [[mulai]]
    tujuan1 = 'RS1'
    tujuan2 = 'RS2'
    tujuan3 = 'RS3'
    visited = set()

    while stack:     
        jalur = stack.pop(-1)
        state = jalur[-1]
        if state == tujuan1:
            return jalur
        elif state == tujuan2:
            return jalur
        elif state == tujuan3:
            return jalur
        elif state not in visited:
            for cabang in graf.get(state, []): 
                jalur_baru = list(jalur) 
                jalur_baru.append(cabang) 
                stack.append(jalur_baru) 

            visited.add(state)

        isi = len(stack)
        if isi == 0:
            print("Tidak ditemukan")
