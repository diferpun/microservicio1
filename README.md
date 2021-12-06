# microservicio1 UserLogin/Auction

Esta aplicación plantea el desarrollo de una plataforma web para realizar subastas 

<h2>URL microservicio</h2>

https://auction-desp-be.herokuapp.com/


<h2>End Points</h2>

•	login/   => function de login
 <br/>
•	refresh/ => se refresca el token
 <br/>
•	createuser/ => se crea un nuevo usuario
 <br/>
•	user/<int:pk> => retorna los datos del usuario teniendo en cuenta la llave primaria
 <br/>
•	updateuser/<int:pk> =>  actualiza los datos teniendo en cuenta la llave primaria
 <br/>
•	createauction/ => Se crea una subasta
 <br/>
•	auctiondetailView/<int:pk> => se indica la subasta teniendo en cuenta la llave primaria 
 <br/>
•	auctionupdateView/<int:pk>=> Se actualiza los campos de la subasta de acuerdo al pk
 <br/>
•	auctiondeleteView/<int:pk> => Se elimina la subasta de acuerdo a la llave primaria
 <br/> 
•	auctionlistview/ => Se muestran todas las subastas en la base de datos
 <br/>
•	createbid/ => se crea una puja requiere el token del usuario que se ingresa en el postman ademas la oferta debe ser mayor al valor base de la subasta. Este valor base se actualiza cada vez que se hace una oferta mayor
 <br/>
•	detailbid/<int:user> => se generan todas las pujas de un usuario requiere token
 <br/> 
•	topbid/<int:user>/<int:auction> => se muestran la máxima puja que el usuario ha ofrecido en una determinada subasta    
 <br/>
•	deletebid/<int:auction> =>  se elimina todas las pujas que un usuario ha realizado en una determinada subasta
 <br/>

