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


def test_left_join_hash():
  ht_one = HashTable()
  ht_one.add("fond", "enamored")
  ht_one.add("wrath", "anger")
  ht_one.add("diligent", "employed")
  ht_one.add("outfit", "garb")
  ht_one.add("guide", "usher")
  ht_two = HashTable()
  ht_two.add("fond", "averse")
  ht_two.add("wrath", "delight")
  ht_two.add("diligent", "idle")
  ht_two.add("guide", "follow")
  ht_two.add("flow", "jam")
  assert (left_join_hash(ht_one,ht_two)) == [['fond', 'enamored', 'averse'], ['guide', 'usher', 'follow'], ['wrath', 'anger', 'delight'], ['outfit', 'garb', None], ['diligent', 'employed', 'idle'], ['flow', None, 'jam']]

