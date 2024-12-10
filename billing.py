from tkinter import *;
from tkinter import messagebox
import random,os,tempfile,smtplib
from PIL import Image, ImageTk
import requests


if not os.path.exists('bills'):         #If bills folder not exists for that purpose we imported os module
    os.mkdir('bills')                   #inside os module mkdir method will help to make folder bills


#functionality
billnumber=random.randint(500,1000)     #This will generate random values
def total():

    global soapvalue,faceCreamValue,faceWashValue,hairSprayValue,hairGelValue,bodyLotionValue,cosmeticsTotal,cosmeticTax,RiceValue,OilValue,DaalValue,wheatValue,sugarValue,teaValue,groceryTotal,groceryTax,MaazaValue,PepsiValue,spriteValue,DewValue,frootiValue,cocacolaValue,totalColdDrink,coldDrinksTax
    







    soapvalue=int(bathsoapEntry.get())*20
    faceCreamValue=int(faceCreamEntry.get())*50
    faceWashValue=int(faceWashEntry.get())*70
    hairSprayValue=int(hairSprayEntry.get())*75
    hairGelValue=int(hairGelEntry.get())*40
    bodyLotionValue=int(bodyLotionEntry.get())*100
    cosmeticsTotal=(soapvalue+faceCreamValue+faceWashValue+hairSprayValue+hairGelValue+bodyLotionValue)
    
    cosmeticPriceEntry.delete(0,END)        #Delete the initial value from start to end
    cosmeticPriceEntry.insert(0,str(cosmeticsTotal)+" Rs")   #this will insert total in entry field

    cosmeticTax=cosmeticsTotal*0.12
    cosmeticTaxEntry.delete(0,END)
    cosmeticTaxEntry.insert(0,str(cosmeticTax)+" Rs")

#==============
    RiceValue=int(RiceEntry.get())*30
    OilValue=int(OilEntry.get())*100
    DaalValue=int(DaalEntry.get())*120
    wheatValue=int(wheatEntry.get())*50
    sugarValue=int(sugarEntry.get())*30
    teaValue=int(teaEntry.get())*50

    groceryTotal=(RiceValue+OilValue+DaalValue+wheatValue+sugarValue+teaValue)
    groceryPriceEntry.delete(0,END)         #Delete the initial value from start to end
    groceryPriceEntry.insert(0,str(groceryTotal)+" Rs")

    groceryTax=groceryTotal*0.05
    groceryTaxEntry.delete(0,END)
    groceryTaxEntry.insert(0,str(groceryTax)+" Rs")


#=====================
    MaazaValue=int(MaazaEntry.get())*40
    PepsiValue=int(PepsiEntry.get())*40
    spriteValue=int(spriteEntry.get())*40
    DewValue=int(DewEntry.get())*40
    frootiValue=int(frootiEntry.get())*40
    cocacolaValue=int(cocacolaEntry.get())*40

    totalColdDrink=(MaazaValue+PepsiValue+spriteValue+DewValue+frootiValue+cocacolaValue)
    coldDrinksPriceEntry.delete(0,END)  #Delete the initial value from start to end
    coldDrinksPriceEntry.insert(0,str(totalColdDrink)+" Rs")

    coldDrinksTax=totalColdDrink*0.08
    coldDrinksTaxEntry.delete(0,END)
    coldDrinksTaxEntry.insert(0,str(coldDrinksTax)+" Rs")


# ================================================
def bill_area():
    if(nameEntry.get()=='' or  PhoneNumberEntry.get()==""):
        messagebox.showerror("Error","Customer Details are Required")
    elif cosmeticPriceEntry.get()=="" and groceryPriceEntry.get()=="" and coldDrinksPriceEntry.get()=="":
        messagebox.showerror("Error","Please Select the Items")
    elif cosmeticPriceEntry.get()==0 and groceryPriceEntry.get()==0 and coldDrinksPriceEntry.get()==0:
        messagebox.showerror("Error","No Products are Selected")
    else:
        textarea.delete(1.0,END)

        textarea.insert(END,"\t\t**Welcome Customer**\n\n")
        textarea.insert(END,f'Bill Number :{billnumber}\n')
        textarea.insert(END,f'Customer Name :{nameEntry.get()}\n')
        textarea.insert(END,f'Phone Number :{PhoneNumberEntry.get()}\n')
        textarea.insert(END,"=======================================================")
        textarea.insert(END,"Products\t\t\tQTY\t\t\tPrice\n")
        textarea.insert(END,"=======================================================")

    if bathsoapEntry.get()!='0':
        textarea.insert(END,f'Bath Soap\t\t\t{bathsoapEntry.get()}\t\t\t{soapvalue} Rs\n')

    if faceCreamEntry.get()!='0':
        textarea.insert(END,f'Face Cream\t\t\t{faceCreamEntry.get()}\t\t\t{faceCreamValue} Rs\n')

    if faceWashEntry.get()!='0':
        textarea.insert(END,f'Face Wash\t\t\t{faceWashEntry.get()}\t\t\t{faceWashValue} Rs\n')

    if hairSprayEntry.get()!='0':
        textarea.insert(END,f'Hair Spray\t\t\t{hairSprayEntry.get()}\t\t\t{hairSprayValue} Rs\n')

    if hairGelEntry.get()!='0':
        textarea.insert(END,f'Hair Gel\t\t\t{hairGelEntry.get()}\t\t\t{hairGelValue} Rs\n')

    if bodyLotionEntry.get()!='0':
        textarea.insert(END,f'Body Lotion\t\t\t{bodyLotionEntry.get()}\t\t\t{bodyLotionValue} Rs\n')

    if RiceEntry.get()!='0':
        textarea.insert(END,f'Rice\t\t\t{RiceEntry.get()}\t\t\t{RiceValue} Rs\n')

    if OilEntry.get()!='0':
        textarea.insert(END,f'Oil\t\t\t{OilEntry.get()}\t\t\t{OilValue} Rs\n')

    if DaalEntry.get()!='0':
        textarea.insert(END,f'Daal\t\t\t{DaalEntry.get()}\t\t\t{DaalValue} Rs\n')

    if wheatEntry.get()!='0':
        textarea.insert(END,f'Wheat\t\t\t{wheatEntry.get()}\t\t\t{wheatValue} Rs\n')
    
    if sugarEntry.get()!='0':
        textarea.insert(END,f'Sugar\t\t\t{sugarEntry.get()}\t\t\t{sugarValue} Rs\n')

    if teaEntry.get()!='0':
        textarea.insert(END,f'Tea\t\t\t{teaEntry.get()}\t\t\t{teaValue} Rs\n')

    if MaazaEntry.get()!='0':
        textarea.insert(END,f'Maaza\t\t\t{MaazaEntry.get()}\t\t\t{MaazaValue} Rs\n')

    if PepsiEntry.get()!='0':
        textarea.insert(END,f'Pepsi\t\t\t{PepsiEntry.get()}\t\t\t{PepsiValue} Rs\n')

    if spriteEntry.get()!='0':
        textarea.insert(END,f'Sprite\t\t\t{spriteEntry.get()}\t\t\t{spriteValue} Rs\n')

    if DewEntry.get()!='0':
        textarea.insert(END,f'Dew\t\t\t{DewEntry.get()}\t\t\t{DewValue} Rs\n')

    if frootiEntry.get()!='0':
        textarea.insert(END,f'Frooti\t\t\t{frootiEntry.get()}\t\t\t{frootiValue} Rs\n')

    if cocacolaEntry.get()!='0':
        textarea.insert(END,f'Coca Cola\t\t\t{cocacolaEntry.get()}\t\t\t{cocacolaValue} Rs\n')
        textarea.insert(END,"-------------------------------------------------------")

    if cosmeticTaxEntry.get()!='0.0':
        textarea.insert(END,f'Cosmetic Tax\t\t\t\t{round(cosmeticTax)}\n')
    if groceryTaxEntry.get()!='0.0':
        textarea.insert(END,f'Grocery Tax\t\t\t\t{round(groceryTax)}\n')
    if coldDrinksTaxEntry.get()!='0.0':
        textarea.insert(END,f'Cold Drink Tax\t\t\t\t{round(coldDrinksTax)}\n\n')

    totalbill=(cosmeticsTotal+groceryTotal+totalColdDrink+cosmeticTax+groceryTax+coldDrinksTax)
    textarea.insert(END,f'Total Bill\t\t\t\t{round(totalbill,2)} Rs\n')
    textarea.insert(END,"-------------------------------------------------------")

    save_bill()
# ========================================
def save_bill():
    global billnumber
    result=messagebox.askyesno("Confirm","Do You Want to Save")
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f'bills/ {billnumber}.text','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo("Success",f'Bill Number {billnumber} is saved successfully')
        billnumber=random.randint(500,1000)     #we have added this random over here to update bill number
        

#=========================================================

def search_bill():
    for i in os.listdir("bills/"):      #os.listdr() will list all files present in bills folder by using for loop
        
        if (int(i.split('.')[0])==int(BillNumberEntry.get())):
        
            f=open(f'bills/{i}','r')         #open the folder with file in read mode
            textarea.delete(1.0,END)        #delete all the text present at textarea
            for data in f:
                textarea.insert(END,data)
            f.close()
            break
    else:
        messagebox.showerror("Error","Invalid Bill Number")

# =======================================
def print_bill():
    if textarea.get(1.0,END)=="\n":
        messagebox.showerror("Error","Bill is Empty")
    else:
        file=tempfile.mktemp('.txt')        #tempfile.mktemp will create an temporary file
        open(file,'w').write(textarea.get(1.0,END))     #we have to open file in write mode and write the content present in textarea
        os.startfile(file,'print')      #os will startfile operation for that we have to give file name and command
        
# =======================================================
'''
def send_email():
    global senderEmailEntry,receiverEntry,passwordEntry
    if textarea.get(1.0,END)=="\n":
        messagebox.showerror("Error","Bill is Empty")
    else:
        root1=Toplevel()
        root1.title("Send Gmail")
        root1.geometry("570x600")
        root1.config(bg="PaleGreen4")

        senderFrame=LabelFrame(root1,text="SENDER",font=("Arial",16,"bold"),bg="PaleGreen4",bd=8,fg="white")
        senderFrame.grid(row=0,column=0,padx=40,pady=20)
        
        senderEmail=Label(senderFrame,text="Sender's Email",font=("Arial",14,"bold"),fg="white",bg="PaleGreen4")
        senderEmail.grid(row=0,column=0,padx=10,pady=8)

        senderEmailEntry=Entry(senderFrame,font=("Arial",16,"bold"),bd=2,relief="ridge",width=23)
        senderEmailEntry.grid(row=0,column=1,padx=10,pady=8)

        passwordEmail=Label(senderFrame,text="Password",font=("Arial",14,"bold"),fg="white",bg="PaleGreen4")
        passwordEmail.grid(row=1,column=0,padx=10,pady=8)

        passwordEntry=Entry(senderFrame,font=("Arial",16,"bold"),bd=2,relief="ridge",width=23,show="*")
        passwordEntry.grid(row=1,column=1,padx=10,pady=8)

        recipientFrame=LabelFrame(root1,text="RECIPIENT",font=("Arial",16,"bold"),bg="PaleGreen4",bd=8,fg="white")
        recipientFrame.grid(row=1,column=0,padx=40,pady=20)

        
        receiverEmail=Label(recipientFrame,text="Email Address",font=("Arial",14,"bold"),fg="white",bg="PaleGreen4")
        receiverEmail.grid(row=0,column=0,padx=10,pady=8)

        receiverEntry=Entry(recipientFrame,font=("Arial",16,"bold"),bd=2,relief="ridge",width=23)
        receiverEntry.grid(row=0,column=1,padx=10,pady=8)

        messageLabel=Label(recipientFrame,text="Message",font=("Arial",14,"bold"),fg="white",bg="PaleGreen4")
        messageLabel.grid(row=1,column=0,padx=10,pady=8)

        email_text_area=Text(recipientFrame,font=("Arial",12,"bold"),bd=2,relief="sunken",width=45,height=12)
        email_text_area.grid(row=2,column=0,columnspan=2)


        email_text_area.delete(1.0,END)
        email_text_area.insert(END,textarea.get(1.0,END).replace("=",'').replace("-","").replace("\t\t\t","\t\t"))

        sendButton=Button(root1,text="SEND",font=("Arial",14,"bold"),relief="groove",width=15,command=send_gmail)
        sendButton.grid(row=2,column=0,pady=10)

        root1.mainloop()
'''
        
def send_gmail():
    try:
        # ob=smtplib.SMTP('smtp.gmail.com',587)
        # ob.starttls()       #This will make connection secure
        # ob.login(senderEmailEntry.get(),passwordEntry.get())
        # message=email_text_area.get(1.0,END)
        # # receiver_address=receiverEntry.get()
        # ob.sendmail(senderEmailEntry.get(),receiverEntry.get(),message)
        # ob.quit()
        messagebox.info("Success","Bill sent Successfully")
        root1.destroy()
    except:
        messagebox.showerror("Error","Something went wrong")





#============================
def send_bill():


    # def send_msg():
    #     message = mobileTextArea.get(1.0, "end-1c")
    #     print("Message:", message)
    
    #     number = numberEntry.get()    
    #     print("Number:", number)

    #     url = "https://www.fast2sms.com/dev/bulkV2"
    #     querystring = {
    #         'authorization': "lLGHk5tAgYhSOv0qtCvAn4LAWEPfu4WaAAj2eVR8MUYAA5OF8GEqAyeEGC2s",
    #         'message': message,
    #         'language': "english",
    #         'route': "q",
    #         'numbers': number
    #  }

    #     headers = {'cache-control': "no-cache"}

    #     response = requests.request("GET", url, headers=headers, params=querystring)

    #     # Print the entire response content
    #     print("Response Content:", response.text)

    #     try:
    #         dict_response = response.json()
    #         result = dict_response.get("return")

    #         if result is True:
    #             messagebox.showinfo("Success", "Message Sent Successfully")
    #         else:
    #             messagebox.showerror("Failure", "Something Went Wrong")
    #     except Exception as e:
    #         print("Error parsing JSON response:", e)
    #         messagebox.showerror("Failure", "Error Parsing Response")
	def send_msg():
            # message=mobileTextArea.get(1.0,END)
            message = mobileTextArea.get(1.0, "end-1c")
            print(message)
            number=numberEntry.get()    
            print(number)



            # url = "https://www.fast2sms.com/dev/bulkV2"
            # querystring = {'authorization':"lLGHk5tAgYhSOv0qtCvAn4LAWEPfu4WaAAj2eVR8MUYAA5OF8GEqAyeEGC2s","message":message,"language":"english","route":"q","numbers":number}
            url = "https://www.fast2sms.com/dev/bulkV2"
            querystring = {
            'authorization': "lLGHk5tAgYhSOv0qtCvAn4LAWEPfu4WaAAj2eVR8MUYAA5OF8GEqAyeEGC2s",
            'message': message,
            'language': "english",
            'route': "",
            'numbers': number
     }      
            headers = {'cache-control': "no-cache"}

            response = requests.request("GET", url, headers=headers, params=querystring)

          
            # headers = {
            #   'cache-control': "no-cache"
            #     }
            # response = requests.request("GET", url, headers=headers, params=querystring)
            
            print("Response Content:", response.text)

            try:
                dict_response = response.json()
                result = dict_response.get("return")

                if result is True:
                    messagebox.showinfo("Success", "Message Sent Successfully")
                else:
                    messagebox.showerror("Failure", "Something Went Wrong")
            except Exception as e:
                print("Error parsing JSON response:", e)
                messagebox.showerror("Failure", "Error Parsing Response")

            # dict=response.json()
            # result=dict.get("return")
            # print(result)
            # if result==True:
            #     messagebox.showinfo("Success","Message Sent Successfully")
            # else:
            #     messagebox.showerror("Faliure","Something Went Wrong")

            # auth="2ZwF2nCOnTVgtmLS8VFfQOlDCxF0Mhg41Rm1syhpZZ9lDYUikFPWAlhW85v4"
            # url="https://www.fast2sms.com/dev/bulkV2"
            # params={
            # 'authorization':auth,
            # 'message':message,
            # 'number':number,
            # 'sender-id':'FSTSMS',
            # 'route':'sltsms',
            # 'language':'english'
            
            
            #  }
            # response=requests.get(url,params=params)
            # print(response)
          

            # dict=response.json()
            # result=dict.get("return")
            # print(result)
            # if result==True:
            #     messagebox.showinfo("Success","Message Sent Successfully")
            # else:
            #     messagebox.showerror("Faliure","Something Went Wrong")

	root2=Toplevel()
	root2.title("Send Bill")
	root2.geometry("570x600")
	root2.config(bg="PaleGreen4")
	root2.iconbitmap("Images/icon.ico")
	numberLabel=Label(root2,text="Mobile Number",font=("Arial",18,"bold underline"),bg="PaleGreen4",fg="RosyBrown2",bd=12,relief="groove")
	numberLabel.pack(pady=5)
	
	numberEntry=Entry(root2,font=("helvetica",22,"bold"),bd=3,width=24)
	numberEntry.pack(pady=5)

	billLabel=Label(root2,text="Bill Details",font=("Arial",18,"bold underline"),bg="PaleGreen4",fg="RosyBrown2",bd=12,relief="groove")
	billLabel.pack(pady=5)
	mobileTextArea=Text(root2,font=("Arial",12,"bold"),bd=3,width=42,height=12)
    
	mobileTextArea.pack(pady=5)
	mobileTextArea.delete(1.0,END)
	mobileTextArea.insert(END,textarea.get(1.0,END).replace("=",'').replace("-","").replace("\t\t\t","\t\t"))


    
    

	sendButton=Button(root2,text="SEND",font=("Arial",14,"bold"),relief="groove",width=15,command=send_msg)
	sendButton.pack(pady=5)
    


	root2.mainloop()

# =========================================================================
def pay():
    root3=Toplevel()
    root3.title("Online Payement")
    root3.geometry("570x600")
    root3.config(bg="PaleGreen4")
    root3.iconbitmap("Images/icon.ico")
    img1=Image.open('Images/Varun_QR_CODE.jpg')
    img1=img1.resize((300,300),Image.LANCZOS)
    root3.resizable(False, False)
    root3.photo1=ImageTk.PhotoImage(img1)
    label=Label(root3,text="Scan On QR Code For Online Payment",font=("Arial",20,"bold"),bg="black",fg="yellow",bd=3,relief="groove")
    label.pack(pady=8)
    root3.img_1=Label(root3,image=root3.photo1)
    root3.img_1.place(x=70,y=70,width=400,height=500)
    root3.mainloop()

    

# ========================
def clear():
    bathsoapEntry.delete(0,END)
    faceCreamEntry.delete(0,END)
    faceWashEntry.delete(0,END)
    hairSprayEntry.delete(0,END)
    hairGelEntry.delete(0,END)
    bodyLotionEntry.delete(0,END)
    RiceEntry.delete(0,END)
    OilEntry.delete(0,END)
    DaalEntry.delete(0,END)
    wheatEntry.delete(0,END)
    sugarEntry.delete(0,END)
    teaEntry.delete(0,END)
    MaazaEntry.delete(0,END)
    PepsiEntry.delete(0,END)
    DewEntry.delete(0,END)
    frootiEntry.delete(0,END)
    cocacolaEntry.delete(0,END)
    spriteEntry.delete(0,END)


    bathsoapEntry.insert(0,0)
    faceCreamEntry.insert(0,0)
    faceWashEntry.insert(0,0)
    hairSprayEntry.insert(0,0)
    hairGelEntry.insert(0,0)
    bodyLotionEntry.insert(0,0)
    RiceEntry.insert(0,0)
    OilEntry.insert(0,0)
    DaalEntry.insert(0,0)
    wheatEntry.insert(0,0)
    sugarEntry.insert(0,0)
    teaEntry.insert(0,0)
    MaazaEntry.insert(0,0)
    PepsiEntry.insert(0,0)
    DewEntry.insert(0,0)
    frootiEntry.insert(0,0)
    cocacolaEntry.insert(0,0)
    spriteEntry.insert(0,0)


    groceryPriceEntry.delete(0,END)
    cosmeticPriceEntry.delete(0,END)
    coldDrinksPriceEntry.delete(0,END)

    PhoneNumberEntry.delete(0,END)
    nameEntry.delete(0,END)
    BillNumberEntry.delete(0,END)

    groceryTaxEntry.delete(0,END)
    cosmeticTaxEntry.delete(0,END)
    coldDrinksTaxEntry.delete(0,END)

    textarea.delete(1.0,END)











root=Tk()    #root is the object of class TK
root.geometry('1920x1080')
root.title("Retail Billing System")
root.iconbitmap("Images/icon.ico")
headingLabel=Label(root,
text="Retail Billing System",font=("times new roman",30,"bold"),bg="PaleGreen4",fg="RosyBrown2",bd=12,relief="groove")
headingLabel.pack(fill=X,pady=8)
#=============
customer_details_frame=LabelFrame(root,text="Customer Details",font=("times new roman",15,"bold"),fg="greenyellow",bg="PaleGreen4",bd=8,relief="groove")
customer_details_frame.pack(fill=X)
nameLabel=Label(customer_details_frame,text="Name ",font=("Arial",16),bg="PaleGreen4",fg="lavenderblush")
nameLabel.grid(row=0,column=0,padx=10)
nameEntry=Entry(customer_details_frame,font=("Arial",12),bd=6,width=22)
nameEntry.grid(row=0,column=1)

PhoneNumberLabel=Label(customer_details_frame,text="Phone Number ",font=("Arial",16),bg="PaleGreen4",fg="lavenderblush")
PhoneNumberLabel.grid(row=0,column=2,padx=10)
PhoneNumberEntry=Entry(customer_details_frame,font=("Arial",12),bd=6,width=20)
PhoneNumberEntry.grid(row=0,column=3)

BillNumberLabel=Label(customer_details_frame,text="Bill Number ",font=("Arial",16),bg="PaleGreen4",fg="lavenderblush")
BillNumberLabel.grid(row=0,column=4,padx=10)
BillNumberEntry=Entry(customer_details_frame,font=("Arial",12),bd=6,width=20)
BillNumberEntry.grid(row=0,column=5)

btnSearch=Button(customer_details_frame,text="Search",font=("times new roman",12,"bold"),bd=8,relief="raised",width=15,command=search_bill)
btnSearch.grid(row=0,column=6,padx=65,pady=5)

#============
productsFrame=Frame(root)
productsFrame.pack(pady=7,fill=X)

cosmeticsLabelFrame=LabelFrame(productsFrame,text="Cosmetics",font=("times new roman",15,"bold"),fg="greenyellow",bg="PaleGreen4",bd=8,relief="groove")
cosmeticsLabelFrame.grid(row=0,column=0,padx=5)

bathsoapLabel=Label(cosmeticsLabelFrame,text="Bath Soap",font=("Arial",14),bg="PaleGreen4",fg="lavenderblush")
bathsoapLabel.grid(row=0,column=0,padx=8,sticky="w")
bathsoapEntry=Entry(cosmeticsLabelFrame,font=("Arial",12),bd=6,width=10)
bathsoapEntry.grid(row=0,column=1,padx=15,pady=5)
bathsoapEntry.insert(0,0)

faceCreamLabel=Label(cosmeticsLabelFrame,text="Face Cream",font=("Arial",14),bg="PaleGreen4",fg="lavenderblush")
faceCreamLabel.grid(row=1,column=0,padx=8,sticky="w")
faceCreamEntry=Entry(cosmeticsLabelFrame,font=("Arial",12),bd=6,width=10)
faceCreamEntry.grid(row=1,column=1,padx=15,pady=5)
faceCreamEntry.insert(0,0)

faceWashLabel=Label(cosmeticsLabelFrame,text="Face Wash",font=("Arial",14),bg="PaleGreen4",fg="lavenderblush")
faceWashLabel.grid(row=2,column=0,padx=8,sticky="w")
faceWashEntry=Entry(cosmeticsLabelFrame,font=("Arial",12),bd=6,width=10)
faceWashEntry.grid(row=2,column=1,padx=15,pady=5)
faceWashEntry.insert(0,0)

hairSprayLabel=Label(cosmeticsLabelFrame,text="Hair Spray",font=("Arial",14),bg="PaleGreen4",fg="lavenderblush")
hairSprayLabel.grid(row=3,column=0,padx=8,sticky="w")
hairSprayEntry=Entry(cosmeticsLabelFrame,font=("Arial",12),bd=6,width=10)
hairSprayEntry.grid(row=3,column=1,padx=15,pady=5)
hairSprayEntry.insert(0,0)

hairGelLabel=Label(cosmeticsLabelFrame,text="Hair Gel",font=("Arial",14),bg="PaleGreen4",fg="lavenderblush")
hairGelLabel.grid(row=4,column=0,padx=8,sticky="w")
hairGelEntry=Entry(cosmeticsLabelFrame,font=("Arial",12),bd=6,width=10)
hairGelEntry.grid(row=4,column=1,padx=15,pady=5)
hairGelEntry.insert(0,0)

bodyLotionLabel=Label(cosmeticsLabelFrame,text="Body Lotion",font=("Arial",14),bg="PaleGreen4",fg="lavenderblush")
bodyLotionLabel.grid(row=5,column=0,padx=8,sticky="w")
bodyLotionEntry=Entry(cosmeticsLabelFrame,font=("Arial",12),bd=6,width=10)
bodyLotionEntry.grid(row=5,column=1,padx=15,pady=5)
bodyLotionEntry.insert(0,0)

#==========
GroceryLabelFrame=LabelFrame(productsFrame,text="Grocery",font=("times new roman",15,"bold"),fg="greenyellow",bg="PaleGreen4",bd=8,relief="groove")
GroceryLabelFrame.grid(row=0,column=1,padx=4)

RiceLabel=Label(GroceryLabelFrame,text="Rice",font=("Arial",14),bg="PaleGreen4",fg="lavenderblush")
RiceLabel.grid(row=0,column=0,padx=8,sticky="w")
RiceEntry=Entry(GroceryLabelFrame,font=("Arial",12),bd=6,width=10)
RiceEntry.grid(row=0,column=1,padx=15,pady=5)
RiceEntry.insert(0,0)

OilLabel=Label(GroceryLabelFrame,text="Oil",font=("Arial",14),bg="PaleGreen4",fg="lavenderblush")
OilLabel.grid(row=1,column=0,padx=8,sticky="w")
OilEntry=Entry(GroceryLabelFrame,font=("Arial",12),bd=6,width=10)
OilEntry.grid(row=1,column=1,padx=15,pady=5)
OilEntry.insert(0,0)

DaalLabel=Label(GroceryLabelFrame,text="Daal",font=("Arial",14),bg="PaleGreen4",fg="lavenderblush")
DaalLabel.grid(row=2,column=0,padx=8,sticky="w")
DaalEntry=Entry(GroceryLabelFrame,font=("Arial",12),bd=6,width=10)
DaalEntry.grid(row=2,column=1,padx=15,pady=5)
DaalEntry.insert(0,0)

wheatLabel=Label(GroceryLabelFrame,text="Wheat",font=("Arial",14),bg="PaleGreen4",fg="lavenderblush")
wheatLabel.grid(row=3,column=0,padx=8,sticky="w")
wheatEntry=Entry(GroceryLabelFrame,font=("Arial",12),bd=6,width=10)
wheatEntry.grid(row=3,column=1,padx=15,pady=5)
wheatEntry.insert(0,0)

sugarLabel=Label(GroceryLabelFrame,text="Sugar",font=("Arial",14),bg="PaleGreen4",fg="lavenderblush")
sugarLabel.grid(row=4,column=0,padx=8,sticky="w")
sugarEntry=Entry(GroceryLabelFrame,font=("Arial",12),bd=6,width=10)
sugarEntry.grid(row=4,column=1,padx=15,pady=5)
sugarEntry.insert(0,0)

teaLabel=Label(GroceryLabelFrame,text="Tea",font=("Arial",14),bg="PaleGreen4",fg="lavenderblush")
teaLabel.grid(row=5,column=0,padx=8,sticky="w")
teaEntry=Entry(GroceryLabelFrame,font=("Arial",12),bd=6,width=10)
teaEntry.grid(row=5,column=1,padx=15,pady=5)
teaEntry.insert(0,0)

# ==========
coldDrinksLabelFrame=LabelFrame(productsFrame,text="Cold Drinks",font=("times new roman",15,"bold"),fg="greenyellow",bg="PaleGreen4",bd=8,relief="groove")
coldDrinksLabelFrame.grid(row=0,column=2,padx=4)

MaazaLabel=Label(coldDrinksLabelFrame,text="Maaza",font=("Arial",14),bg="PaleGreen4",fg="lavenderblush")
MaazaLabel.grid(row=0,column=0,padx=8,sticky="w")
MaazaEntry=Entry(coldDrinksLabelFrame,font=("Arial",12),bd=6,width=10)
MaazaEntry.grid(row=0,column=1,padx=15,pady=5)
MaazaEntry.insert(0,0)

PepsiLabel=Label(coldDrinksLabelFrame,text="Pepsi",font=("Arial",14),bg="PaleGreen4",fg="lavenderblush")
PepsiLabel.grid(row=1,column=0,padx=8,sticky="w")
PepsiEntry=Entry(coldDrinksLabelFrame,font=("Arial",12),bd=6,width=10)
PepsiEntry.grid(row=1,column=1,padx=15,pady=5)
PepsiEntry.insert(0,0)

spriteLabel=Label(coldDrinksLabelFrame,text="Sprite",font=("Arial",14),bg="PaleGreen4",fg="lavenderblush")
spriteLabel.grid(row=2,column=0,padx=8,sticky="w")
spriteEntry=Entry(coldDrinksLabelFrame,font=("Arial",12),bd=6,width=10)
spriteEntry.grid(row=2,column=1,padx=15,pady=5)
spriteEntry.insert(0,0)

DewLabel=Label(coldDrinksLabelFrame,text="Dew",font=("Arial",16),bg="PaleGreen4",fg="lavenderblush")
DewLabel.grid(row=3,column=0,padx=8,sticky="w")
DewEntry=Entry(coldDrinksLabelFrame,font=("Arial",12),bd=6,width=10)
DewEntry.grid(row=3,column=1,padx=15,pady=5)
DewEntry.insert(0,0)

frootiLabel=Label(coldDrinksLabelFrame,text="Frooti",font=("Arial",14),bg="PaleGreen4",fg="lavenderblush")
frootiLabel.grid(row=4,column=0,padx=8,sticky="w")
frootiEntry=Entry(coldDrinksLabelFrame,font=("Arial",12),bd=6,width=10)
frootiEntry.grid(row=4,column=1,padx=15,pady=5)
frootiEntry.insert(0,0)

cocacolaLabel=Label(coldDrinksLabelFrame,text="Coca Cola",font=("Arial",14),bg="PaleGreen4",fg="lavenderblush")
cocacolaLabel.grid(row=5,column=0,padx=8,sticky="w")
cocacolaEntry=Entry(coldDrinksLabelFrame,font=("Arial",12),bd=6,width=10)
cocacolaEntry.grid(row=5,column=1,padx=15,pady=5)
cocacolaEntry.insert(0,0)

# ===========
billFrame=Label(productsFrame,bd=8,relief="sunken")
billFrame.grid(row=0,column=3)


billareaLabel=Label(billFrame,text="Bill Area",font=("Arial",14,"bold"),bg="white",fg="black",bd=7,relief="groove")
billareaLabel.pack(fill=X)

scrollBar=Scrollbar(billFrame,orient=VERTICAL)
scrollBar.pack(side="right",fill=Y)


textarea=Text(billFrame,height=14.3,width=55,yscrollcommand=scrollBar.set)          #yscrollcommand will set the scroll bar with the textarea
textarea.pack(padx=5)
scrollBar.config(command=textarea.yview)
# ===============

billMenuFrame=LabelFrame(root,text="Bill Menu",font=("times new roman",15,"bold"),fg="greenyellow",bg="PaleGreen4",bd=8,relief="groove")
billMenuFrame.pack(fill=X)

cosmeticPriceLabel=Label(billMenuFrame,text="Cosmetic Price",font=("Arial",14),bg="PaleGreen4",fg="lavenderblush")
cosmeticPriceLabel.grid(row=0,column=0,padx=8,sticky="w")
cosmeticPriceEntry=Entry(billMenuFrame,font=("Arial",12),bd=6,width=11)
cosmeticPriceEntry.grid(row=0,column=1,padx=12,pady=5)

groceryPriceLabel=Label(billMenuFrame,text="Grocery Price",font=("Arial",14),bg="PaleGreen4",fg="lavenderblush")
groceryPriceLabel.grid(row=1,column=0,padx=8,sticky="w")
groceryPriceEntry=Entry(billMenuFrame,font=("Arial",12),bd=6,width=11)
groceryPriceEntry.grid(row=1,column=1,padx=12,pady=5)

coldDrinksPriceLabel=Label(billMenuFrame,text="Cold Drink Price",font=("Arial",14),bg="PaleGreen4",fg="lavenderblush")
coldDrinksPriceLabel.grid(row=2,column=0,padx=8,sticky="w")
coldDrinksPriceEntry=Entry(billMenuFrame,font=("Arial",12),bd=6,width=11)
coldDrinksPriceEntry.grid(row=2,column=1,padx=12,pady=5)


cosmeticTaxLabel=Label(billMenuFrame,text="Cosmetic Tax",font=("Arial",14),bg="PaleGreen4",fg="lavenderblush")
cosmeticTaxLabel.grid(row=0,column=2,padx=8,sticky="w")
cosmeticTaxEntry=Entry(billMenuFrame,font=("Arial",12),bd=6,width=11)
cosmeticTaxEntry.grid(row=0,column=3,padx=12,pady=5)

groceryTaxLabel=Label(billMenuFrame,text="Grocery Tax",font=("Arial",14),bg="PaleGreen4",fg="lavenderblush")
groceryTaxLabel.grid(row=1,column=2,padx=8,sticky="w")
groceryTaxEntry=Entry(billMenuFrame,font=("Arial",12),bd=6,width=11)
groceryTaxEntry.grid(row=1,column=3,padx=12,pady=5)

coldDrinksTaxLabel=Label(billMenuFrame,text="Cold Drink Tax",font=("Arial",14),bg="PaleGreen4",fg="lavenderblush")
coldDrinksTaxLabel.grid(row=2,column=2,padx=8,sticky="w")
coldDrinksTaxEntry=Entry(billMenuFrame,font=("Arial",12),bd=6,width=11)
coldDrinksTaxEntry.grid(row=2,column=3,padx=12,pady=5)

buttonFrame=Frame(billMenuFrame,bd=8,relief="groove",padx=4)
buttonFrame.grid(row=0,column=4,rowspan=3)

totalButton=Button(buttonFrame,text="Total",font=("Arial",15,"bold"),fg="white",bg="PaleGreen4",width=6,pady=4,bd=6,relief="raised",command=total)
totalButton.grid(row=0,column=0,pady=23.7,padx=7)

billButton=Button(buttonFrame,text="Bill",font=("Arial",15,"bold"),fg="white",bg="PaleGreen4",width=6,pady=4,bd=6,relief="raised",command=bill_area)
billButton.grid(row=0,column=1,pady=23.7,padx=7)

emailButton=Button(buttonFrame,text="Send",font=("Arial",15,"bold"),fg="white",bg="PaleGreen4",width=6,pady=4,bd=6,relief="raised",command=send_bill)
emailButton.grid(row=0,column=2,pady=23.7,padx=7)

printButton=Button(buttonFrame,text="Print",font=("Arial",15,"bold"),fg="white",bg="PaleGreen4",width=6,pady=4,bd=6,relief="raised",command=print_bill)
printButton.grid(row=0,column=3,pady=23.7,padx=7)

payButton=Button(buttonFrame,text="Pay",font=("Arial",15,"bold"),fg="white",bg="PaleGreen4",width=6,pady=4,bd=6,relief="raised",command=pay)
payButton.grid(row=0,column=4,pady=23.7,padx=7)
clearButton=Button(buttonFrame,text="Clear",font=("Arial",15,"bold"),fg="white",bg="PaleGreen4",width=6,pady=4,bd=6,relief="raised",command=clear)
clearButton.grid(row=0,column=5,pady=23.7,padx=7)

















root.mainloop()         #mainloop method holds our tkinter window desktop application