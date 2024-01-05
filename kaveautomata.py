#!/bin/python

def addItem(name, price):
    items.append([name, price])

def addExtra(name, price):
    extras.append([name, price])

class CoffeeMachine:
    def __init__(self, items, extras, coins):
        self.items = items
        self.extras = extras
        self.coins = coins

    def main(self):
        allowedItems = []

        for i in range(len(items)):
            print(f'{items[i][0]} - {items[i][1]}Ft')
            allowedItems.append(items[i][0])

        itemInput = input('Válassz a fenti italok közül! ').lower()
        extraInput = ""

        while itemInput not in allowedItems:
            itemInput = input('Az általad kiválasztott ital nem létezik. Kérlek, válassz a fenti listából! ').lower()

        match itemInput:
            case "kávé":
                print('\nA kávét választottad. Most jönnek az extrák.')
                allowedExtras = []
                for i in range(len(extras)):
                    if i == 3:
                        continue
                    print(f'{extras[i][0]} - {extras[i][1]}Ft')
                    allowedExtras.append(extras[i][0])
                extraInput = input('Válassz a fenti extrák közül! ').lower()
                
                while extraInput not in allowedExtras:
                    extraInput = input('Az általad kiválasztott extra nem létezik. Kérlek, válassz a fenti listából! ').lower()

            case "tea":
                print('\nA teát választottad. Most jönnek az extrák.')
                allowedExtras = []
                for i in range(len(extras)):
                    if i == 1:
                        continue
                    print(f'{extras[i][0]} - {extras[i][1]}Ft')
                    allowedExtras.append(extras[i][0])
                extraInput = input('Válassz a fenti extrák közül! ').lower()

                while extraInput not in allowedExtras:
                    extraInput = input('Az általad kiválasztott extra nem létezik. Kérlek, válassz a fenti listából! ').lower()

            case "forró csoki":
                print('\nA forró csokit választottad. Most jönnek az extrák.')
                allowedExtras = []
                for i in range(len(extras)):
                    if i == 1 or i == 3:
                        continue
                    print(f'{extras[i][0]} - {extras[i][1]}Ft')
                    allowedExtras.append(extras[i][0])
                extraInput = input('Válassz a fenti extrák közül! ').lower()

                while extraInput not in allowedExtras:
                    extraInput = input('Az általad kiválasztott extra nem létezik. Kérlek, válassz a fenti listából! ').lower()

            case _:
                print('Nem tudom hogy ezt hogy csináltad, de gratulálok.')

        itemChoice = 0
        extraChoice = 0

        for i in range(len(items)):
            if itemInput == items[i][0]:
                itemChoice = i

        for i in range(len(extras)):
            if extraInput == extras[i][0]:
                extraChoice = i

        amount = items[itemChoice][1] + extras[extraChoice][1]
        amountPaid = 0
        coinChoice = 0
        changeCoins = [0 for _ in range(5)]

        print(f'\nA fizetendő összeg {amount}Ft.')

        print('A következő érmékkel fizethetsz:')
        for i in self.coins:
            print(f'{i}Ft ', end="")
        print('\n')
        while amount > amountPaid:
            coinChoice = int(input('"Dobj be egy érmét" '))
            while coinChoice not in self.coins:
                coinChoice = int(input('Ezt az érmét vagy nem fogadjuk el, vagy rossz formátumban írtad le. Kérlek, csak egy számot adj meg, pl. "200" ahelyett hogy "200Ft" '))
            amountPaid += coinChoice
            if amount > amountPaid:
                print(f'Eddig {amountPaid} forintot fizettél ki.')
            else:
                change = amountPaid - amount
                if change == 0:
                    print('Kifizetted a teljes összeget. Nincs visszajáró. Köszönjük a vásárlást!')
                else:
                    for i in self.coins:
                        changeCoins[self.coins.index(i)] = change // i
                        change = change % i
                    print(f'Kifizetted a teljes összeget. A visszajáród {changeCoins[0]}x{self.coins[0]}Ft, {changeCoins[1]}x{self.coins[1]}Ft, {changeCoins[2]}x{self.coins[2]}Ft, {changeCoins[3]}x{self.coins[3]}Ft és {changeCoins[4]}x{self.coins[4]}Ft.')

if __name__ == "__main__":
    choice = input('Üdvözöllek. Vásárolsz vagy kilépsz? (v VAGY k) ').lower()
    while choice == 'v':
        items = []
        extras = []
        coins = [200, 100, 50, 20, 10]

        addItem("kávé", 150)
        addItem("tea", 200)
        addItem("forró csoki", 300)

        addExtra("tej", 50)
        addExtra("tejszín", 100)
        addExtra("cukor", 50)
        addExtra("citrom", 100)

        app = CoffeeMachine(items, extras, coins)
        app.main()

        choice = input('Jó újra látni téged. Vásárolsz vagy kilépsz? (v VAGY k) ').lower()
