# Hashmap LEFT JOIN
<!-- Short summary or background information -->
The Hashtable LEFT JOIN returns all rows from the left table, even if there are no matches in the right table. This means that if the ON clause matches 0 (zero) records in the right table; the join will still return a row in the result, but with NULL in each column from the right table.

## Challenge
<!-- Description of the challenge -->
Write a function called left join
Arguments: two hash maps
The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
Return: The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
![](left_join.jpg)

## Solution
<!-- Embedded whiteboard image -->

create function that called left join itaccept two hashtable
iterat over each hash to get the key for each value
if the key related of the key in each hash
put the vlaue insid array
terurn the array that contain values