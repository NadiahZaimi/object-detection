#out stock of product
def out_of_stock_product(detected_products):
    # List of products to check for out-of-stock
    maggi_kari_to_check = [
        "maggi kari unsorted", "maggi kari"
    ]
    maggi_tomyam_to_check = [
         "maggi tomyam", "maggi tomyamunsorted"
    ]
    nestle_koko_to_check = [
        "nestle koko unsorted", "nestle koko"
    ]
    
    nestle_milo_to_check = [
        "nestle milo unsorted", "nestle milo"
    ]
    nestle_star_to_check = [
        "nestle stars unsorted", "nestle stars"
    ]
    
    
    
    #SOV - Maggi Kari
    # Initialize the out_of_stock status as False
    out_of_stock_kari = True #Out of Stock

    # Check if any of the products are missing in the detected products
    for product in maggi_kari_to_check:
        if product in detected_products: #checkProduct ade dlm list
            # Set out_of_stock to False, bkn OOS
            out_of_stock_kari = False
            break  # Exit the loop when not found any la

    # Determine the status based on out_of_stock
    if out_of_stock_kari:
        oos_maggi_kari = "Yes" #Out of stock
    else:
        oos_maggi_kari = "No" # In stock
    
        
    #SOV - Maggi Tomyam
    # Initialize the out_of_stock status as False
    out_of_stock_tomyam = True #Out of Stock

    # Check if any of the products are missing in the detected products
    for product in maggi_tomyam_to_check:
        if product in detected_products: #checkProduct ade dlm list
            # Set out_of_stock to False, bkn OOS
            out_of_stock_tomyam = False
            break  # Exit the loop when not found any la

    # Determine the status based on out_of_stock
    if out_of_stock_tomyam:
        oos_maggi_tomyam = "Yes" #Out of stock
    else:
        oos_maggi_tomyam = "No" # In stock
        
        
        
        
    #SOV- Nestle Koko
    # Check 
    out_of_stock_koko = True #Out of Stock
    
    for product in nestle_koko_to_check:
        if product in detected_products: #checkProduct ade dlm list
            # Set out_of_stock to False, bkn OOS
            out_of_stock_koko = False
            break  # Exit the loop when not found any la

    if out_of_stock_koko:
        oos_nestle_koko = "Yes" #Out of stock
    else:
        oos_nestle_koko = "No" # In stock
        
    #SOV- Nestle Milo
    # Check 
    out_of_stock_milo = True #Out of Stock
    
    for product in nestle_milo_to_check:
        if product in detected_products: #checkProduct ade dlm list
            # Set out_of_stock to False, bkn OOS
            out_of_stock_milo = False
            break  # Exit the loop when not found any la

    if out_of_stock_milo:
        oos_nestle_milo = "Yes" #Out of stock
    else:
        oos_nestle_milo = "No" # In stock
    
    #SOV- Nestle Star
    # Check 
    out_of_stock_star = True #Out of Stock
    
    for product in nestle_star_to_check:
        if product in detected_products: #checkProduct ade dlm list
            # Set out_of_stock to False, bkn OOS
            out_of_stock_star = False
            break  # Exit the loop when not found any la

    if out_of_stock_star:
        oos_nestle_star = "Yes" #Out of stock
    else:
        oos_nestle_star = "No" # In stock
    
    return oos_maggi_kari, oos_maggi_tomyam, oos_nestle_koko, oos_nestle_milo, oos_nestle_star
    
    
    
def out_of_stock_maggi(detected_products):
    # List of products to check for out-of-stock
    maggi_to_check = [
        "maggi kari unsorted", "maggi kari", "maggi tomyam", "maggi tomyamunsorted"
    ]
    
    # Initialize the out_of_stock status as False
    out_of_stock = True #Out of Stock

    # Check if any of the products are missing in the detected products
    for product in maggi_to_check:
        if product in detected_products: #checkProduct ade dlm list
            # Set out_of_stock to False, bkn OOS
            out_of_stock = False
            break  # Exit the loop when not found any la

    # Determine the status based on out_of_stock
    if out_of_stock:
        oos_maggi = "Yes" #Out of stock
    else:
        oos_maggi = "No" # In stock

    return oos_maggi

def out_of_stock_nestle(detected_products):
   
    nestle_to_check = [
        "nestle koko unsorted", "nestle koko", "nestle milo unsorted", "nestle milo",
        "nestle stars unsorted", "nestle stars"
    ]

    out_of_stock = True #Out of Stock

    # Check 
    for product in nestle_to_check:
        if product in detected_products: #checkProduct ade dlm list
            # Set out_of_stock to False, bkn OOS
            out_of_stock = False
            break  # Exit the loop when not found any la

    if out_of_stock:
        oos_nestle = "Yes" #Out of stock
    else:
        oos_nestle = "No" # In stock

    return oos_nestle

def complience_maggi(detected_products):
   
    maggi_to_check = [
        "maggi kari unsorted", "maggi tomyamunsorted"
    ]

    complience = False #organized

    # Check 
    for product in maggi_to_check:
        if product in detected_products: #checkProduct ade dlm list
            # Set complience to False, tak organized
            complience = True
            break  # Exit the loop when not found any la

    if complience:
        complience_maggi = "No" #not organized
    else:
        complience_maggi = "Yes" # organized

    return complience_maggi

def complience_nestle(detected_products):
   
    nestle_to_check = [
        "nestle koko unsorted", "nestle milo unsorted", "nestle stars unsorted"
    ]

    complience = False #organized

    # Check 
    for product in nestle_to_check:
        if product in detected_products: #checkProduct ade dlm list
            # Set complience to False, tak organized
            complience = True
            break  # Exit the loop when not found any la

    if complience:
        complience_nestle = "No" #not organized
    else:
        complience_nestle = "Yes" #organized

    return complience_nestle


#Check eye level
#FIGHTING

# def compliance_eye_level(detected_boxes, max_height):
    
#     nestle_to_check = [
#         "nestle koko unsorted", "nestle koko", "nestle milo unsorted", "nestle milo",
#         "nestle stars unsorted", "nestle stars"
#         ]

#     found_products = set(nestle_to_check)
    
#     for found_products in detected_boxes:
#         x_min, y_min, x_max, y_max = found_products

#         # You can add logic here to check if the coordinates match the specified criteria.
#         # If any product doesn't meet the criteria, return "No".
#         if not (y_min <= max_height <= y_max):
#             return "No"

#     # If the loop completes without returning "No," it means all products are in compliance.
#     return "Yes"

#check product ade 
#dptkan coordinate product yg detect tu
#set coordinat
#all dekat set coordinate (Yes)
#some tak kene coordinate (No)
def nestle_eye_level_check(detected_products, detected_boxes):
    # List of products to check for out-of-stock
    nestle_to_check = [
        "nestle koko unsorted", "nestle koko", "nestle milo unsorted", "nestle milo",
        "nestle stars unsorted", "nestle stars"
    ]
    
    # Initialize eye level
    nestle_eye_level_status = "Yes"

    #nestle
    # Check if any of the products are missing in the detected products
    for product in nestle_to_check:
        if product in detected_products: #checkProduct ade dlm list
            print("Product Detected:", product)
             # Check the coordinates for this product
            product_index = detected_products.index(product)
            product_box = detected_boxes[product_index]
            # Assuming the boxes are in [x1, y1, x2, y2] format
            # Check if the product is NOT within the specified height range (2 meters)
            if not (1000 < product_box[3] <= 3000): #takde kat coordinat ni
                nestle_eye_level_status = "No"  # not eye level
                print("Coordinates for", product, ":", product_box)
                break    
            
    return nestle_eye_level_status

def maggi_eye_level_check(detected_products, detected_boxes):
    # List of products to check for out-of-stock
    
    
    maggi_to_check = [
        "maggi kari unsorted", "maggi kari", "maggi tomyam", "maggi tomyamunsorted"
    ]
    
    # Initialize eye level
    maggi_eye_level_status = "Yes"
      
    #Maggi
    # Check if any of the products are missing in the detected products
    for product in maggi_to_check:
        if product in detected_products: #checkProduct ade dlm list
            print("Product Detected:", product)
             # Check the coordinates for this product
            product_index = detected_products.index(product)
            product_box = detected_boxes[product_index]
            # Assuming the boxes are in [x1, y1, x2, y2] format
            # Check if the product is NOT within the specified height range (2 meters)
            if not (1000 < product_box[3] <= 3000): #takde kat coordinat ni
                maggi_eye_level_status = "No"  # not eye level
                print("Coordinates for", product, ":", product_box)
                break      
            
    return maggi_eye_level_status



