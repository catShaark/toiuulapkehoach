
def read(path): 
    input_path = "./Dataset/" + path

    with open(input_path, "r") as f:
        lines = f.read().splitlines()
    N, M, K = lines[0].strip().split()
    N = int(N)
    M = int(M)
    K = int(K)

    a,b,c,d,e,f = lines[1].strip().split()
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    e = int(e)
    f = int(f)

    s = []
    for i in range(2, N+2):
        s_tmps = lines[i].strip().split()
        s_tmp = []
        for i in s_tmps:
            s_tmp.append(int(i))
        s.append(s_tmp)
    
    g = []
    for i in range(N+2, 2*N+2):
        g_tmps = lines[i].strip().split()
        g_tmp = []
        for i in g_tmps:
            g_tmp.append(int(i))
        g.append(g_tmp)

    t = []
    t_tmp = lines[2*N+2].strip().split()
    for i in t_tmp:
        t.append(int(i))
    
    path_out = path.replace("input", "output")
    path_output = "./GA/Output/" + path_out
    return path_output,N,M,K,t,s,g,a,b,c,d,e,f
