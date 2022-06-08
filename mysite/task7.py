from home.models import product

#inserting a new record into the product model:
   #1. python manage.py shell
   #2. from home.models import product
   #3. new_product = product(p_name ="hilux", p_price="$500000", p_color="navy-blue", p_brand="ford")
   #4. new_product.save()
   #5. product.object.all()

#get all records in the product table:
   #1. all_products = product.objects.all() 
   #2. print(all_products)

#filter products by name:
   #1. post.objects.filter(p_name = "hilux")

#get single record from product:
   #1. one_product = product.objects.get(pk = 1)   

#to change a product price
   # x = product.objects.get(p_price = "$500000")
   # print(x)
   # x.p_price = "$600000"
   # x.save()
       