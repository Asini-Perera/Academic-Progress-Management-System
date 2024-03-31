

# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: W1953579 
# Date: 14.12.2022




#intialising the variables to 0
progress = 0
trailer = 0
retriever = 0
exclude = 0
number_range=range(0,121,20)
list_histogram=[]
list_outcome=[]
list_progress=[]
list_trailer=[]
list_retriever=[]
list_exclude=[]
# create input data function
def input_data(data="Pass"):
    while True:
        try:
            credit =int(input("Please enter your {} credits at : ".format(data)))
            if credit in number_range:
                    return credit
            else:
                        print("Out of range")
        except ValueError:
                print("Integer required")
#appending list data 
def get_list(list_histogram):
    list_histogram.append(pass_credits)
    list_histogram.append(defer_credits)
    list_histogram.append(fail_credits)
    
#print list
def print_list(progress,list_progress,list_type="Progress"):
    if progress >0:
            for i in range(0,len(list_progress),3):
                print("{} ".format(list_type),end="- ")
                print(",".join(map(str,list_progress[i:i+3])))
def printed_list():
                print_list(progress,list_progress,list_type="Progress")
                print_list(trailer,list_trailer,list_type="trailer")
                print_list(retriever,list_retriever,list_type="retriever")
                print_list(exclude,list_exclude,list_type="exclude")
                
def add_file(progress,list_progress,list_type="Progress"):
    if progress >0:
        file = open("list_file.txt","w")
        for i in range(0,len(list_progress),3):
            file.write(str("{} - ".format(list_type)))
            file.write(",".join(map(str,list_progress[i:i+3])))
            file.write('\n')
        file.close()
        file_print = open("list_file.txt","r")
        print(file_print.read())

#startup programme
print("......Welcome......\n If you are a Student press number     1\n If you are a staff press number     2")
menue=input("Enter your number: ")
while menue !='1' and menue !='2':
    print("Invalide Input")
    menue=input("Enter your number: ")
    print()
#student version
if menue == '1':
    while True:
        print()
        pass_credits=input_data()#using function for getting data
        defer_credits=input_data("defer")
        fail_credits=input_data("fail")
        #total calculation
        if pass_credits + defer_credits + fail_credits != 120:
            print("Total incorrect")
            continue
        #check the outcome
        elif pass_credits == 120:
                    print("Progress")
                    progress +=1
        elif pass_credits == 100:
                    print("Progress (module trailer)")
                    trailer +=1
        elif  80<= fail_credits <= 120:
                    print("Exclude")
                    exclude +=1
        else:
                 print(" module retriever ")
                 retriever +=1
        break
#staff version
if menue =='2':
    while True:
        while True:
             print()
             pass_credits=input_data()
             defer_credits=input_data("defer")
             fail_credits=input_data("fail")
             if pass_credits + defer_credits + fail_credits != 120:
                 print("Total incorrect")
                 continue
             elif pass_credits == 120:
                        print("Progress")
                        progress +=1
                        get_list(list_progress)
             elif pass_credits == 100:
                        print("Progress (module trailer)")
                        trailer +=1
                        get_list(list_trailer)
             elif  80<= fail_credits <= 120:
                        print("Exclude")
                        exclude +=1
                        get_list(list_exclude)
             else:
                     print("module retriever ")
                     retriever +=1
                     get_list(list_retriever)
             break
      
        total = progress + trailer + exclude + retriever
        print()
        
        print("Would you like to enter another set of data?")
        next_set=str(input("Enter 'y' for yes or 'q' to quit and view results: "))
        if next_set == "q":
            print("...........................................................................\n")
      #print histogram
            print("Histogram")
            if progress >0:
                print("Progress " ,progress, ": ","*"*progress)    
            if  trailer >0:
                print("Trailer ",trailer,": ","*"*trailer)
            if retriever >0:
                print("Retriever ",retriever,": ","*"*retriever)
            if exclude > 0:
                print("Exclude ",exclude,": ","*"*exclude)
            print()
            print(total," outcomes in total")
            print("....................................................................\n")
            add_file(progress,list_progress,list_type="Progress")
            add_file(trailer,list_trailer,list_type="trailer")
            add_file(retriever,list_retriever,list_type="retriever")
            add_file(exclude,list_exclude,list_type="exclude")
            break
        elif next_set == "y":
            continue
        else:
            while next_set!='y'and'q':
                print("Invalid Input")
                print()
                next_set=str(input("Enter 'y' for yes or 'q' to quit and view results: "))

 
                        
