# Last updated: 9/17/2025, 10:57:29 AM
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = foods
        self.cuisines = cuisines
        self.ratings = ratings
        
        self.food_cuisine = {foods[i] : (cuisines[i], ratings[i]) for i in range(len(foods))}
        self.cuisine_rating = {}

        for i, cuisine in enumerate(cuisines):
            if cuisine not in self.cuisine_rating:
                self.cuisine_rating[cuisine] = []
            
            heapq.heappush(self.cuisine_rating[cuisine], (-ratings[i], foods[i]))


    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, rating = self.food_cuisine[food]

        self.food_cuisine[food] = (cuisine, newRating)

        heapq.heappush(self.cuisine_rating[cuisine], (-newRating, food))



        

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_rating[cuisine]
        while heap:
            rating_neg, food = heap[0]
            if self.food_cuisine[food][1] == -rating_neg:
                return food
            heapq.heappop(heap)  
        return ""  


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)