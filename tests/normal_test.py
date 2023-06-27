from tests.settings import *

# create tests for normal items here...
def test_normal_over_50():
    item = Item("normal", -10, 50)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == -11
    assert item.quality == 48
def test_normal_item_degradation():
    item = Item("apple", 10, 20)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    gilded_rose.update_quality()
    assert item.sell_in == 8
    assert item.quality == 18
def test_normal_item_zero():
    item = Item("apple", 0, 50)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    gilded_rose.update_quality()
    assert item.sell_in == -2
    assert item.quality == 46
def test_normal_item_negative():
    item = Item("apple", -10, 0)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    gilded_rose.update_quality()
    assert item.sell_in == -12
    assert item.quality == 0

#AGED BRIE

def test_aged_brie():
    item = Item("Aged Brie", 4, 10)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 3
    assert item.quality == 11

def test_aged_brie_quality_over_50():
    item = Item("Aged Brie", 4, 50)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 3
    assert item.quality == 50

def test_sulfuras():
    item = Item("Sulfuras, Hand of Ragnaros", 0, 80)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 0
    assert item.quality == 80

# Backstage Passes
def test_backstage_quality_drop():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 30)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == -1
    assert item.quality == 0

def test_backstage_increase_by_1():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 30, 0)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 29
    assert item.quality == 1

def test_backstage_increase_by_2():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 0)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 5
    assert item.quality == 2

def test_backstage_increase_by_3():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 0)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 4
    assert item.quality == 3

def test_backstage_increase_by_3_more():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 0)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 0
    assert item.quality == 3