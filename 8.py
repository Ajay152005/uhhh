diction = {'SENIORS' : {'BHARATHI': 10 , 'TAGORE': 9, 'SHIVAJI': 8, 'PRATAP': 7}, 
           'JUNIORS' : {'BHARATHI' : 6, 'TAGORE': 5, 'SHIVAJI': 4, 'PRATAP': 3 },
            'SUBJUNIONS': {'BHARATHI': 2, 'TAGORE': 1, 'SHIVAJI': 0, 'PRATAP': 10 }}

def MAX_SCORE(diction):
    result = {}
    for cate, value in diction.items():
        max1 = 0
        for cate1, val in value.items():
            if value[cate1] > max1:
                max1 = value[cate1]
                max_name = cate1
        result[cate] = max_name

    return result

result = MAX_SCORE(diction)

print("Houses with maximum score: ")

for name, value in result.items():
    print(name, "  :  ", value)
    