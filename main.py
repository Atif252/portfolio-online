blue_st = '<span class="blue">'
blue_end = '</span>'
a = 'def func(url, args):'
if 'def' in a:
    b, c = a.split()[0],a.split()[1:]
    b = blue_st + str(b) + blue_end
    print(b, c[0], c[1])


if 'return' in a:
    b = a.split()[0]
    b = blue_st + str(b) + blue_end
    print(b)


if 'from' in a:
    b = a.split()[0]
    b = blue_st + str(b) + blue_end
    print(b)

if 'import' in a:
    b = a.split()[0]
    b = blue_st + str(b) + blue_end
    print(b)
