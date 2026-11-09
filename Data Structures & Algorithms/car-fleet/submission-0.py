class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [] # [position, speed, ideal endtime]
        fleets = 0
        fleetTime = -2

        for i in range(len(position)):
            if speed[i] > 0:
                endTime = (target - position[i]) / speed[i]
            else:
                endTime = -1                
            cars.append([position[i], speed[i], endTime])

        cars.sort(reverse=True, key=lambda x: x[0])

        for car in cars:
            if car[2] == -1:
                break

            if fleetTime == -2 or fleetTime < car[2]:
                fleets += 1
                fleetTime = car[2]

        return fleets