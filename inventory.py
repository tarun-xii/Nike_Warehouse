

contents = ""
#Programme has a Shoe class 
#Shoe class reads in data from inventory text file
#we create 5 objects to store atleast 5 data points from file 
#We compute the lowest quantity item, and output this to the user and signifiy that we need to restock
#We compute highest quantity product and compute that we need to have a sale 
#We use a function to work out value of items 
#We output this data to the user


class Shoe_class:


   def __init__(self,country,code,product,cost,quantity):
         self.country = country
         self.code = code
         self.product = product
         self.cost = cost
         self.quantity = quantity



   def read_data(file_name):

      try:
          with open(file_name, 'r+') as f:

                next(f)  #Skips the headings
                for line in f:
                    #line_counter += 1
                    user_input = line  #Used to get first initial
                    warehouse_string = line.split(",")  #Used to split sentence into individual words
              
                    #print(f"{warehouse_string[0]} {warehouse_string[1]} {warehouse_string[2]} {warehouse_string[3]} {warehouse_string[4]}") #Output to user
                    
                    if (warehouse_string[0]=="Canada"):
           
                          Shoe_class.Canada = line
 
                    if (warehouse_string[0]=="Morocco"):
                       
                          Shoe_class.Morocco = line

                    if (warehouse_string[0]=="Brazil"):
             
                          Shoe_class.Brazil = line

                    if (warehouse_string[0]=="China"):
 
                          Shoe_class.China = line

                    if (warehouse_string[0]=="France"):
    
                          Shoe_class.France = line
                          



      except FileNotFoundError:
            print("Please review file name and retry")
        
   def value_per_item(self):
         value = self.cost * self.quantity
         return value




warehouse_name = 'inventory.txt'

Shoe_class.read_data(warehouse_name)

#Creating the objects of the class 
Canada = Shoe_class.Canada
Morocco = Shoe_class.Morocco
Brazil = Shoe_class.Brazil
China = Shoe_class.China
France = Shoe_class.France

code_can = Canada.split(",")  #Used to split sentence into individual words
code_mor = Morocco.split(",")
code_bra = Brazil.split(",")
code_chi = China.split(",")
code_fra = France.split(",")

Canada_obj =  Shoe_class(code_can[0],code_can[1],code_can[2],int(code_can[3]),int(code_can[4]))
Morocco_obj = Shoe_class(code_mor[0],code_mor[1],code_mor[2],int(code_mor[3]),int(code_mor[4]))
Brazil_obj =  Shoe_class(code_bra[0],code_bra[1],code_bra[2],int(code_bra[3]),int(code_bra[4]))
China_obj =   Shoe_class(code_chi[0],code_chi[1],code_chi[2],int(code_chi[3]),int(code_chi[4]))
France_obj =  Shoe_class(code_fra[0],code_fra[1],code_fra[2],int(code_fra[3]),int(code_fra[4]))


list_of_countries = [Canada,Morocco,Brazil,China,France]




#Search in list by code 
user_code_input = str(input("Please enter product code : "))

if (user_code_input == code_can[1]):
      print(Canada)
elif (user_code_input == code_mor[1]):
      print(Morocco)
elif (user_code_input == code_bra[1]):
      print(Brazil)
elif (user_code_input == code_chi[1]):
      print(China)
elif (user_code_input == code_fra[1]):
      print(France)
else : 
      print("No data found")
      

#Determine lowest quantity 

quantity_list = [code_can[4],code_mor[4],code_bra[4],code_chi[4],code_fra[4]]
product_list =  [code_can[2],code_mor[2],code_bra[2],code_chi[2],code_fra[2]]


for i in range(0,5):
      if (quantity_list[i]==min(quantity_list)):
            print(f"Lowest quantity product is : {product_list[i]}. Restock ")
            
      elif (quantity_list[i]==max(quantity_list)):
            print(f"Highest quantity product is : {product_list[i]}. Put for sale ")



test_list =  [code_can[2],code_mor[2],code_bra[2]]

#Calling function 


code_can.append(Canada_obj.value_per_item())
code_mor.append(Morocco_obj.value_per_item())
code_bra.append(Brazil_obj.value_per_item())
code_chi.append(China_obj.value_per_item())
code_fra.append(France_obj.value_per_item())




print(code_can[:])
print(code_mor[:])
print(code_bra[:])
print(code_chi[:])
print(code_fra[:])

