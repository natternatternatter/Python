class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        # your code here
        for x in nums:
            num += x
            self.result + x
        # print(num)
        # num = self
        # self.result = num

        return self

    def subtract(self, num, *nums):
        # your code here
        # print(num)
        # print(nums)
        for x in nums:
            num -= x
            self.result - x
        # self.result = num
        return self
    # create an instance:


md = MathDojo()
# to test:
# print(md.result)
# (md.subtract(10, 5, 1).result)
# print(md.result)

md.add(2).result
print(md.result)

md.add(2, 5, 1).result
print(md.result)

md.subtract(3, 2).result
print(md.result)
# should print 5
