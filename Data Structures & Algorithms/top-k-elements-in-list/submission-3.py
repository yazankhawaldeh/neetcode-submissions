class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = {}
        final = []
        for i in nums: # sorting for frequency into hash map
            if i not in frequent:
                frequent[i] = 1
            elif i in frequent:
                frequent[i] += 1
        sorted_data_desc = dict(sorted(frequent.items(), key=lambda item: item[1], reverse=True))
        for key in sorted_data_desc:
            if len(final) == k:
                break
            final.append(key)
        return final

        # my_dict.values() returns values in key
        # my_dict alone retrusn the key. We need to return the key based on value since value
        # holds frequency
        