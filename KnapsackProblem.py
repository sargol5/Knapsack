
#define a class for knapsack
class KnapsackClass():
     def _init_(self): 
        
        pass
    
#define a class for items which is subclass of knapsackclass
class itemsClass(KnapsackClass):
     def _init_(self): 
        
         pass
        
#define a method which gives us the max value that we can select from the knapsack with the limitation of capacity
     def find_max_value(self,NumberOI,ValueOItem, WeightOItem, capacity,items):
      
        numberOV = len(ValueOItem)
        if capacity <= 0 or numberOV == 0 or len(WeightOItem) != numberOV:
                return 0
#in dynamic programming We have a table and hear We describe capacity as the column,
#and items as the rows. each item in each step can be selected just one time
#each cell in matrix is the total value of selected items

        T = [[0 for x in range(capacity+1)] for y in range(numberOV)]
    
#We set all T[i][0]=0 because the capacity is zero for them,#go through the matrix for other capacities

        for i in range(0, numberOV):
            T[i][0] = 0
        for c in range(0, capacity+1):
            if WeightOItem[0] <= c:
                T[0][c] = ValueOItem[0]
        for i in range(1, numberOV):
            for c in range(1, capacity+1):
                v=0
#if the weight of item is less than the capacity
#We should choose between two states and keep two states that are:(1-the value of last step (T[i-1][c])
#and 2-ssum of the value of selected item with the value that we have from last step)
#each time we have access to the last steps and no need to calculate them again (dynamic programming feature)
    
                if WeightOItem[i] <= c:
                    v = T[i - 1][c - WeightOItem[i]]+ValueOItem[i]
                T[i][c] = max(T[i - 1][c], v)
                
#Considering a list= lst for returning value to print it in the output.sol            
        lst= print_items(T,items,WeightOItem, ValueOItem, capacity)
    
#the last cell of the table is our response so we should return that
        return T[numberOV - 1][capacity],lst
   


    
    
#This method will return the selected items
#in this algorithm we start from the last cell and compare it with above row in that column, 
#if the values are not equal,so the item is selected and append it to the list and return that

def print_items(T,items,WeightOItem, ValueOItem, capacity):
        lst =[]
        n = len(WeightOItem)
        totalValueOItem = T[n-1][capacity]
        for i in range(n-1,0, -1):
            if totalValueOItem != T[i - 1][capacity]:
                lst.append(items[i])
                
#after We added the selected item to the list we should decrease the weight of that from capacity
#and decrease the value of that from totalValueOItem and go to the column with that capacity in the previous row
                capacity-= WeightOItem[i]
                totalValueOItem -= ValueOItem[i]
        return lst
        
        
        
        
        
        
def main():
#choose an object and named it as “backpack” 
    backpack=itemsClass()
#Read file from input.txt and split it for setting them as the input in method” find_max_value” 
    a_file = open("input-sara.txt","r")
    lists = [(line.strip()).split() for line in a_file]
    arr=[]
    arr1=[]
    arr2=[]
    
#The input list contains four sub lists which contains: number of items, items, weight of items,
#value of items and capacity 
    
    for i in range (1,len(lists)-1):
#read the first item in the big List which shows the number of items and put in "NumberOI"
            NumberOI1=lists[0]
#read the last items in the big List which shows capacity and put in "capacity"
            capacity1=lists[len(lists)-1]
#read the first items of each nested list and put in array(items1)
            arr.append(lists[i][0])
            items1=arr
#read the second items of each nested list and put in "ValueOItem" which shows the value of items
            arr1.append(lists[i][1])
            ValueOItem1=arr1
#read the third items of each nested list and put in array"WeightOItem" which shows the weight of each item
            arr2.append(lists[i][2])
            WeightOItem1=arr2
        
#As We have list of strings, we should change them to list of integers
    ValueOItem1 = list(map(int, ValueOItem1))
    WeightOItem1=list(map(int, WeightOItem1))
    NumberOI1=list(map(int, NumberOI1))
    capacity1=list(map(int, capacity1))
  
 #As "ValueOItem" is a list of integers, We should change it to an integer 

    strings = [str(integer) for integer in capacity1]
    capacity_string = "".join(strings)
    capacity_integer = int(capacity_string)

#print the output
    print("Total knapsack value: " + 
               str(backpack.find_max_value(NumberOI1,ValueOItem1, WeightOItem1,capacity_integer,items1)))
    
    final_result = backpack.find_max_value(NumberOI1,ValueOItem1, WeightOItem1,capacity_integer,items1)
    print(final_result[0])
#write the output in a text file named: "output.sol"
    with open("output-sara.sol",'w') as f:
        f.write("Selected items from the knapsack are: ")
        for elem in final_result[1]:
            f.write(elem + '  ')
        f.write('\n')
        f.write("Total knapsack value: " + str(final_result[0]))
    f.close()
    
main()