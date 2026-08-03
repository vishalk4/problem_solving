def generateParenthesis(n: int):
    result = []  # store all valid combinations
    
    # Helper function for backtracking
    def backtrack(current, open_count, close_count):
        # current → current string being built
        # open_count → number of '(' used
        # close_count → number of ')' used
        
        # ✅ Base case: if string length is 2*n → valid combination
        if len(current) == 2 * n:
            result.append(current)
            return
        
        # ✅ Add '(' if we still have some left
        if open_count < n:
            backtrack(current + "(", open_count + 1, close_count)
        
        # ✅ Add ')' only if it won't make it invalid
        # condition: close_count < open_count
        if close_count < open_count:
            backtrack(current + ")", open_count, close_count + 1)
    
    # start recursion
    backtrack("", 0, 0)
    
    return result
