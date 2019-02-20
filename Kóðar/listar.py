## Listar
## Býr til listann lst
lst = ['x', 'y', 'z', 1, 2, 3, 1, 2, 3]
print('listinn í byrjun', lst)

## Bætir við listann lst
lst.append('x')
print('búið að bæta x í listann', lst)

## Tekur hlutinn með indexinn 1 úr listanum
## í þessu tilfelli er það 'y'
lst.pop(1)
print('búið að taka index 1 úr listanum', lst, end = ' ')
print('og index 1 orðið', lst[1])

## Tekur fyrsta atvik þar sem
## 'x' kemur fyrir úr listanum
lst.remove('x')
print('Fyrsta x-ið var tekið úr lst',lst)

## Fall sem tekur eyðir öllum
## x í lst
def remove_all_x(listinn, value):
    while value in listinn:
        listinn.remove(value)
        
## Kallar á fallið og setur
## lst of 1 inn í fallið
remove_all_x(lst, 1)
print('Öllum ásum hefur verið eytt út', lst)

## For lykkjur með listum
for i in lst:
    print(i)
for num, item in enumerate(lst, 0):
    print('Hlutur á index', num, 'er:', item)

## Skipta hluti með index 1 og 5
print(lst)
lst[1], lst[5] = lst[5], lst[1]
print(lst)

## Segir hversu margir hlutir
## eru í listanum
print('Það eru', len(lst), 'hlutir í listanum')
