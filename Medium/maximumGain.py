# 1717. Maximum Score From Removing Substrings

# You are given a string s and two integers x and y. You can perform two types of operations any number of times.

# Remove substring "ab" and gain x points.
# For example, when removing "ab" from "cabxbae" it becomes "cxbae".
# Remove substring "ba" and gain y points.
# For example, when removing "ba" from "cabxbae" it becomes "cabxe".
# Return the maximum points you can gain after applying the above operations on s.

 

# Example 1:

# Input: s = "cdbcbbaaabab", x = 4, y = 5
# Output: 19
# Explanation:
# - Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
# - Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
# - Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
# - Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
# Total score = 5 + 4 + 5 + 5 = 19.
# Example 2:

# Input: s = "aabbaaxybbaabb", x = 5, y = 4
# Output: 20
 

# Constraints:

# 1 <= s.length <= 105
# 1 <= x, y <= 104
# s consists of lowercase English letters.

def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_substring(s: str, first: str, second: str, score: int) -> (str, int):
            stack = []
            points = 0
            for ch in s:
                if stack and stack[-1] == first and ch == second:
                    stack.pop()
                    points += score #
                else:
                    stack.append(ch)
            return ''.join(stack), points

        if x > y:  #If we remove low-score pairs first, we might lose chances to remove high-score pairs later. (Greedy)
            # Remove "ab" first
            s, score1 = remove_substring(s, 'a', 'b', x)
            s, score2 = remove_substring(s, 'b', 'a', y)
        else:
            # Remove "ba" first
            s, score1 = remove_substring(s, 'b', 'a', y)
            s, score2 = remove_substring(s, 'a', 'b', x)

        return score1 + score2