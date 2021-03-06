from attr import has
from data_structure.hashtable.hashtable import HashTable
import pytest

@pytest.fixture
def hashtable():
	return HashTable()

def test_hash(hashtable):
	expected = 700
	actual = hashtable._HashTable__hash("d")
	assert actual == expected

def test_hash_word(hashtable):
	expected = 376
	actual =  hashtable._HashTable__hash("dd")
	assert actual == expected

"""
"a"
ord("d") = 100
100 * 7 = 700
700 % 1024 = 700

-----------------
"dd"
200
200 * 7 = 1400
1400 % 1024 = 376
""" 

def test_add():
  pass
def test_contain():
	expected = True
	hashtable= HashTable()
	hashtable.add("dd","adham")

	actual = hashtable.contains("dd")

	assert actual == expected
