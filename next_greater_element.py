def nextGreaterElement(nums1, nums2):
    nums1Idx = {n: i for i, n in enumerate(nums1)}
    res = [-1] * len(nums1)

    stack = []
    for i in range(len(nums2)):
        cur = nums2[i]
        while stack and cur > stack[-1]:
            val = stack.pop()
            idx = nums1Idx[val]
            res[idx] = cur
        if cur in nums1Idx:
            stack.append(cur)
    return res

    nums1Idx = {n: i for i, n in enumerate(nums1)}
    res[-1] * len(nums1)

    for i in range(len(nums2)):
        if nums2[i] not in nums1Idx:
            continue
        for j in range(i + 1, len(nums2)):
            if nums2[i] > nums2[i]:
                idx = nums1Idx[nums2[i]]
                res[idx] = nums2[j]
                break