# shop (Flask & MongoDb & Bootstrap)
![shop](https://user-images.githubusercontent.com/71823327/109374387-41f16c80-78ca-11eb-936a-4c0c3977271f.PNG)
![shop2](https://user-images.githubusercontent.com/71823327/109374396-4c136b00-78ca-11eb-97f6-0d2e5daf775a.PNG)
![shop3](https://user-images.githubusercontent.com/71823327/109374404-52094c00-78ca-11eb-8006-c61a6141818e.PNG)
* This project is simple online shoping website that you can have your own storages with lots of products with your favorite category in manager position and buy products
* as customer position.
* You have powerfull admin panel that can help you t manage your store better.
* The main category of website is in `category.json` with special format and if you want to change that remember to keep the structure of that file.
* You have to set your database configuration in file `instance/confige.py`(get help from config_sample.py).
* Also you can use my prepared database in directory `onlineshop_db`.
## How to run
1. set your flask app variable.(based on which os you are working with (Linux or windows))
* For instance for windows `set FLASK_APP=onlineshop`
2. run your server.
* `flask run`
## Features
* All the managing ability such as add product , add product to storage , edit the product (price , name) , managing the customer and ...
* Using Ajax for better performance for the clinet who work with the site.
