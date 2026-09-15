class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string newString = "";

        int minSizeStr = min(word1.size(), word2.size());
        for (int i = 0; i < minSizeStr; i++)
        {
            newString += word1[i];
            newString += word2[i];
            


        }
        // Now compare strings and see which one is bigger
        // Whichever one is bigger, append from index minSizeStr to
        // string.size()
        if (word1.size() > word2.size())
        {
            for (int i = minSizeStr; i < word1.size(); i++)
            {
                newString += word1[i];
            }

        } else 
        {
            for (int i = minSizeStr; i < word2.size(); i++)
            {
                newString += word2[i];
            }

        }
        return newString;
    }
};