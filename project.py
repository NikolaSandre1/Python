from itertools import combinations
def find_matches(list1, list2):
    # Find common elements in both lists
    matches = [item for item in list1 if item in list2]
    return f"{matches}"

def similarity(list1, list2):
    # Convert lists to sets for unique elements
    set1 = set(list1)
    set2 = set(list2)
    
    # Calculate intersection and union
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    
    # Calculate Jaccard similarity percentage
    if union == 0:
        return 0.0
    similarity_percentage = (intersection / union) * 100
    return similarity_percentage

def main():
    #input of the 2 lists
    print("Please paste the first list of values:")
    input_list1 = input()
    print("Please paste the second list of values :")
    input_list2 = input()
    
    # Convert pasted strings into lists
    list1 = input_list1
    list2 = input_list2

    # Calculate similarity
    similarity_percentage = similarity(list1,list2)
    
    #If they dont have similarities
    if similarity_percentage==0:
        print("\n The values are not simular.")
    # Print results

    print("\n", find_matches(input_list1,input_list2))
    print(f"Percentage of similarity: ",similarity_percentage,"%")
   
   

main()