import numbers
a={'aa',0,'b',1,2,'g',3 }


s= {x for x in a if isinstance(x, numbers.Number)}
print(s)

dd=a.difference(s)
print(dd)
