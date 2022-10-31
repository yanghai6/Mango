import os
from pathlib import Path

# App
RAW_PREFERENCE_DATA_CSV_HEADERS = [
    "age",
    "gender",
    "date",
    "amount",
    "category",
    "id",
    "marital",
    "education",
]

RAW_MIN_OFFER_DATA_CSV_HEADERS = [
    "id",
    "gender",
    "age",
    "income",
    "marital",
    "education",
    "min_offer",
]

CATEGORIES = [
    "Hospital or Clinic",
    "Electronics",
    "Convenience Store",
    "Jewelry",
    "Airlines",
    "Hotels",
    "Department Store",
    "Car Rent",
    "None",
    "Restaurant",
    "Gas Station",
    "Clothing",
    "Construction Material",
    "Financial Transfers",
    "Auto Parts",
    "Online Purchases",
    "Service",
    "Drugstores",
    "Furniture and Decoration",
    "Supermarket",
    "Other",
    "Tourism Agency",
]


AGE = [
    "<= 24",
    "25-29",
    "30-34",
    "35-39",
    "40-44",
    "45-49",
    "50-54",
]

GENDER = [
    "Female",
    "Male",
]

MARITAL = [
    "divorced",
    "married",
    "separated",
    "single",
    "widowed",
]

EDUCATION = [
    "below upper secondary",
    "tertiary education",
    "upper secondary and post-secondary non-tertiary",
]

PERSONA_MAPPING = {
    "age": {
        0: "<= 24",
        1: "25-29",
        2: "30-34",
        3: "35-39",
        4: "40-44",
        5: "45-49",
        6: "50-54",
    },
    "gender": {0: "female", 1: "male"},
    "marital_status": {
        0: "divorced",
        1: "married",
        2: "separated",
        3: "single",
        4: "widowed",
    },
    "education": {
        0: "below upper secondary",
        1: "tertiary education",
        2: "upper secondary and post-secondary non-tertiary",
    },
    "income": {
        0: "below $10,000",
        1: "between $10,000 and $19,999",
        2: "between $20,000 and $29,999",
        3: "between $30,000 and $39,999",
        4: "between $40,000 and $49,999",
        5: "between $50,000 and $59,999",
        6: "between $60,000 and $69,999",
        7: "between $70,000 and $79,999",
        8: "between $80,000 and $89,999",
        9: "between $90,000 and $99,999",
        10: "between $100,000 and $109,999",
        11: "between $110,000 and $119,999",
        12: "between $120,000 and $129,999",
    },
}

CATEGORY_PRODUCT_MAPPING = {
    "Hospital or Clinic": [
        {
            "value": 50,
            "description": "Dental Care",
            "image": "https://upload.wikimedia.org/wikipedia/en/thumb/0/0d/Mount_Sinai_Hospital_Logo.svg/640px-Mount_Sinai_Hospital_Logo.svg.png?1638323351931",
            "category": "Hospital or Clinic",
        }
    ],
    "Electronics": [
        {
            "value": 50,
            "description": "Gift Card",
            "image": "https://d2j6dbq0eux0bg.cloudfront.net/default-store/giftcards/gift_card_003_1500px.jpg",
            "category": "Electronics",
        }
    ],
    "Convenience Store": [
        {
            "value": 5,
            "description": "Snack",
            "image": "https://www.chatelaine.com/wp-content/uploads/2018/03/healthy-snacks-lays.png",
            "category": "Convenience Store",
        },
        {
            "value": 5,
            "description": "Coffee",
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhWy0t1QIG4XKvWyOSiIZo4h5QhEXzEWZfZA&usqp=CAU",
            "category": "Convenience Store",
        },
    ],
    "Jewelry": [
        {
            "value": 50,
            "description": "Ring",
            "image": "http://cdn.shopify.com/s/files/1/0364/7253/products/Mini_Stackable_Diamond_Ring_-_Rose_1024x1024.png?v=1542832599",
            "category": "Jewelry",
        },
        {
            "value": 75,
            "description": "Necklace",
            "image": "http://cdn.shopify.com/s/files/1/0364/7253/products/IMG_3176-EditR_1024x1024.png?v=1573040086",
            "category": "Jewelry",
        },
    ],
    "Airlines": [
        {
            "value": 150,
            "description": "Flight",
            "image": "https://logos-world.net/wp-content/uploads/2021/05/Air-Canada-Logo.png",
            "category": "Airlines",
        }
    ],
    "Hotels": [
        {
            "value": 450,
            "description": "All-inclusive",
            "image": "https://www.hospitalitynet.org/picture/xxl_153080168.jpg?t=20170718165429",
            "category": "Hotels",
        },
        {
            "value": 150,
            "description": "Hotel Room",
            "image": "https://images.trvl-media.com/hotels/1000000/30000/28000/27994/715b2ae3_y.jpg",
            "category": "Hotels",
        },
    ],
    "Department Store": [
        {
            "value": 40,
            "description": "Shoes",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Logo_NIKE.svg/1200px-Logo_NIKE.svg.png",
            "category": "Department Store",
        },
        {
            "value": 30,
            "description": "Clothes",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/UNIQLO_logo.svg/1200px-UNIQLO_logo.svg.png",
            "category": "Department Store",
        },
    ],
    "Car Rent": [
        {
            "value": 30,
            "description": "Sedan",
            "image": "https://download.logo.wine/logo/Budget_Rent_a_Car/Budget_Rent_a_Car-Logo.wine.png",
            "category": "Car Rent",
        },
        {
            "value": 35,
            "description": "SUV",
            "image": "https://download.logo.wine/logo/Budget_Rent_a_Car/Budget_Rent_a_Car-Logo.wine.png",
            "category": "Car Rent",
        },
    ],
    "None": [
        {"value": 99999999, "description": "None", "image": "#", "category": "None"}
    ],
    "Restaurant": [
        {
            "value": 10,
            "description": "Fast Food",
            "image": "https://static.wikia.nocookie.net/logopedia/images/7/70/Five_guys%2C_stacked.jpg/revision/latest?cb=20181008151801",
            "category": "Restaurant",
        },
        {
            "value": 10,
            "description": "Cafe",
            "image": "https://upload.wikimedia.org/wikipedia/en/thumb/d/d3/Starbucks_Corporation_Logo_2011.svg/1200px-Starbucks_Corporation_Logo_2011.svg.png",
            "category": "Restaurant",
        },
        {
            "value": 20,
            "description": "Restaurant",
            "image": "https://upload.wikimedia.org/wikipedia/en/thumb/d/d4/The_Cheesecake_Factory_%28logo%2C_stacked%29.svg/1024px-The_Cheesecake_Factory_%28logo%2C_stacked%29.svg.png",
            "category": "Restaurant",
        },
    ],
    "Gas Station": [
        {
            "value": 50,
            "description": "Gas",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Chevron_Logo.svg/1836px-Chevron_Logo.svg.png",
            "category": "Gas Station",
        }
    ],
    "Clothing": [
        {
            "value": 20,
            "description": "New Clothes",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/UNIQLO_logo.svg/1200px-UNIQLO_logo.svg.png",
            "category": "Clothing",
        }
    ],
    "Construction Material": [
        {
            "value": 50,
            "description": "Wood",
            "image": "http://cdn.shopify.com/s/files/1/1472/3568/products/OffCutsCityFirewood_grande.png?v=1606186993",
            "category": "Construction Material",
        },
        {
            "value": 40,
            "description": "Steel",
            "image": "https://www.metalsupermarkets.com/wp-content/uploads/2021/03/Metal-Supermarkets-Steel-Supplier-300x262.png",
            "category": "Construction Material",
        },
    ],
    "Financial Transfers": [
        {
            "value": 100,
            "description": "e-Transfer",
            "image": "https://images.squarespace-cdn.com/content/v1/56aaa935a128e6257bda9609/1585353927832-ELGXH4YYD5UG8Z6R36J4/interac-email-transfer-logo.png",
            "category": "Financial Transfers",
        }
    ],
    "Auto Parts": [
        {
            "value": 200,
            "description": "Winter Tire",
            "image": "https://1000logos.net/wp-content/uploads/2017/08/Michelin-logo.png",
            "category": "Auto Parts",
        }
    ],
    "Online Purchases": [
        {
            "value": 100,
            "description": "Amazon Gift Card",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Amazon_logo.svg/800px-Amazon_logo.svg.png",
            "category": "Online Purchases",
        },
        {
            "value": 100,
            "description": "Bestbuy Gift Card",
            "image": "https://cdn.vox-cdn.com/thumbor/C5Une1ds5CQ9gO3TL_OoW-9ovb0=/0x0:882x498/920x613/filters:focal(371x179:511x319):format(webp)/cdn.vox-cdn.com/uploads/chorus_image/image/59677317/2018_rebrand_blog_logo_LEAD_ART.0.jpg",
            "category": "Online Purchases",
        },
    ],
    "Service": [
        {
            "value": 20,
            "description": "Netflix",
            "image": "https://assets.brand.microsites.netflix.io/assets/493f5bba-81a4-11e9-bf79-066b49664af6_cm_1440w.png?v=61",
            "category": "Service",
        },
        {
            "value": 10,
            "description": "Spotify",
            "image": "https://storage.googleapis.com/pr-newsroom-wp/1/2018/11/Spotify_Logo_RGB_Green.png",
            "category": "Service",
        },
    ],
    "Drugstores": [
        {
            "value": 50,
            "description": "Prescription",
            "image": "https://files.ontario.ca/thumb-health-prescription-transparent.png",
            "category": "Drugstores",
        }
    ],
    "Furniture and Decoration": [
        {
            "value": 50,
            "description": "Lights",
            "image": "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/currey-08191961701.jpg?crop=0.849xw:0.995xh;0.0646xw,0.00517xh&resize=480:*",
            "category": "Furniture and Decoration",
        }
    ],
    "Supermarket": [
        {
            "value": 80,
            "description": "Groceries",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Costco_Wholesale_logo_2010-10-26.svg/512px-Costco_Wholesale_logo_2010-10-26.svg.png",
            "category": "Supermarket",
        }
    ],
    "Other": [
        {
            "value": 80,
            "description": "Video Games",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Steam_icon_logo.svg/512px-Steam_icon_logo.svg.png",
            "category": "Other",
        }
    ],
    "Tourism Agency": [
        {
            "value": 200,
            "description": "Canadian Tour",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Flag_of_Canada_%28Pantone%29.svg/1024px-Flag_of_Canada_%28Pantone%29.svg.png",
            "category": "Tourism Agency",
        },
        {
            "value": 500,
            "description": "Mexico Tour",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Flag_of_Mexico.svg/1024px-Flag_of_Mexico.svg.png",
            "category": "Tourism Agency",
        },
    ],
}


# Directory paths
ROOT_DIR = Path(__file__).parent.parent

APP_DIR = os.path.join(ROOT_DIR, "app")

STATIC_DIR = os.path.join(APP_DIR, "static")
BACKEND_DIR = os.path.join(APP_DIR, "backend")

CONTROLLERS_DIR = os.path.join(BACKEND_DIR, "controllers")
EXCEPTIONS_DIR = os.path.join(BACKEND_DIR, "exceptions")
MODELS_DIR = os.path.join(BACKEND_DIR, "models")
SERVICES_DIR = os.path.join(BACKEND_DIR, "services")

DATA_PREPROCESSING_DIR = os.path.join(MODELS_DIR, "data_preprocessing")
ML_DIR = os.path.join(MODELS_DIR, "ml")
TB_LOGS_DIR = os.path.join(ML_DIR, "tb_logs")

PREFERENCES_MODEL_FILE = os.path.join(ML_DIR, "preferences_model.ckpt")
MIN_OFFER_MODEL_FILE = os.path.join(ML_DIR, "min_offer_model.ckpt")
