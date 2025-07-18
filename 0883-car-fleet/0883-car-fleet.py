class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_positions = sorted(position)
        combined = sorted(list(zip(position, speed)))[::-1]

        speed_ratio = []

        for car in combined:
            speed_ratio.append((target - car[0]) / car[1])
        
        print(speed_ratio)
        prev = float('-inf')
        fleet_count = 0
        for speed in speed_ratio:
            if speed > prev:
                fleet_count += 1
                prev = speed
        return fleet_count