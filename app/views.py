from app import app
from flask import render_template, request, redirect, url_for
from flask import jsonify, flash

#Mock Array of products
products1 = [
        {
            "id": 1,
            "name": "Omega Speedmaster - Apollo Edition",
            "price": 16960,
            "image": "images/Omega Speedmaster - Apollo Edition.webp",
            "description": "This 42-mm Speedmaster features a couple of unique elements from the steel version. One such element is the Apollo XVII mission patch in gold that is located on the subdial at nine o'clock. The same gold mission patch can be found on the case back. The blue dial corresponds with the blue ceramic bezel."
        },
        {
            "id": 2,
            "name": "Rolex Milgauss",
            "price": 11549,
            "image": "images/Rolex Milgauss.jpg",
            "description": "A must-have watch Swiss-made Rolex Milgauss Oystersteel Men's watch model 116400GV-0001. Features a polished 904L stainless steel case with a screw-down crown & case back and a brushed with polished 904L stainless steel oyster bracelet. A deep black dial is accentuated by Chromalight luminescent hands."
        },
        {
            "id": 3,
            "name": "Rolex Submariner - Hulk",
            "price": 21990,
            "image": "images/Rolex Submariner - Hulk.webp",
            "description": "Stainless steel case with a stainless steel oyster bracelet. Uni-directional rotating stainless steel bezel with a green cerachrom top ring. Green dial with silver-tone Mercedes-logo, sword, and Breguet-style shape hands and luminous dot hour markers. Minute markers around the outer rim. "
        },
        {
            "id": 4,
            "name": "Audemars Piguet Royal Oak",
            "price": 400,
            "image": "images/AudemarsPiguetRoyalOak.jpg",
            "description": "A must have example of simple and clean, the Royal Oak Extra Thin Tourbillon is a welcome take on the impressive offerings from Audemars Piguet. The 18k rose gold 41 mm case is assembled with a matching, fixed bezel, blue petite tapisserie dial, and a screw-down crown. This timepiece is powered by a 2924 calibre with a 70-hour power reserve and power reserve indicator."
        },
        {
            "id": 5,
            "name": "Omega Seamaster 300M",
            "price": 6000,
            "image": "images/Omega Seamaster.webp",
            "description": "The watch is in New/Unworn condition, with no signs of wear. The pictures are very representative of the condition. Omega Seamaster Diver 300M Blue Dial, reference 210.22.42.20.03.002"
        },
        {
            "id": 6,
            "name": "Vacheron Constantin Overseas",
            "price": 121000,
            "image": "images/Vacheron Constantin Overseas.jpg",
            "description": "Vacheron Constantin 4300V Overseas Perpetual Calendar Ultra-Thin Skeleton 4300V/120R-B547, 4300V120RB547, 4300V 120R B547, 18k rose gold on an integral 18k rose gold bracelet with a double folding deployant clasp, automatic Vacheron caliber 1120 QP/1, 40-hour power reserve, skeletonized dial with applied luminous rose gold hour markers and luminous hands, perpetual calendar with indications for the month (with leap year), day, date, and moonphase, sapphire crystal, water resistant to 50 meters, diameter: 41.5mm, thickness: 8.1mm. Like new with box and undated papers. The watch was worn only a couple of times."
        }
    ]

## ROUTES ##
@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')
 

@app.route('/products')
def products():
    """Render the website's products page."""

    return render_template('products.html', products=products1)

@app.route('/product/<int:id>', methods=['GET'])
def product(id):
    """Render the website's product page."""

    selected_Product = next((item for item in products1 if item["id"] == id), None)
    if selected_Product is not None:
        return render_template('selected_product.html', product=selected_Product)
    else:
        return render_template('404.html'), 404


## API ROUTES FOR POST MAN TESTING ## 
@app.route('/GetProducts', methods=['GET'])
def GetProducts():

    return jsonify(products1)

@app.route('/GetProduct/<int:id>', methods=['GET'])
def get_product(id):
    
     selected_Product = next((item for item in products1 if item["id"] == id), None)
     if selected_Product is not None:
         return jsonify(selected_Product)
     else:
         return jsonify({"message": "Product not found"}), 404

## General functions ##
@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
