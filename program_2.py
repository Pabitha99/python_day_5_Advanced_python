# using lambda function to check every element is integer or string in list 
my_list=[1,"a",2,"b",3,"c"]
check_l=lambda x:'integer' if isinstance(x,int) else 'string'
result=list(map(check_l,my_list))
print(result)
# output:['integer', 'string', 'integer', 'string', 'integer', 'string']