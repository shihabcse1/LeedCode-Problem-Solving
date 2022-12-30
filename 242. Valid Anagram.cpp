class Solution {
public:
    // Problem Link: https://leetcode.com/problems/valid-anagram/
    // Time Complexity: 0(n)
    // Space Complexity: 0(1)
    bool isAnagram(string s, string t) {
        int word_count1[26] = {0};
        int word_count2[26] = {0};

        int str1_length = s.length();
        int str2_length = t.length();
        int index = 0;

        if(str1_length != str2_length) {
            return false;
        }

        for(int i = 0; i < str1_length; i++) {
            index = s[i] - 'a';
            word_count1[index]++;
        }

        for(int i = 0; i < str2_length; i++) {
            index = t[i] - 'a';
            word_count2[index]++;
        }

        for(int i = 0; i < 26; i++) {
            if(word_count1[i] != word_count2[i]) {
                return false;
            }
        }

        return true;
        
    }
};