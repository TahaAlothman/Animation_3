# f=open('text1.txt','r')          # open file and just read it(create a file if it doesn't exist)
# data=f.readlines()           
# for i in data:
#     print(i)
       
# f=open('text2.txt','w')              # Delete the data and write something new(create a file if it doesn't exist)   
# f.write('TahaAlothman')
# f.close()


# f=open('text3.txt','r')               #add to data  something new at specific position(create a file if it doesn't exist)
# data=f.readlines()
# f.close()
# data.insert(2,'TahaAlothman')
# for i in data:
#     print(i)


# f=open('text4.txt','a')               #add to data  something new(if a file doesn't exist,error!)
# f.write('Python')
# f.close()




#in the past when we didn't write f.close(), there was error, and we fixed this error like this
# with open('mystro.txt','a') as file:
    # file.write('Test.............')