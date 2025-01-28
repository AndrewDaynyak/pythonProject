#~O~O~O~OP~O~OO~

town='~O~O~O~OP~O~OO~'
split = town.split('O')
if town.startswith('P'):
    print(split.count('~O'))
if town.endswith('P'):
    print(split.count('O~'))
else:
    index_p=enumerate(town)
    for index, letter in index_p:
        if letter == 'P':
            letter_p=index
            left=town[0:letter_p]
            left_split=left.split()
            print(left_split)
            right = town[letter_p+1:]
            print(right)
            res1=left.count('O~')
            res2=right.count('~O')
            total=res1+res2
            print(total)



