class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergeSort(cur_nums: List[int]):
            n = len(cur_nums)
            if n <= 1:
                return cur_nums

            mid: int = n // 2
            left: List[int] = mergeSort(cur_nums[:mid])
            right: List[int] = mergeSort(cur_nums[mid:])

            return merge(left, right)

        def merge(left: List[int], right: List[int]) -> List[int]:
            i = 0
            j = 0

            out: List[int] = []
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    out.append(left[i])
                    i += 1
                else:
                    out.append(right[j])
                    j += 1

            out.extend(left[i:])
            out.extend(right[j:])

            return out

        return mergeSort(nums)
            

            