class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> seen;
        for (const auto& x: nums)
        {
            if (!seen.contains(x))
            {
                seen.insert(x);
            }
            else {
                return true;
            }
        }
        return false;
        
    }
};