class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        color = [0] * (n+2)
        tempv = 0
        to_ret = []
        for idt, cot in queries :
            idt += 1
            # If the color of the current index is not 0 and it is the same as the color of the previous index, decrement tempv by 1.
            if color[idt] != 0 and color[idt] == color[idt-1] :
                tempv -= 1
            # If the color of the current index is not 0 and it is the same as the color of the next index, decrement tempv by 1.
            if color[idt] != 0 and color[idt] == color[idt+1] :
                tempv -= 1
            
            # Set the color of the current index to the color specified in the query.
            color[idt] = cot
            # If the color of the current index is the same as the color of the previous index, increment tempv by 1.
            if color[idt] == color[idt-1] :
                tempv += 1
            # If the color of the current index is the same as the color of the next index, increment tempv by 1.
            if color[idt] == color[idt+1] :
                tempv += 1
            # Add tempv to the list of answers.
            to_ret.append(tempv)
        return to_ret