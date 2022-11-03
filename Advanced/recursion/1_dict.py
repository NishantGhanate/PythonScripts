def get_dict_diff(old, new):
    
    n_dict_diff = {}
    def compare(old, new):
        dict_diff = {}
        if not isinstance(old, dict) or isinstance(new, dict) :
            return dict_diff
        
        for key in new:
            if key in old:
                new_val = new[key]
                old_val = old[key]
                if isinstance(new_val, dict) and isinstance(old_val, dict):
                    # print(new_val, old_val)
                    temp_new, temp_old = {}, {}
                    temp_new[key] = new[key]
                    temp_old[key] = old[key]
                    compare(temp_new, temp_old)
                    
                elif old_val != new_val:
                    dict_diff[key] = new_val

            else:
                dict_diff[key] = new[key]
        return dict_diff

    n = compare(old, new)
    print(n)
    # return dict_diff


a = {
    'a' : 1,
    'b' : {
        'old_1' : 2,
        'old_2' : 3
    },
    'c' : 4
}

b = {
    'a' : 1,
    'b' : {
        'old_1' : 3,
        'old_2' : 4
    },
    'c' : 5
}

ans = get_dict_diff(old=a , new=b)
# print(ans)