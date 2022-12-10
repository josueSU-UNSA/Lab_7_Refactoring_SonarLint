# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def __increase_quality_backstage(self,item,passes_backstage):
        if (item.name == passes_backstage and item.sell_in < 11 and item.quality< 50):
            item.quality = item.quality + 1
        if (item.name == passes_backstage and item.sell_in < 6 and item.quality< 50):
            item.quality = item.quality + 1

    def __decrease_sell_in_no_sulfuras(self,item,sulfuras):
        if item.name != sulfuras:
            item.sell_in = item.sell_in - 1

    def __lead_conjured_items(self,item,conjured):
        if item.name == conjured and 0<item.sell_in<150:
           
            item.sell_in = item.sell_in - 1
            item.quality=item.quality-2
            return True
        elif(item.sell_in<0):
            item.sell_in=item.sell_in-1
            item.quality=item.quality-4
            return True
        else :
            return False
            
    def __is_passes_or_aged_brie(self,item,aged_brie,passes_backstage):
        return item.name==aged_brie or item.name==passes_backstage

    def update_quality(self):
        passes_backstage="Backstage passes to a TAFKAL80ETC concert"
        sulfuras="Sulfuras, Hand of Ragnaros"
        aged_brie="Aged Brie"
        conjureds="Conjured item"
        
        item_names=(passes_backstage,sulfuras,aged_brie)
        
        for item in self.items:

            if self.__lead_conjured_items(item,conjureds):
                continue

            if  item.name not in item_names and item.quality > 0:
                item.quality = item.quality - 1
            elif item.quality < 50 and self.__is_passes_or_aged_brie(item,aged_brie,passes_backstage) :
                item.quality = item.quality + 1
                
                
                self.__increase_quality_backstage(item,passes_backstage)


            self.__decrease_sell_in_no_sulfuras(item,sulfuras)

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
