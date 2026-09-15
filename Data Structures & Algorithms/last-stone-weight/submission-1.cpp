class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        // we include a std::priority_queue for our data structure
        std::priority_queue<int> heap(stones.begin(), stones.end());
        while (heap.size() > 1)
        {
            if (heap.size() == 2)
            {
                int stone = heap.top();
                heap.pop();
                int stone2 = heap.top();
                return stone - stone2;
                

                
            }
            int oogabooga1 = heap.top();
            heap.pop();
            int oogabooga2 = heap.top();
            heap.pop();
            int newstone = oogabooga1 - oogabooga2;
            if (newstone > 0)
            {
                heap.push(newstone);
            }
        }
        return heap.top();


        

        
    }
};
