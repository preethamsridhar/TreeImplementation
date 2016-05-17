# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 12:16:24 2016

@author: Preetham Sridhar
"""
from collections import deque


class TreeNode(object):
    """
    Basic tree structure
    
    """
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    @staticmethod
    def sortedArrayToBST(nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums == []:
            return None

        def funct(nums, start, end):
            if start == end:
                root = TreeNode(nums[start])
                return root

            mid = (start + end) / 2

            root = TreeNode(nums[mid])

            if start < mid: root.left = funct(nums, start, mid - 1)
            if mid < end: root.right = funct(nums, mid + 1, end)

            return root

        return funct(nums, 0, len(nums) - 1)

    @staticmethod
    def in_order_traversal(root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        list_val = []

        def in_ord(root):
            if root is None:
                return
            in_ord(root.left)
            list_val.append(root.val)
            in_ord(root.right)

        in_ord(root)
        return list_val

    @staticmethod
    def pre_order_traversal(root):
        list_val = []
        def pre_order(root):
            if root is None:
                return
            list_val.append(root.val)
            pre_order(root.left)
            pre_order(root.right)

        pre_order(root)
        return list_val

    @staticmethod
    def post_order_traversal(root):
        list_val = []
        def post_order(root):
            if root is None:
                return
            post_order(root.left)
            post_order(root.right)
            list_val.append(root.val)

        post_order(root)
        return list_val

    @staticmethod
    def level_order_traversal(root):
        que = deque()
        que.append(root)
        flag = False
        result = []
        while que:
            for i in que:
                if i =='null':
                    flag = False
                else:
                    flag = True
                    break

            if flag:
                if not que[0] == 'null':
                    cur = que.popleft()
                    result.append(cur.val)

                    if cur.left:
                        que.append(cur.left)
                    else:
                        que.append("null")

                    if cur.right:
                        que.append(cur.right)
                    else:
                        que.append("null")
                else:
                    cur = que.popleft()
                    result.append("null")
            else:
                return result


    @staticmethod
    def find_the_path(root, value):
        path = []
        def find_path(root):
            if not root is None:
                path.append(str(root.val))
                if not root.val == value:
                    a = find_path(root.left)
                    b = find_path(root.right)
                    if a is False and b is False:
                        path.pop()
                        return False
                if root.val == value:
                    return True
            else:
                return False

        find_path(root)
        if path:
            return path
        else:
            return ["not found"]

    @staticmethod
    def find_the_path_between(root,p,q):
        path_p = []
        path_q = []

        def find_path_p(root):
            if not root is None:
                path_p.append(str(root.val))
                if not root.val == p:
                    a = find_path_p(root.left)
                    b = find_path_p(root.right)
                    if a is False and b is False:
                        path_p.pop()
                        return False
                if root.val == p:
                    return True
            else:
                return False

        def find_path_q(root):
            if not root is None:
                path_q.append(str(root.val))
                if not root.val == q:
                    a = find_path_q(root.left)
                    b = find_path_q(root.right)
                    if a is False and b is False:
                        path_q.pop()
                        return False
                if root.val == q:
                    return True
            else:
                return False

        find_path_p(root)
        find_path_q(root)
        new_path = []
        for i in range(min(len(path_p),len(path_q))):
            if path_p[i] == path_q[i]:
                continue
            else:
                path_p=path_p[::-1]
                new_path = path_p[:len(path_p)-i+1]+path_q[i:len(path_q)]
                break
        return new_path




tree = Solution.sortedArrayToBST([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
print "In order->",Solution.in_order_traversal(tree)
print "Pre order->",Solution.pre_order_traversal(tree)
print "Post order->",Solution.post_order_traversal(tree)
print "Level order->",Solution.level_order_traversal(tree)
print "Enter the node value to find the path"
n = int(raw_input())
print "Path to %s:" %n,"->".join(Solution.find_the_path(tree, n))
print "Enter two node values to find the between path"
p,q = map(int,raw_input().split())
print "Path to %d and %d:"%(p,q),
print Solution.find_the_path_between(ree, p, q)
