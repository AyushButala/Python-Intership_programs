categoryName = input("Enter Category Name : ")

if categoryName == "Cloth":
    productName = input("Enter Product Name : ")
    productPrice = int(input("Enter Product Price : "))
    qty = int(input("Enter Product Quantity : "))
    gstPercentage = int(input("Enter GST Percentage : "))
    gstAmount = qty*((productPrice*gstPercentage)/100)
    total = (qty*productPrice)+gstAmount
    print("Category Name : {6} ,Product Name : {0} , Price : {1} , Quantity : {2} , Gst : {3} , GST Amount : {4} , Total Amount : {5}".format(
        productName, productPrice, qty, gstPercentage, gstAmount, total, categoryName))
elif categoryName == "Furniture":
    productName = input("Enter Product Name : ")
    productPrice = int(input("Enter Product Price : "))
    qty = int(input("Enter Product Quantity : "))
    gstPercentage = int(input("Enter GST Percentage : "))
    gstAmount = qty*((productPrice*gstPercentage)/100)
    total = (qty*productPrice)+gstAmount
    print("Category Name : {6} ,Product Name : {0} , Price : {1} , Quantity : {2} , Gst : {3} , GST Amount : {4} , Total Amount : {5}".format(
        productName, productPrice, qty, gstPercentage, gstAmount, total, categoryName))
elif categoryName == "Hotel":
    productName = input("Enter Product Name : ")
    productPrice = int(input("Enter Product Price : "))
    qty = int(input("Enter Product Quantity : "))
    gstPercentage = int(input("Enter GST Percentage : "))
    gstAmount = qty*((productPrice*gstPercentage)/100)
    total = (qty*productPrice)+gstAmount
    print("Category Name : {6} ,Product Name : {0} , Price : {1} , Quantity : {2} , Gst : {3} , GST Amount : {4} , Total Amount : {5}".format(
        productName, productPrice, qty, gstPercentage, gstAmount, total, categoryName))
else:
    print("Invalid Category")
