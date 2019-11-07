lstflavors = []

def updateflavors(op, flav):

    if op == "add":
                    
        if flav in lstflavors:
            print(f"{flav} already exists \n Choose a different flavor.")
        else:         
            lstflavors.append(flav)
            print(f"{flav} added to your {lstflavors} cone!")
            
        print(f"That's {len(lstflavors)} scoops! \n Enjoy your {lstflavors} ice cream cone!")
    
    if op == "remove" and len(lstflavors) != 0:
        if flav in lstflavors:
            lstflavors.remove(flav)
            print(f"Removed {flav} from your {lstflavors} ice cream cone.")
        else:
            print(f"{flav} not on your {lstflavors} ice cream cone.")


updateflavors("add", 'vanilla')
updateflavors("add", 'blueberry')
updateflavors("add", 'chocolate')
updateflavors("remove", 'vanilla')
updateflavors("remove", 'vanilla')
