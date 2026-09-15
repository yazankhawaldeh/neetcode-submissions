class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int mid;
        for (const auto& x : matrix) {
            int low = 0;
            int high = x.size() - 1;
            while (low <= high) {
                mid = (low + high) / 2;
                if (x[mid] == target) return true;
                if (x[mid] > target) {
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            }

        }
        return false;
    }
};
