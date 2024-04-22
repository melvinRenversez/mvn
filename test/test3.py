x = input('~# ')
xs = x.split(' ')
list_action = []
print(xs)
for r in xs:
    if r != '':
        if r[0] == '-':
            print("find ::: ", r)
            print("index ::: ", xs.index(r))
            print("action ::: ", xs[xs.index(r)+1])
            val = [r, xs[xs.index(r)+1]]
            list_action.append(val)
            
print('')
print(list_action)