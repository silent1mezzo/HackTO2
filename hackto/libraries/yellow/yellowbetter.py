from yellowapi import *
import json
import random

class YellowBetterAPI(YellowAPI):
    def __init__(self, api_key, where, uid, test_mode=True, format='JSON', handlers=[]):
        super(YellowBetterAPI, self).__init__(api_key, test_mode, format, handlers)

        self.categories =   {   'movers': 'mover',
                                'decorators': 'decorator', 
                                'insurance': 'insurance',
                                'landscaping': 'lawn',
                                'post offices': 'postal',
                                'telcos': 'telephone',
                                'banks': 'bank',
                                'dry cleaners': 'dry cleaner',
                                'grocery stores': 'grocery',
                                'schools': 'school',
                                'day cares': 'day care',
                                'churches': 'church',
                                'gas stations': 'gas station',
                                'hospitals': 'hospital',
                                'mechanics': 'mechanic',
                                'restaurants': 'restaurant',
                                'shopping': 'plaza',
                                'hair dressers': 'hair',
                                'pharmacy': 'pharmacy',
                            }
        self.where = where
        self.uid = uid
   
    def availableCategories(self):
        return self.categories.keys() 
    
    def categoriesAndBusinesses(self):
        result = {}
        categories = self.availableCategories()
        for category in categories:
            bizListings = self.find_inArea(what=category)
            result[category] = [biz for biz in bizListings]
        return result

    def find_inArea(self, what, page=None, page_len=None,
            sflag=None, lang=None, maxDistance=float(1.0), debug=0, maxResults=10):
        where = self.where
        uid = self.uid
        try:
            resultsDict = json.loads(self.find_business(what,where,uid,page,page_len, sflag, lang))
        except (ValueError):
            return []
        listings = resultsDict.get('listings')
        if not listings:
            return []
        filteredResults = []
        for listing in listings:
            if listing.get('name', None):
                if self.isListingADupe(listing.get('name'), filteredResults):
                    continue
            if not listing.get('distance'):
                continue
            if float(listing.get('distance')) < float(maxDistance):
                self.clean_listing(listing)
                filteredResults.append(listing)
                if len(filteredResults) == maxResults:
                    break
        if debug:        
            for result in filteredResults:
                print result.get('name')
        return filteredResults
   
    # given a 'listing name' see if it's in the filtered results or not.
    def isListingADupe(self, name, filteredResults):
        for result in filteredResults:
            if name == result.get('name'):
                return True
        return False        

    # given yp listing result, remove unneeded keys
    def clean_listing(self,listing):
        keys = ['isParent', 'content', 'parentId']
        for key in keys:
            if listing.has_key(key):
                del listing[key]
        return listing

