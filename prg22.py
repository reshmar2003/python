import pickle

#phonebook={
#    'a':'1',
#    'b':'2',
#    'c':'3'
#}

#with open('phonebook.dat','wb') as bin:
#    pickle.dump(phonebook,bin)



with open('phonebook.dat','rb') as bin:
    data=pickle.load(bin)
    print(type(data))
    print(data)
