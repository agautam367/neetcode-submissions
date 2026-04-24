class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1={}
        dic2={}
        counter=0
        if len(s)!=len(t):
            return False
        for i in s:
            if i not in dic1:
                dic1[i]=1
            else:
                dic1[i]+=1
        for j in t:
            if j not in dic2:
                dic2[j]=1
            else:
                dic2[j]+=1
        print(dic1, dic2)
        for i in dic1.keys():
            if i not in dic2:
                return False
            else:
                if dic1[i]==dic2[i]:
                    counter+=1
            
        if counter==len(dic1):
            return True
        else:
            return False
                    
                

