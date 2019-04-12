quads = ['= a b c', 'goto _', 'gotoF $2 _']

def fillGoto(position, fillValue):
    global quads
    quads[position] = quads[position].replace('_', str(fillValue))
    return

print(quads)
fillGoto(1, 4)
print(quads)
fillGoto(2, 5)
print(quads)