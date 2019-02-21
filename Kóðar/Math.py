## Innbyggð stærðfræði

## Tölugildi:
## 10 = 10, -10 = 10
num = abs(int(input()))
print(num)

## Integer Division & Modulo
## Int Division er heiltöludeiling og skilar x/y nema enginn afganur
## Modulo er afgangurinn eftir að y hefur verið dregið frá þar til ekki er hægt lengur án þess að fara ú mínus
x, y = map(int, input().split())
num = divmod(x, y)
print('x//y =', num[0], ', x%y =', num[1])

## Max
## gefur hæðstu töluna
num = max(list(map(int, input().split())))
print(num)

## Min
## gefur læðstu töluna
num = min(list(map(int, input().split())))
print(num)


import math
