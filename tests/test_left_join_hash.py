from data_structure.hashmap_left_join.hashmap_left_join import left_join_hash , HashTable

def test_join():
    hash_one = HashTable()
    hash_one.add("1", "1")
    hash_one.add("2", "1")
    hash_one.add("3", "1")
    hash_one.add("4", "1")
    hash_one.add("5", "1")

    hash_two = HashTable()
    hash_two.add("1", "1")
    hash_two.add("2", "1")
    hash_two.add("3", "1")
    hash_two.add("4", "1")
    hash_two.add("5", "1")

    expected = [['1', '1', '1'], ['2', '1', '1'], ['3', '1', '1'], ['4', '1', '1'], ['5', '1', '1']]
    actual = left_join_hash(hash_one, hash_two)

    assert actual == expected