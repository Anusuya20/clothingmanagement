# ECOMMERCE
- Developer(https://github.com/Anusuya20)

---
## screenshots

### Admin Dashboard
![admin dashboard](https://user-images.githubusercontent.com/89215124/208358384-a30c0b99-8d4e-49ac-8b7d-b04543612b72.png)
### Admin View Clothes
![viewclothes](https://user-images.githubusercontent.com/89215124/208362828-5ab4d9db-ef2a-4c34-ab53-c8be2dd00074.png)
### Customer Home page
![customerhome](https://user-images.githubusercontent.com/89215124/208361613-4edbfed0-3357-425e-9073-33ae3a236c12.png)
### Cart 
![cartpage](https://user-images.githubusercontent.com/89215124/208362220-4c3488f6-176e-4b60-9de2-8a92bb275be8.png)
### Track Orders
![vieworders](https://user-images.githubusercontent.com/89215124/208362449-ba6a5cbe-7e16-4ff1-a1ad-59d85b064355.png)

---
## FUNCTIONS
## Customer
- Customer can view/search products without login.
- Customer can also add/remove product to cart without login (if customer try to add same product in cart. It will add only one)
- When customer try to purchase product, then he/she must login to system.
- After creating account and login to system, he/she can place order.
- There is a payment page also (just for demo, DONT FILL YOUR CARD DETAILS THERE ,By the way, website do not save that details)
- If customer click on pay button, then their payment will be successful and their order will be placed.
- Customer can check their ordered details by clicking on orders button.
- Customer can see the order status (Pending, Confirmed, Delivered) for each order  
- Customer can Download their order invoice for each order
- Customer can send feedback to admin (without login)
---
### Admin
- First admin will login ( for username/password run following command in cmd )
```
py manage.py createsuperuser
```
- Give username, email, password and your admin account will be created.
- After login, there is a dashboard (attached in screenshot) where admin can see how many customer is registered, how many products are there for sale, how many orders placed.
- Admin can add/delete/view/edit the products.
- Admin can view/edit/delete customer details.
- Admin can view/delete orders.
- Admin can change status of order (order is pending, confirmed, out for delivery, delivered)
- Admin can view the feedbacks sent by customers.
---
### Other Features
- customer places order and admin deleted that user(fraud detection), then their orders will automatically deleted

- suppose 1 customer places 4 products order and admin deleted 2 product from website, then that 2 product order will
    also be deleted and other 2 will be their
- If user click on purchase button without having products in their cart, then website will ask to add product in cart first.



## HOW TO RUN THIS PROJECT
- Install Python(3.7.6) (Dont Forget to Tick Add to Path while installing Python)
- Open Terminal and Execute Following Commands :
```
pip install django==3.0.5
pip install django-widget-tweaks
pip install xhtml2pdf

```
- Download This Project Zip Folder and Extract it
- Move to project folder in Terminal. Then run following Commands :
```
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```
- Now enter following URL in Your Browser Installed On Your Pc
```
http://127.0.0.1:8000/
```




