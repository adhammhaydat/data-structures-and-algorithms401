# Hashtables
<!-- Short summary or background information -->

In computing, a hash table (hash map) is a data structure that implements an associative array abstract data type, a structure that can map keys to values.

## pull req:

https://github.com/adhammhaydat/data-structures-and-algorithms401/pull/3

## Challenge
<!-- Description of the challenge -->

create Branch Name: hashtable

Implement a Hashtable Class with the following methods:
that contane these methods: 
1. hash
2. get 
3. add
4. contain


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
The Big o:
1. time : O(1)
2. space : O(1)

## API
<!-- Description of each method publicly available in each of your hashtable -->
* add

    Arguments: key, value
    Returns: nothing
    This method should hash the key, and add the key and value pair to the table, handling collisions as needed.

* get
    Arguments: key
    Returns: Value associated with that key in the table

* contains
    Arguments: key
    Returns: Boolean, indicating if the key exists in the table already.

* hash
    Arguments: key
    Returns: Index in the collection for that key
