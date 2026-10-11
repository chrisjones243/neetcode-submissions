class Solution:
    def time_to_eat(self, piles: List[int], speed: int) -> time:
        hours = 0
        for pile in piles:
            hours += (pile + speed - 1) // speed
        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        min_speed = 1
        max_speed = max(piles)
        result = max_speed

        while min_speed <= max_speed:
            speed = min_speed + (max_speed - min_speed) // 2
            hours = self.time_to_eat(piles, speed)

            if hours <= h:
                result = speed
                max_speed = speed - 1
            else: 
                min_speed = speed + 1
            
        return result

        