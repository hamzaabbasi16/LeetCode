class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        counter = Counter(candidates)
        counter = [(key, counter[key]) for key in counter]
        
        def recursion(index = 0, current_combination = [], combination_sum = 0):
            if combination_sum > target or index not in range(len(counter)): return
            elif combination_sum == target: combinations.append(current_combination.copy()) 
            else:
                candidate, frequency = counter[index]
                if frequency > 0:
                    counter[index] = (candidate, frequency-1)
                    recursion(index, current_combination + [candidate], combination_sum + candidate)
                counter[index] = (candidate, frequency)
                recursion(index+1, current_combination, combination_sum)
                        
        recursion()
        return combinations