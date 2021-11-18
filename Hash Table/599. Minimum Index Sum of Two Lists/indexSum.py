class Solution:
    def findRestaurant(self, list1: "list[str]", list2: "list[str]") -> "list[str]":
        bothLike = {}
        choices = []
        for place in list1:
            if place in list2:
                bothLike[place] = list1.index(place) + list2.index(place)

        lowestIndex = min(bothLike.values())
        for key in bothLike:
            if bothLike[key] == lowestIndex:
                choices.append(key)
        
        return choices

check = Solution()
print(check.findRestaurant(
    list1=["Shogun","Tapioca Express","Burger King","KFC"],
    list2=["KFC","Burger King","Tapioca Express","Shogun"]
))