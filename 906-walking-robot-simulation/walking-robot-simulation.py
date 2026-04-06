class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        cp=[0,0]
        m=0
        origin=[-10**5,-10**5]
        def hp(CP):
            c=CP[0]-origin[0]
            c+=CP[1]*(2*10**5)-origin[1]
            return c
        ho=set()
        for e in obstacles:
            ho.add(hp(e))    
        dr="NESW"
        fd='N'
        def np(CP,FD,S):
            NP=CP.copy()
            if FD in 'NS':
                inc=1
                if FD=='S':
                    inc=-1
                for i in range(S):
                    if hp([NP[0],NP[1]+inc]) in ho:
                        return NP 
                    NP[1]+=inc    
            else: 
                inc=1
                if FD=='W':
                    inc=-1
                for i in range(S):
                    if hp([NP[0]+inc,NP[1]]) in ho:
                        return NP
                    NP[0]+=inc      
            return NP                                 
        for i in range(len(commands)):
            if commands[i]==-1:
                fd=dr[(dr.find(fd)+1)%4]
            elif commands[i]==-2:    
                fd=dr[(dr.find(fd)+3)%4]
            else:
                cp=np(cp,fd,commands[i])
                m=max(m,cp[0]**2+cp[1]**2) 
        return m      
                   