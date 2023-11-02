import io
from PIL import Image, ImageDraw, ImageFont
import os
from flask import Flask, request, send_file, jsonify
import nest_asyncio
from pyngrok import ngrok
from ultralytics import YOLO
from oos_detection import out_of_stock_product, complience_maggi, complience_nestle, nestle_eye_level_check, maggi_eye_level_check


app = Flask(__name__)
model = YOLO('best_246.pt')

# Specify the folder where you want to save annotated images
output_folder = "annotated_images"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#Put outsite so all can access    
item_list = [
    "fn kundur",
    "fn lemontea",
    "jnj twin",
    "maggi kari unsorted",
    "maggi kari",
    "maggi tomyam",
    "maggi tomyamunsorted",
    "marigold",
    "mr potato",
    "nestle koko unsorted",
    "nestle koko",
    "nestle milo unsorted",
    "nestle milo",
    "nestle stars unsorted",
    "nestle stars",
    "ping pong",
    "roma malkist",
    "twisties ori",
    "twisties sco",
    "yeos greentea",
    "yeos tebu"
]

@app.route("/objectdetection/", methods=["POST"])
def predict():
    if not request.method == "POST":
        return

    if request.files.get("image"):
        image_file = request.files["image"]
        image_bytes = image_file.read()
        img = Image.open(io.BytesIO(image_bytes))
        
        # rotate image
        # Check and rotate based on EXIF data
        exif = img._getexif()
        if exif:
            orientation = exif.get(0x0112)  # EXIF code for orientation
            if orientation is not None:
                if orientation == 1:
                    # Normal orientation, no rotation needed
                    pass
                elif orientation == 3:
                    img = img.rotate(180, expand=True)
                elif orientation == 6:
                    img = img.rotate(270, expand=True)
                elif orientation == 8:
                    img = img.rotate(90, expand=True)

        results = model(img)
        
        # Annotate the image with bounding boxes and class labels
        annotated_img = annotate_image(img, results[0].boxes.xyxy.tolist(), results[0].boxes.cls.tolist())

        # Generate a unique filename for the annotated image
        output_filename = os.path.join(output_folder, "annotated_image.jpg")

        # Save the annotated image as a JPG file
        annotated_img.save(output_filename, format="JPEG")
        
        # Out_of_stock
        # Perform out of stock detection
        product_names = [item_list[int(class_label)] for class_label in results[0].boxes.cls.tolist()]
        print(product_names)
        oos_maggi_kari,oos_maggi_tomyam, oos_nestle_koko, oos_nestle_milo, oos_nestle_star= out_of_stock_product(product_names)
        
        comp_maggi = "N/A"
        eye_level_status_maggi = "N/A"
        comp_nestle = "N/A"
        eye_level_status_nestle = "N/A"
        
        if oos_maggi_kari == "No" or oos_maggi_tomyam == "No" :
            if oos_nestle_koko == "No" or oos_nestle_milo == "No" or oos_nestle_star == "No":
                # Process only complience_nestle and nestle_eye_level_check
                comp_maggi = complience_maggi(product_names)
                eye_level_status_maggi = maggi_eye_level_check(product_names, results[0].boxes.xyxy.tolist())
                comp_nestle = complience_nestle(product_names)
                eye_level_status_nestle = nestle_eye_level_check(product_names, results[0].boxes.xyxy.tolist())
            else:
                comp_maggi = complience_maggi(product_names)
                eye_level_status_maggi = maggi_eye_level_check(product_names, results[0].boxes.xyxy.tolist())
                comp_nestle = "-"
                eye_level_status_nestle = "-"
        else:
            
            if oos_nestle_koko == "No" or oos_nestle_milo == "No" or oos_nestle_star == "No":  
                # Process only complience_nestle and nestle_eye_level_check
                comp_maggi = "-"
                eye_level_status_maggi = "-"
                comp_nestle = complience_nestle(product_names)
                eye_level_status_nestle = nestle_eye_level_check(product_names, results[0].boxes.xyxy.tolist())
            else:
                comp_maggi = "-"
                eye_level_status_maggi = "-"
                comp_nestle = "-"
                eye_level_status_nestle = "-"

        # Return the path to the saved annotated image and the out of stock result in JSON format
        response = {
            "Result": f"Annotated image saved at: {output_filename}",
            "Out of Stock Maggi Kari": oos_maggi_kari,
            "Out of Stock Maggi Tomyam": oos_maggi_tomyam,
            "Out of Stock Nestle Koko": oos_nestle_koko,
            "Out of Stock Nestle Milo": oos_nestle_milo,
            "Out of Stock Nestle Star": oos_nestle_star,
            "Compliance Maggi": comp_maggi,
            "Compliance Nestle": comp_nestle,
            "Eye Level nestle": eye_level_status_nestle,
            "Eye Level Maggi": eye_level_status_maggi,
        }
        return jsonify(response)
    
    
def annotate_image(image, boxes, classes):
    img_draw = image.copy()
    draw = ImageDraw.Draw(img_draw)
    font = ImageFont.truetype("arial.ttf", 20)

    for box, class_label in zip(boxes, classes):
        x_min, y_min, x_max, y_max = box
        class_label = int(class_label)

        item_list = [
            "fn kundur",
            "fn lemontea",
            "jnj twin",
            "maggi kari unsorted",
            "maggi kari",
            "maggi tomyam",
            "maggi tomyamunsorted",
            "marigold",
            "mr potato",
            "nestle koko unsorted",
            "nestle koko",
            "nestle milo unsorted",
            "nestle milo",
            "nestle stars unsorted",
            "nestle stars",
            "ping pong",
            "roma malkist",
            "twisties ori",
            "twisties sco",
            "yeos greentea",
            "yeos tebu"
        ]
        
        label_name = item_list[class_label]
        class_label_text = f"Class: {label_name}"

        random_colors = [
            (152, 245, 255),
            (253, 40, 143),
            (19, 119, 14),
            (238, 197, 152),
            (58, 172, 216),
            (110, 128, 180),
            (84, 37, 209),
            (159, 223, 131),
            (119, 61, 207),
            (195, 123, 132),
            (20, 196, 56),
            (195, 29, 59),
            (42, 112, 127),
            (225, 90, 9),
            (155, 76, 68),
            (55, 144, 139),
            (207, 95, 5),
            (189, 11, 91),
            (101, 66, 242),
            (171, 232, 84),
            (119, 217, 59)
        ]


        draw.rectangle([x_min, y_min, x_max, y_max], outline=random_colors[class_label], width=2)

        
        draw.text((x_min, y_min), class_label_text, fill=random_colors[class_label], font=font)

    return img_draw

ngrok_tunnel = ngrok.connect(8000)
print('Public URL:', ngrok_tunnel.public_url)
nest_asyncio.apply()
app.run(host="0.0.0.0", port=8000)
