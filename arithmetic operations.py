def Operator(operator):
    if operator == '+' or operator == '-':
        return True 
    return False

def Numbers(num):
    for n in num:
        if n.isdigit():
            continue
        else:
          return False
    return True
def arithmetic_arranger(operations,result):
   if len(operations)>5:
       return "Too many problems."
   for op in operations:
       lst=op.split()
       if Operator(lst[1])==False:
           return "Operator must be '+' or '-'"
       if Numbers(lst[0])==False or Numbers(lst[2])==False:
           return "Numbers must only contain digits"
       if len (lst[0]) > 4 or len (lst[2]) >4:
           return "Numbers cannot be more than four digits"
       print (" "+lst[0])
       print (lst[1])
       print (lst[2])
       dashes=""
       for i in range(len(lst[0])+len(lst[2])+1):
           dashes+="-"
           i+=1
       print (dashes)
       if result== True:
           print (int (lst[0])+int(lst[2]))
   
