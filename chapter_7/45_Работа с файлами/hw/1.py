file_path = "../nums.txt"
with (open(file_path,'r')) as f:
        nums = f.read()

nums_list = list(map(float, nums.split()))
nums_list.sort()
nums_str = list(map(str,nums_list))

with open("../nums.txt","a") as f:
        f.write("\t")
        for t in nums_str:
               f.writelines(t+'\t')

