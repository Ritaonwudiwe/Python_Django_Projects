from home.models import product

# navigate to python shell on the cmd: python manage.py shell
# write: from home.models import product 
# and run the following commands:

#inserting a new record into the product model:
   #1. new_product = product(p_name ="hilux", p_price="$500000", p_color="navy-blue", p_brand="ford")
   #2. new_product.save()
   #3. product.object.all()

#get all records in the product table:
   #1. all_products = product.objects.all() 
   #2. print(all_products)

#filter products by name:
   #1. post.objects.filter(p_name = "hilux")

#get single record from product:
#2 methods:
   #by using a key or id: one_product = product.objects.get(pk = 1)
   #by using field name: one_product = product.objects.get(p_name = "hilux")  

#to change a product price
   # x = product.objects.get(p_price = "$500000")
   # print(x)
   # x.p_price = "$600000"
   # x.save()
       