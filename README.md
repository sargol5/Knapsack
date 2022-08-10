# Knapsack
I have three files:
1- KnapsackProblem.ipynb
2- Input-sara.txt
3- Output.sol which is empty and the output will be printed on that 

My program read input file and split the lines for putting them in the argument of my method and print the output in file output.sol. 
My program “ KnapsackProblem” contains : 
A. Two classes: 
1- “KnapsackClass” 2- “itemsClass” 
B. Two methods: 
1- find_max_value:givesusthemaxvaluethatwecanselectfromthe knapsack with the limitation of capacity . 
2- print_items: return the selected items for putting in the knapsack. C. one table called:”T” 
find_max_value method: 
in dynamic programming We have a table and here We describe capacity as the column, and items as the rows. each item in each step can be selected just one time. each cell in matrix is the total value of selected items. 
We set all T[i][0] =0 because the capacity is zero for them, then go through the matrix for other capacities. if the weight of item is bigger than the capacity, we should consider the last step items. 
if the weight of item is less than the capacity, We should choose between two states and keep the max of these two states that are:(1-the value of last step (T[i- 1][c]) and 2-sum of the value of selected item with the value that we have from last step). 
each time we have access to the last steps and no need to calculate them again and because of this feature dynamic programming is helpful.
As the last cell of the table is our response so we should return that to print it in the output.sol. 
printitems method: 
This method will return the selected items. in this algorithm we start from the last cell and compare it with above row in that column, if the values are not equal, so the item is selected and append it to the list and return that. After We added the selected item to the list, we should decrease the weight of that from capacity 
and decrease the value of that from totalValueOItem and go to the column with that capacity in the previous row.
Main:
choose an object and named it as “backpack” from Knapsack class for using its methods. 
Read file from input.txt and split it for setting them as the input in method” find_max_value”. 
The input list contains four sub lists which contains: number of items, items, weight of items, value of items and capacity. 
•	read the first item in the big List which shows the number of items and put in "NumberOI". 
•	read the last item in the big List which shows capacity and put in "capacity" 
•	read the first items of each nested list and put in array (items1). 
•	read the second items of each nested list and put in "ValueOItem" which 
shows the value of items. 
•	read the third items of each nested list and put in array "WeightOItem" which 
shows the weight of each item. 
As We have list of strings, we should change them to list of integers. As "ValueOItem" is a list of integers, we should change it to an integer. 
Print the output and write the output in a text file named: "output.sol". 

![image](https://user-images.githubusercontent.com/100320852/183782665-de38e486-3e5b-46c2-9902-79a18524b494.png)
