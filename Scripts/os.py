import os 
def rename_files(path):
    for f in os.scandir(path):
        if f.is_dir():
            print(f.path)
            file_list = os.listdir(f.path)
            print(file_list)
        else:
            print(f.path)

    # rootPaths = os.listdir(path)
    # for r in rootPaths:
    #     print(path+r)
   

path = r"H:\Log"
# rename_files(path)

# def argument(arg1, *args): 
#     print ("First argument :", arg1) 
#     for arg in args: 
#         print("Tuple of *args :", arg) 
  
# argument('Hello World', 'Welcome', 'to python', '') 


# def Keyargument(**kwargs):  
#     for key, value in kwargs.items(): 
#         print ("%s == %s" %(key, value)) 
  
# # Driver code 
# Keyargument(first ='Breakfast', mid ='lunch', last='Dinner')

a = ["1.mp4","10.mp4","100.mp4","2.mp4","20.mp4","200.mp4"]
a = sorted(a, key=lambda x: int(x[:-4]))
print(a)