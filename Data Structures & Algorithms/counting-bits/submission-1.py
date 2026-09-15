class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(0,n+1):
            a = bin(i)[2:]
            counter = 0
            for char in a:
                if char == '1':
                    counter += 1
            output.append(counter)

            print(a)
        return output
        