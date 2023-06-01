#!/usr/bin/python3

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Time
        # Space

        # if len(strs) == 1:
        #     return [strs]

        # # Create list of hashmap
        # map_list = [{} for x in strs]
        # for index, str in enumerate(strs):
        #     for char in str:
        #         map_list[index][char] = 1 + map_list[index].get(char, 0)
        # print(map_list[index])

        # Compare list of hashmap for duplicate value
        
        ##### REVISIT ######
        
        # Time: O(mn) m is length of strs and n is the average length of str
        # Space: O(mn)
        #  Ref: https://youtu.be/vzdNOK2oB2E
        if len(strs) == 1:
            return [strs]
        
        output = defaultdict(list)
        for str in strs:
            count = [0] * 26
            
            for char in str:
                count[ord(char) - ord("a")] += 1
            
            output[tuple(count)].append(str)
            
        return output.values()
