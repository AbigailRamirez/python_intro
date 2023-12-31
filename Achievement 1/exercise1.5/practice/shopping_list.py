class ShoppingList(object):
    #initialization method
    def __init__(self, list_name):
        self.list_name = list_name
        shopping_list = []
        self.shopping_list = shopping_list
    
    # Method to add new items to self.shopping_list
    def add_item(self, item):
        self.item = item
        if item in self.shopping_list:
            print("Item is already in the list!")
        else:
            self.shopping_list.append(item)
            print("Item added to list!")
    
    # Method to remove items to self.shopping_list
    def remove_item(self, item):
        self.item = item
        if item in self.shopping_list:
            self.shopping_list.remove(item)
            print("Item was removed from the list!")
        else:
            print("Item not found in list.")
    
    # Method to print all items in self.shopping_list
    def view_list(self):
        print("Shopping List: ", self.list_name)
        print("----------------------------------")
        for item in self.shopping_list:
            print(item)

# Initialize a new list
pet_store_list = ShoppingList("Pet Store Shopping List")

# Add the following items to the list using the add_item() method: dog food, frisbee, bowl, collars, flea collars
pet_store_list.add_item("dog food")
pet_store_list.add_item("frisbee")
pet_store_list.add_item("bowl")
pet_store_list.add_item("collars")
pet_store_list.add_item("flea collars")

# Remove flea collars using the remove_item() method
pet_store_list.remove_item("flea collars")

# Try adding frisbee again using the add_item() method
pet_store_list.add_item("frisbee")

# Display the entire shopping list through the view_list() method
pet_store_list.view_list()