import json
import API_stuff

# Todo replace Bazaar.json with api grabber
f = open("Bazaar.json")
data = json.load(f)


def BazzarDataCollect():
    # Todo create the api reader
    return None


def PID_Gather(BazzarData):
    # creates an array of all item id's which currently exist in the bazzar
    Product_dict = BazzarData['products']
    ItemID_list = []
    for ID in Product_dict:
        ItemID_list.append(ID)
    return ItemID_list


def ProfitMarginCaluRaw(SellP, BuyP):
    # Takes the Market Prices for the goods and calulates how many coins you would gain via a flip to 1.d.p
    return round(BuyP - SellP, 1)


def ProfitMarginCaluPercent(SellP,BuyP):
    Margin = BuyP - SellP
    percent = Margin / SellP
    return round(percent*100,2)

def Top3Invest(MarginQuantity,ItemID_list):
    Top3 = [{},{},{}]
    Top3[0] = MarginQuantity[0]
    Top3[1] = MarginQuantity[1]
    Top3[2] = MarginQuantity[2]
    return Top3

def main(BazaarData):
    ItemID_list = PID_Gather(BazaarData)
    MarginDict = {}
    for Item in ItemID_list:
        ItemMargin = ProfitMarginCaluRaw(data['products'][Item]['quick_status']['sellPrice'],
                                         data['products'][Item]['quick_status']['buyPrice'])
        MarginDict.update({Item: ItemMargin})
    return Top3Invest()

print(main(data))