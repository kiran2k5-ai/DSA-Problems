#Group Anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        grp_ana={}

        for i in strs:
            s=''.join(sorted(i))
            if s not in grp_ana:
                grp_ana.update({s:[i]})
            else:
                grp_ana[s].append(i)
        return list(grp_ana.values())
