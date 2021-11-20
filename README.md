# microservicio1 UserLogin

Microservicio 

End Points


•	login/   => function de login
•	refresh/ => se refresca el token
•	createuser/ => se crea un nuevo usuario
•	user/<int:pk> => retorna el usuario de la cuenta la llave primaria
•	updateuser/<int:pk> =>  actualiza los datos teniendo en cuenta la llave primaria
•	createauction/ => Se crea una subasta
•	auctiondetailView/<int:pk> => se indica la subasta teniendo en cuenta la llave primaria 
•	auctionupdateView/<int:pk>=> Se actualiza los campos de la subasta de acuerdo al pk
•	auctiondeleteView/<int:pk> => Se elimina la subasta de acuerdo a la llave primaria 
•	auctionlistview/ => Se muestran todas las subastas en la base de datos
•	createbid/ => se crea una puja requiere el token del usuario
•	detailbid/<int:user> => se generan todas las pujas de un usuario requiere token 
•	topbid/<int:user>/<int:auction>  se muestran la máxima puja que el usuario ha ofrecido en una determinada subasta    
•	deletebid/<int:auction> =>  se elimina todas las pujas que un usuario ha realizado en una determinada subasta

