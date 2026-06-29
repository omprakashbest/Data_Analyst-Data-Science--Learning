"""
-> Account Merge 

Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0]
is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some 
common email to both accounts. Note that even if two accounts have the same name, they may belong to different 
people as people could have the same name. A person can have any number of accounts initially, but all of their 
accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is 
the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in 
any order.

"""

from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1]*n

    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        uf = UnionFind(len(accounts))

        emailToAcc = {} # email -> index of acc

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToAcc:
                    uf.union(i, emailToAcc)
                else:
                    emailToAcc[e] = i
        emailGroup = defaultdict(list) # index of acc -> list of emails

        for e, i in emailToAcc.items():
            leader = uf.find(i)
            emailGroup[leader].append(e)
        
        res = []
        for i, emails in emailGroup:
            name = accounts[i][0]
            res.append([name] + sorted(emailGroup[i])) # array concat
        return res