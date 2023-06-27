# -*- coding: utf-8 -*-

class ItemTypes:
    BRIE = "Aged Brie"
    SULF = "Sulfuras, Hand of Ragnaros"
    BACK = "Backstage passes to a TAFKAL80ETC concert"


def update_normal(item):
    if item.quality > 0:
        item.quality = item.quality - 1
    item.sell_in = item.sell_in - 1
    if item.sell_in < 0:
        if item.quality > 0:
            item.quality = item.quality - 1


def update_brie(item):
    if item.quality < 50:
        item.quality = item.quality + 1
    item.sell_in = item.sell_in - 1
    if item.sell_in < 0:
        if item.quality < 50:
            item.quality = item.quality + 1


def update_backstage(item):
    if item.quality < 50:
        item.quality = item.quality + 1
        if item.sell_in < 11:
            if item.quality < 50:
                item.quality = item.quality + 1
        if item.sell_in < 6:
            if item.quality < 50:
                item.quality = item.quality + 1
    item.sell_in = item.sell_in - 1
    if item.sell_in < 0:
        item.quality = item.quality - item.quality
def update_sulfuras(item):
    pass


class GildedRose(object):

    def __init__(self, items):
        self.items = items



    def update_quality(self):
        for item in self.items:
            match item.name:
                case ItemTypes.BRIE:
                    update_brie(item)
                    continue
                case ItemTypes.BACK:
                    update_backstage(item)
                    continue
                case ItemTypes.SULF:
                    update_sulfuras(item)
                    continue
                case _:
                    update_normal(item)
                    continue


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
