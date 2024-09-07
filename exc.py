
class CustomItem:
    def __init__(self, name):
        self.name = name
    def __eq__(self, other):
        if isinstance(other, CustomItem):
            return self.name == other.name
    def __hash__(self):
        return hash(self.name)
list_array=[
   CustomItem("CocaCola"),
   CustomItem("Sprite"),
   CustomItem("Jumbo"),
   CustomItem("Orang")
]
def read_items_from_file(names):
    with open(names, 'r') as file:
     items = [CustomItem(line.strip()) for line in file]
    return items
file_items = read_items_from_file('names.txt')

list_hashes = set(hash(item) for item in list_array)

file_hashes = set(hash(item) for item in file_items)

common_hashes = list_hashes.intersection(file_hashes)

print("Items with matching hashes: ")
for item in list_array:
    if hash(item) in common_hashes:
        print(item.name)
       
            
print("\n","Items with different hashes: ")
if list_hashes!=file_hashes:
    print(item.name)