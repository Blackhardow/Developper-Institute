# from ast import NotIn


# word = input('Entrez un mot ')
# dict = {}
# temp = ''
# for (i, letter) in enumerate(word):
#     if letter not in dict :
#         temp = i
#         dict[letter] = []
#         dict[letter].append(temp)
# print(dict)

items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}

wallet = "$300"
amont = int(wallet.replace('$', ''))
newlist = []
for i in items_purchase.keys():
    if int(items_purchase[i].replace('$', '').replace(',', '')) <= amont :
        newlist.append(i)
print(newlist)
print(sorted(newlist))