#This is meant to be the file that holds all the inventory information for the POS system


#this is the class item. Think of it as the term human meaning several different individuals.
class item:

    def __init__(self):

        self.name='empty'
        self.UPC=00000000
        self.itemqty=00

#this is a method meant to allow the user to update the intended item
    def update(self):

        choice= input("Hi, the item you are updating is", self.name, "would you like to update 1. UPC, 2. Description, or 3. QTY?")

        if choice == 1:

            self.UPC=input("please input the new UPC")

        elif choice == 2:

            self.name=input("please input the new item description")

        else:

            self.itemqty=input("please input the new item QTY")


#These are the different things the store sells, in other words the inventory
MtnDew_BajaBlast = item()
BioreCharMask = item()
DoveAvdDrySham_VF = item()
singleweek_pillCase = item()
Jergans_ArganOil = item()
WhiteOut_Liq = item()
EZReach_BIC = item()
Chapstick_cherr = item()
Febreze_PetOdor = item()
SHanson_InstaDri_523 = item()
SHanson_InstaDri_573 = item()
BArmor_FPunch = item()

        