                return reduce(lambda a,x: [x+a[0],0] if not a[1] and ord(x)>58 else [a[0],a[1]-((ord(x)>58)<<1)+1] ,s[::-1],['',0])[0]