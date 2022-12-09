# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        passes_backstage="Backstage passes to a TAFKAL80ETC concert"
        sulfuras="Sulfuras, Hand of Ragnaros"
        aged_brie="Aged Brie"
        item_names=(passes_backstage,sulfuras,aged_brie)
        
        for item in self.items:

            if item.name not in item_names and item.quality > 0 :
                item.quality = item.quality - 1
            elif item.quality < 50 and item.name==aged_brie or item.name==passes_backstage :
                item.quality = item.quality + 1
                
                if (item.name == passes_backstage and item.sell_in < 11 and item.quality< 50):
                    item.quality = item.quality + 1
                if (item.name == passes_backstage and item.sell_in < 6 and item.quality< 50):
                    item.quality = item.quality + 1

            if item.name != sulfuras:
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0 and item.quality>0 and item.name not in item_names :
                item.quality = item.quality - 1
            elif(item.sell_in < 0 and item.name == passes_backstage):
                item.quality = 0
                
            elif (item.sell_in < 0 and  item.name == aged_brie and item.quality < 50):
                item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
