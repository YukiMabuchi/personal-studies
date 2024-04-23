class Solution(object):
    # merge sort
    # 遅かった
    def findKthLargest1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def merge_sort(numbers):
            if len(numbers) <= 1:
                return numbers
            
            center = len(numbers) // 2
            left = numbers[center:]
            right = numbers[:center]

            merge_sort(left)
            merge_sort(right)

            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    numbers[k] = left[i]
                    i += 1
                else:
                    numbers[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                numbers[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                numbers[k] = right[j]
                j += 1
                k += 1

            return numbers

        merge_sort(nums)

        return nums[len(nums) - k]

    # quick sort
    # timeoutした
    def findKthLargest2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def partition(numbers, low, high):
            i = low - 1
            pivot = numbers[high]

            for j in range(low, high):
                if numbers[j] <= pivot:
                    i += 1
                    numbers[i], numbers[j] = numbers[j], numbers[i]
            
            numbers[i+1], numbers[high] = numbers[high], numbers[i+1]

            return i+1
        
        def quick_sort(numbers):
            def _quick_sort(numbers, low, high):
                if low < high:
                    partition_index = partition(numbers, low, high)
                    _quick_sort(numbers, low, partition_index-1)
                    _quick_sort(numbers, partition_index+1, high)
        
            _quick_sort(numbers, 0, len(numbers)-1)

        quick_sort(nums)
        return nums[len(nums)-k]