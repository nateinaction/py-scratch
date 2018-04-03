#!/bin/python3

import sys


def minimumLoss(priceList):
    loss = sys.maxsize
    for i, thisPrice in enumerate(priceList):
        thisLoss = _minLoss(thisPrice, priceList[i:], loss)
        loss = min(loss, thisLoss)

    return loss


def _minLoss(purchasedPrice, priceList, loss):
    for thisPrice in priceList:
        myLoss = purchasedPrice - thisPrice
        if loss > myLoss > 0:
            loss = myLoss
    return loss


if __name__ == "__main__":
    myInput = "20 7 8 2 5"
    price = list(map(int, myInput.strip().split(' ')))
    result = minimumLoss(price)
    print(result)
