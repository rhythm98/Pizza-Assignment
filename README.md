# PizzaAssignment


## setting up the project 

1. firstly create virtual environment and install all the dependencies mentioned in [reuirement.txt](https://github.com/ajitsinghrathore/PizzaAssignment/blob/master/requirements.txt) file
2. Then , for connecting to database you need to provide the connection url username and password of your mongodb database in [settings.py](https://github.com/ajitsinghrathore/PizzaAssignment/blob/master/pizza_project/pizza_project/settings.py) file as shown below

   * ```
        DATABASES = {
            'default': {
                'ENGINE': 'djongo',
                'CLIENT': {
                    'host': "your host url",
                    'username': 'your username',
                    'password': 'your password',
                    'authMechanism': 'SCRAM-SHA-1'
                }

            }
        }

     ```

3. make migrations and  execute all migrations with these commands
    1. ``` python manage.py makemigrations```
    2. ``` python manage.py migrate```
4.  after all these  start your server with the  command given below
    1. ``` python manage.py runserver```


Server is runnning now  , For testing purpose i have created python scripts which  contains functions of  api calls for creating , fetching , updating and deleting pizza's , in order to use it comment all the function calls except the  function call to desired api call and execute it  


## Api endpoints 

* ### For fetching ("http://127.0.0.1:8000/PizzaApi/getPizza/") 

Users can fetch filtered list of pizza  based on size or type of pizza from this endpoint
input format for sending request to backend is given below
```
 data = {              
   "size":size,         
   "type":type,
   "page":pageno
 }  
```
 add data as query params in get request  , here **size** and **type** are optional fields for filtering  but **page** is mandatory and it  represents the page number for paginating large amount of pizza's

 response from server is as follows 
 ```
 response = {              
   'count': 1, 
   'next': 'http://127.0.0.1:8000/PizzaApi/getPizza/?page=2&size=small&type=square',
   'previous': None,
   'results': [    { 'id':1,
                     'Type': 'square',
                     'size': 'small',
                     'Toppings': [{'name': 'cheese'}, {'name': 'tomato'}]}
                 , { 'id':2,
                     'Type': 'square',
                     'size': 'small',
                     'Toppings': [{'name': 'onion'}, {'name': 'corn'}]}
              ]
 }  
```
here 
* id represents the id of the pizza which can be used to uniquely identify this pizza and update or delete it later 
* count represents the total number of pizza's present in database according to the  size and type which user has requested 
* next represnts  the url for fetching next set of results 
* previous represents  the url for fetching  previous page 
* results  is having the real data which  contain list of pizza 
* inside each pizza its type ,size and list of toppings are given

**Note** size of pagination is  set to 2 for testinf purpose you can chanhge its value in  [settings.py](https://github.com/ajitsinghrathore/PizzaAssignment/blob/master/pizza_project/pizza_project/settings.py) file as shown below

  * ```
      REST_FRAMEWORK = {
          'DEFAULT_PAGINATION_CLASS' :'rest_framework.pagination.PageNumberPagination',
          'PAGE_SIZE': enter your custom size of each page,
      }
    ```


* ### for creating ("http://127.0.0.1:8000/PizzaApi/")

Users can create pizza's from this endpoint , the input data format is given below
```
 data = {              
  "Type": "Regular",
  "size": "small",
  "Toppings": ["onion","cheese"]
 }  
```
add this as data in the **post request** for creating pizza's   and if  entries are valid  then piza will be created and **201 created status** message will be sent back from server , if size is not present in database then first we need to add that size then create pizza of that size , also  pizza type regular and square are only permitted if any of these  conditions are not satisfied then server will send **400 bad request** to the client along with the details of  the condition which is violated



* ### for deleting ("http://127.0.0.1:8000/PizzaApi/") 

User's can delete  any pizza from database by just sending the id of pizza in **http delete method** to this end point  
```
 data = {              
   "id": id,
 }  
```
if pizza with this id exists then it will be deleted and **200 ok** status messaage will be sent back by server but if there is no pizza with this id then server will send **404 not found** status message back to client


* ### for  updating ("http://127.0.0.1:8000/PizzaApi/")

User's can update any pizza entry by sending a **http put request** along with  data in the sample format given below to this end point
```
 data = {              
   'id':5,
   'Type':'square',
   'Toppings':{
         'add_Topping':True,
         'data':['fuck',"cheese"]
   }
 }  
```
here 

* id represent the id of the pizz to be updated , if there is no pizza of this id then server will send **404 not fouund** status message back to  user and nothing will be updated
* type  represent the new type user is willing to assign  it can be regular or square only otherwise request will fail
* toppings is JSON which has two parts 
  1. add_Topping  indicates whether user was want to append the list of toppings with the already present toppings or he wants to replace the old set of toppings with this latest list
  2.  data is list of toppings which user is willing to add or replace with
* size represents the new size which user is willing to give  this size shuld be present in database else request will not be fulfiled

**NOTE** type , size and toppings are not manadtory they are optioinal according to the need  of user but id is mandatory 


if update is succesfull then server will send **200 ok** status message else it will send **400 bad request** if data is not proper formatted or any conditions are violated along with the details of conditions which are violated




      
      
 





 
 
       
       
