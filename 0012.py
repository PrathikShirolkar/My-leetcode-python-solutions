class Solution:
    def intToRoman(self, num: int) -> str:
        key = dict()
        key[0] = ""
        key[1] = "I"
        key[5] = "V"
        key[10] = "X"
        key[50] = "L"
        key[100] = "C"
        key[500] = "D"
        key[1000] = "M"
        
        
        nums = list()
        snum = str(num)
        multiplier = int("1"+"0"*(len(snum)-1))
        print(multiplier)
        for i in snum:
            nums.append(int(i)*multiplier)
            multiplier = int(multiplier/10)
        
        print(nums)
        res = ""
        for i in nums:
            diff_pos = list()
            exact = 0
            print("===>",i)
            for j in list(key.keys())[::-1]:
                if j == i:
                    res += key[j]
                    exact = 1
                    break
                elif i!=0 and (j-i) in [1,10,100]:
                    res += key[j-i]+key[j]
                    print("two",key[j-i]+key[j])
                    break
                else:
                    if (i-j) in [1,10,100,1000]:
                        res+= key[j]+key[int((i-j))]
                        print("three.1",key[j]+key[int((i-j))])
                        break
                    elif (i-j)/2 in [1,10,100,1000]:
                        res+= key[j]+key[int((i-j)/2)]*2
                        print("three.2",key[j]+key[int((i-j)/2)]*2)
                        break
                    elif (i-j)/3 in [1,10,100,1000]:
                        res+= key[j]+key[int((i-j)/3)]*3
                        print("three.3",key[j]+key[int((i-j)/3)]*3)
                        break
            #print("-----------------")
        print(res)
        return res