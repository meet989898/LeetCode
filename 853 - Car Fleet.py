from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        carFleet = []

        pairs = [[position[i], speed[i]] for i in range(len(position))]

        pairs.sort(reverse=True)

        for pair in pairs:
            # print(carFleet)
            pos, sp = pair
            # print(pair)
            time_taken = (target - pos)/sp
            # print(time_taken)

            if len(carFleet) >= 1 and time_taken <= carFleet[-1]:
                # print("Carfleet made")
                continue

            carFleet.append(time_taken)

        return len(carFleet)

sol = Solution()

target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
print(sol.carFleet(target, position, speed))