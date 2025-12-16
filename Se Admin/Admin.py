# edit and controle in admin of wep site
admin=["Ahmed","Nour","Ezz","Mohamed","Elzero"]

name= input("Enter you name:\n").capitalize().strip()

if name in admin:
    print("&"*6,"you are an admin ")
    
    # اساله عن اضفات 
    option=input('Do you want to [update =>u or remove=>r ] you name in admin \n').lower()
    
    if option =="update" or option=="u":#update
        new_name=input ("Enter your new name:").capitalize().strip()
        

        n=admin.index(name)#هيجيب رقم الاسم القديم
        admin.insert(n,new_name)#رقم اللي هيتعدل عليه
        admin.remove(name)
     
        print ("your name  was :" ,name, "now is =>",new_name," you stall admin ")
       
    elif option=="remove"or option=="r":#remove
        admin.remove(name)
        print (" now you aren't Mr : " ,name)
    
    else:# used case
        print ("invaild choice")
      
        
        
    
else:
    print ('you aren\'t an admin')
    
    option2=input ("do you want  be an admin(y /N ) or skip").lower().strip()
    
    if option2 in ["yes" ,"y"]:
        admin.append(name)
        print ("you are an admin  mr ",name)
        
    
    
    else:
        print ("you are nomal user ")
        