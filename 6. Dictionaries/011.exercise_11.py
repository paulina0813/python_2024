'''
Exercise 11
The directory of a company's customers is organized in a text string like the one below, where each line contains the information of the name, email, telephone number, 
tax identification number, and the discount applied to it. The lines are separated with the line break character \n and the first line contains the names of the fields with 
the information contained in the directory.

"nif;name;email;telephone;discount\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail .com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"
Write a program that generates a dictionary with the directory information, where each element corresponds to a client and has its ID as key and another dictionary with the 
rest of the client's information as its value. The dictionaries with the information of each client will have the names of the fields as keys and the information of each 
client corresponding to the fields as values. That is, a dictionary like the following

{'01234567L': {'name': 'Luis González', 'email': 'luisgonzalez@mail.com', 'phone': '656343576', 'discount': 12.5}, '71476342J': {'name' : 'Macarena Ramírez', 'email': 'macarena@mail.com', 'phone': '692839321', 'discount': 8.0}, '63823376M': {'name': 'Juan José Martínez', 'email ': 'juanjo@mail.com', 'phone': '664888233', 'discount': 5.2}, '98376547F': {'name': 'Carmen Sánchez', 'email': 'carmen@mail.com' , 'phone': '667677855', 'discount': 15.7}}
'''

info = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"
info_list = info.split("\n")
dict_keys = info_list[0].split(";")
info_list.pop(0)
directory = {}


for customer in info_list:
    client = {}
    cust_info = customer.split(';') 
    for idx in range(1, len(dict_keys)):
        client[dict_keys[idx]] = cust_info[idx]
    
    directory[cust_info[0]] = client
print(directory)