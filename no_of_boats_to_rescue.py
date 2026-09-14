class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        boats = 0
        while left <= right:
            # put the lightest person with the heaviest
            if people[left] + people[right] <= limit:
                left += 1
            # heaviest person always needs a boat
            right -= 1
            boats += 1
        return boats
