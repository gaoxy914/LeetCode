# LeetCode

## Manacher Algorithm
calculate the longest palindrome substring

- preprocessing<br>
insert '#' between adjacent characters in the string, e.g.,
babad $\rightarrow$ #b#a#b#a#d#<br>
**remark**: after preprocessing, the length of the string after
and the length of the palindrome substring is odd.

- array $P$<br>
$P[i]$ : The maximum extension length of the palindrome substring centered on the i-th character.<br>
**remark**: $P[i]$ is the length of the palindrome substring centered on the i-th caracter of the original string.<br>
For example: abbabb

char|#|a|#|b|#|b|#|a|#|b|#|b|#
--|--|--|--|--|--|--|--|--|--|--|--|--|--
index|0|1|2|3|4|5|6|7|8|9|10|11|12
$P$|0|1|0|1|4|1|0|5|0|1|2|1|0

- calculate $P$ with previous information.<br>
maxRight: $maxRight = \max\{x + P[x] \mid 0 \le x < i\}$.<br>
center: $center = \arg\max\{x + P[x]\mid 0\le x<i\}$.
   * case 1 $i > maxRight$<br>
   extend at the i-th character to enlarge maxRight.
   * case 2 $i < maxRight$<br>
   $(mirror + i) / 2 = center$
      * $P[mirror] < maxRight - i$, which means that $P[i] = P[mirror]$.<br>
      ![avatar](https://github.com/gaoxy914/LeetCode/blob/master/images/manacher1.png)
      * $P[mirror] == maxRight - i$, which means that $P[i]$ is at least $maxRight - i$ and may be extended.<br>
      ![avatar](https://github.com/gaoxy914/Leetcode/blob/master/images/manacher2.png)
      * $P[mirror] > maxRight - i$, which means that $P[i] = maxRight - i$ and can not be extended.<br>
      ![avatar](https://github.com/gaoxy914/Leetcode/blob/master/images/manacher3.png)



In summary, $P[i] = \min\{maxRight - i, P[mirror]\}$
