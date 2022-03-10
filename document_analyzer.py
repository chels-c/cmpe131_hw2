wordDict = {}

with open('document.txt','r') as f:
        for line in f:
                for word in line.split(" "):
                        if word in wordDict:
                                wordDict[word] += 1
                        else:
                                wordDict[word] = 1

dict_items = wordDict.items()
sorted_items = sorted(dict_items)
sorted_dict = sorted(sorted_items, key=lambda x:x[1], reverse=True)

print()
for i in sorted_dict[0:5]:
        print(i[0], ":", i[1])
