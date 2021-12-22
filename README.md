# Contest3
That is bonus contest on Algorithms &amp; Data structures course

## Problems
1. Satellite
*  Two stations recorded the transfer from the satellite flying over them consistently, with the first station has recorded only the beginning of transmission, and the second - its end. The recordings are stored in the form of two rows of characters 'a'..'z'.
* It is known that the recorded fragments partially overlap, ie the end of the first segment coincides with the beginning of the second, but the length of overlap is unknown.
* Required to find the maximum possible length of the overlap end of the first fragment with the beginning of the second.
2. Power Strings
* Given two strings a and b we define a*b to be their concatenation.
  For example, if a = "abc" and b = "def" then a*b = "abcdef".
  If we think of concatenation as multiplication, exponentiation by a non-negative integer is defined in the normal way:
* a0 = “” (empty line)
* an+1 = a * an
* For a given string s print the largest n such that s = an for some string a. 
3. The biggest border of the substring
* The border (verge, brink) br of the string S is any proper prefix of this string that is equal to the suffix of S.
* A string S = abaababaabaab has two borders (not empty) - ab and abaab. A string S = abaabaab has two borders - ab and abaab, but the second one is overlapping. A string of length n formed with a repeating character, like aaaaaaaa (or a8), has n-1 borders. For S = a8 the borders are: a, aa, aaa, aaaa, aaaaa, aaaaaa, aaaaaaa.
* The concept of "proper prefix" eliminates the border equals to the string.
* The length of the border is the number of characters in it.
* We make a generalization of the problem. Suppose we want to calculate the values of the largest borders for all substrings of S[1..i] (i = 1..n) and store them in the array br[1..n].
* Find the maximum value of the border in array of the largest borders br for all substrings in S.
4. Maximum palindrome
* Remove from the given line the least number of characters to get a palindrome (the string that reads the same from right to left and from left to right).
5. Преобразование строковых функций
6. Преобразование строковых функций:обратная задача
7. ABB
* Fernando was hired by the University of Waterloo to finish a development project the university started some time ago. Outside the campus, the university wanted to build its representative bungalow street for important foreign visitors and collaborators.
* Currently, the street is built only partially, it begins at the lake shore and continues into the forests, where it currently ends. Fernando’s task is to complete the street at its forest end by building more bungalows there. All existing bungalows stand on one side of the street and the new ones should be built on the same side. The bungalows are of various types and painted in various colors.
* The whole disposition of the street looks a bit chaotic to Fernando. He is afraid that it will look even more chaotic when he adds new bungalows of his own design. To counterbalance the chaos of all bungalow shapes, he wants to add some order to the arrangement by choosing suitable colors for the new bungalows. When the project is finished, the whole sequence of bungalow colors will be symmetric, that is, the sequence of colors is the same when observed from either end of the street.
* Among other questions, Fernando wonders what is the minimum number of new bungalows he needs to build and paint appropriately to complete the project while respecting his self-imposed bungalow color constraint.
8. Square palindrome
* Andrew has just made a breakthrough in computer science: he realized how to quickly find the largest palindrome square on a given rectangle of letters. Can you do the same?
* A square consisting of n rows of n letters each is a palindrome square of size n if each row and each column of this square is a palindrome string. A string is a palindrome string if its first letter is the same as its last letter, its second letter is the same as its next-to-last letter, and so on.