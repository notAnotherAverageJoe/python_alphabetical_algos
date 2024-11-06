

def narc_num(n):
    result =0
    n_str = str(n)
    
    for i in range(len(n_str)):
        result += int(n_str[i]) ** len(n_str)
        
    return result == n

        
print(narc_num(153))
print(narc_num(15))