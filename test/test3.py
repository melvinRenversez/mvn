x = input('~# ')
xs = x.split(' ')
list_action = []
for r in xs:
    if r != '':
        if r[0] == '-':
            print("find ::: ", r[1:])
            print("index ::: ", xs.index(r))
            print("action ::: ", xs[xs.index(r)+1])
print(xs)