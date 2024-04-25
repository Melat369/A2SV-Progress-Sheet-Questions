class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastOcc = {}
        
        for i,c in enumerate(s):
            lastOcc[c]=i
        size = 0
        end = 0
        output = []
        for i,c in enumerate(s):
            size += 1
            end = max(end,lastOcc[c])
            
            if i == end:
                output.append(size)
                size = 0
        return output
        # start from the string that is next to the last occurance of the string
        # check if that element is inside the last sliced string 
        # if present append it to the previous string if not
        # start looking for the last occurance of that particular sting afterwards

        # mapping the elements in the sting
        # and 
        # get the first element of the string
        # look for the last occurence of the element throuh the string
        # do the first slicing, and check if the elements in the sliced section 
        # have the exact number of counts if not append the next string literal and check







        