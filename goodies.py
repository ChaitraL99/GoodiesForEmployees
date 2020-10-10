#this function reads the data from input file and stores in a list called inputs and maps the item and price as key and value in goodies dict
def read_inputs():
    
    goodies={}
    no_of_employee=0
    
    with open(r"C:\Users\Admin\Desktop\GitHub\HighPeakSoftware\input_file.txt","r") as input_file:
        inputs=input_file.readlines()
    inputs=[x.strip() for x in inputs]
    
    for line in inputs:
        try:
            if line!="":
                temp=line.split(":")
                if temp[0]=="Number of employees":
                    no_of_employee=int(temp[1].strip())
                else:
                    goodies[temp[0]]=int(temp[1].strip())
        except ValueError:
            continue
    
    find_goodies(goodies,no_of_employee)


#this function gets goodies dict, no of employee as parameter and then sorts the dict based on value and is stored in a list
def find_goodies(goodies,no_of_employee):

    goodies_list=[]
    diff_list=[]
    
    sorted_goodies={item:price for item,price in sorted(goodies.items(), key=lambda elem:elem[1])}
    
    for k,v in sorted_goodies.items():
        
        temp=[k,v]
        goodies_list.append(temp)
    
    for i in range(len(goodies_list)):
        for j in range(i,i+no_of_employee):
            
            if i+no_of_employee<=len(goodies_list):
                diff=goodies_list[i+no_of_employee-1][1]-goodies_list[i][1]
                
        diff_list.append(diff)

    #index of minimum difference in list
    index=diff_list.index(min(diff_list))
    print_goodies(index,goodies_list,no_of_employee,min(diff_list))


#this function gets the index and writes the respective goodies to output_file.txt
def print_goodies(index,goodies_list,no_of_employee,diff):
    
    f=open(r"C:\Users\Admin\Desktop\GitHub\HighPeakSoftware\output_file.txt","w")
    
    print("Here the goodies that are selected for distribution are:")
    f.write("Here the goodies that are selected for distribution are: \n\n")
    print()
    
    for i in range(index,index+no_of_employee):
        print(goodies_list[i][0],":",goodies_list[i][1])
        f.write(""+repr(goodies_list[i][0])+":"+repr(goodies_list[i][1])+"\n")
    print()
    
    print("And the difference between the chosen goodie with highest price and the lowest price is ",diff)
    f.write("\n And the difference between the chosen goodie with highest price and the lowest price is "+repr(diff))
    
read_inputs()
