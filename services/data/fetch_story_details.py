from typing import List, Dict

class Product:
    def __init__(self, id: str, name: str, description: str, productFrontImage: str,images: List[str], offer: Dict[str, float]):
        self.id = id
        self.name = name
        self.description = description
        self.productFrontImage = productFrontImage
        self.images = images
        self.offer = offer

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "product_description": self.description,
            "productFrontImage": self.productFrontImage,
            "product_images": self.images,
            "offer": self.offer
        }
    
    def for_gpt(self):
        return {
            "id": self.id,
            "name": self.name,
            "product_description": self.description,
            "mrp": self.offer["mrp"],
            "discountedPrice": self.offer["discountedPrice"],
            "percentageOff": self.offer["percentageOff"]
        }


class StoryData:
    def __init__(self, story_title: str, summary: str, products: List[Product]):
        self.story_title = story_title
        self.summary = summary
        self.products = products
        self.lead_ai_image = None
        self.lead_ai_image_duration = 3

    def to_dict(self):
        return {
            "story_title": self.story_title,
            "summary": self.summary,
            "products": [product.to_dict() for product in self.products]
        }
    
    def for_gpt(self):
        return {
            "story_title": self.story_title,
            "summary": self.summary,
            "products": [product.for_gpt() for product in self.products]
        }

class DataProvider:
    def __init__(self, url: str):
        self.url = url  # Placeholder for future use

    def get_data(self) -> StoryData:
        story_title = "Exclusive offers on best water purifiers from top brands like Aquaguard, Kent, Pureit, Livpure, up to 75 percent off"
        summary = "Now is the perfect time to buy water purifiers on Amazon, with special offers and exclusive deals currently available. Check out our list for best bargains."

        products = [
            Product(
                id="B09YLWT89W",
                name="Aquaguard Sure Delight NXT 6-Stage Water Purifier | RO+UV+UF Tech | Free Service Plan worth ₹2000 | India's #1 Water Purifier | Suitable for Borewell, Tanker Municipal Water",
                description="[Free Service Plan worth ₹2000 - Comes with Aquaguard genuine service plan offering free installation, 1 free maintenance visit and unlimited repair visits within 1 year of purchase, all backed by India's widest service network, accessible with one click across 17,000+ pin-codes, Warranty and Installation- Includes a 1-year free warranty and complimentary installation, Superior 6-Stage Purification- Offers 99.9999 percent bacteria reduction, 99.99% virus reduction, 30x better dust and dirt removal than local purifiers, and 10x more chemical protection through Sedi Shield, Particulate Filter and RO Maxx purification stages, Superior RO Maxx Technology- Removes contaminants like lead, mercury, microplastics, and pesticides, eliminating disease-causing viruses and bacteria, UV E-Boiling Technnology- Ensures that each drop of water is as pure and healthy as water boiled for over 20 minutes, Ultra Filtration- Makes your water crystal clear by removing ultra-fine suspended particles, Works With All Water Sources- Purifies water from any source, including municipal, borewell, or tanker water, ensuring safe and clean drinking water every time, Long Cartridge Life- A cartridge that lasts up to 1 year or 6000 litres, delivering consistent performance based on standard test conditions, Smart LED Indication- Keeps you informed with intuitive alerts for service reminders, tank-full indicators, filter life warnings, and electronic errors, ensuring optimal performance at all times, Certifications- Certified by the National Accreditation Board for Testing and Calibration Laboratories (NABL) and Water Quality Impact Assessment (WQIA), ensuring product reliability and performance]",
                productFrontImage="https://m.media-amazon.com/images/I/41NuMHQLaKL._SL500_.jpg",
                images= [
                "https://m.media-amazon.com/images/I/41NuMHQLaKL._SL500_.jpg",
                "https://m.media-amazon.com/images/I/41Z97xlgBpL._SL500_.jpg",
                "https://m.media-amazon.com/images/I/41rxg7wdp3L._SL500_.jpg",
                "https://m.media-amazon.com/images/I/41V8jjbPqpL._SL500_.jpg",
                "https://m.media-amazon.com/images/I/41OFc-LPjEL._SL500_.jpg",
                "https://m.media-amazon.com/images/I/41Bvx1bk-VL._SL500_.jpg"
            ],
                offer={
                    "mrp": 18000,
                    "discountedPrice": 9499,
                    "percentageOff": 47
                }
            ),
            Product(
                id="B09FK9R6Z7",
                name="KENT Supreme Copper RO Water Purifier | INR 1000 Off on Exchange | 4 Years Free Service | ISI Marked | Multiple Purification Process | RO + UV + UF + Copper + TDS Control + UV LED Tank | 8L Tank",
                description="[Multiple purification by RO+UV+UF+Copper+ TDS Control which removes even dissolved impurities such as arsenic, rust, pesticides fluorides, and kills bacteria and viruses to make water 100% pure and suitable for drinking with goodness of Copper;TDS control system allows adjustment of tds level of purified water which retains essential natural minerals in drinking water, UV LED Light in the storage tank keeps purified water bacteria free and pure Country of Origin-India;Zero Water Wastage Technology which recirculates the rejected water to the overhead tank using its own pump and ensures that no drop of water is wasted during the purification process, Wall mountable design to be suited for domestic purpose;8 litres storage capacity and 20 litres per hour purification capacity, Pre Filter not included;Suitable for purification of brackish, tap water municipal water supply; Warranty: 1 year warranty + 3 years extended service free. Terms and Conditions apply, Purification Method: Ultravioletreverse Osmosis]",
                productFrontImage="https://m.media-amazon.com/images/I/41Kuy2QXyfL._SL500_.jpg",
                images= [
                "https://m.media-amazon.com/images/I/41Kuy2QXyfL._SL500_.jpg",
                "https://m.media-amazon.com/images/I/41J+aZeWCkL._SL500_.jpg",
                "https://m.media-amazon.com/images/I/410LWVdSd4L._SL500_.jpg",
                "https://m.media-amazon.com/images/I/41WpSM6jLKL._SL500_.jpg",
                "https://m.media-amazon.com/images/I/41Pft1yPWHL._SL500_.jpg",
                "https://m.media-amazon.com/images/I/41wuMmMBWlL._SL500_.jpg"
            ],
                offer={
                    "mrp": 24500,
                    "discountedPrice": 14999,
                    "percentageOff": 39 
                }
            ),
            Product(
                id="B08BJN4MP3",
                name="HUL Pureit Eco Water Saver Mineral RO+UV+MF AS wall mounted/Counter top Black 10L | Upto 60% Water Savings | Water Purifier",
                description="[Presenting Pureit ECO water saver with high water saving technology that saves up to 60 percent of your water, which is double than ordinary RO's., Mineral enhancer cartridge enriches your water with essential minerals like Calcium Magnesium, providing you with 100% RO water without bypass., Efficient UV sterilization kills up to 99.9% of bacteria, virus \u0026 cyst with a highly effective UV lamp., Smartsense indicators alert you 15 days before filter expiry and suspend water dispensing if the filter is not changed, ensuring you receive mineral-enriched, safe RO water, Highest storage capacity of 10 litres, so that you \u0026 your family never run out of fresh \u0026 safe RO water., Longer filter life of 6000 litres, which is double compared to ordinary RO\u0027s., Purifies all types of drinking water: Borewell, Tanker \u0026 Tap water. Can be used for TDS up to 2000 PPM. Please use a TDS meter to determine the correct TDS of your water source before purchasing a water purifier., Other features: High speed purification up to 24LPH, 7 stage purification, Tested with international labs standards, Membrane protector, 100 percent food grade plastic, Premium design and aesthetics, 24x7 WhatsApp assistance., Color: Black, Capacity: Up to 10 litres, Power: 42 watts, Input Water Temperature: 10 degree celsius to 40 degree celsius, Operative Input voltage: 100-240 Va.c. 50/60 Hz (Device can withstand voltage fluctuation from 100 to 300 V a.c.), Material tank type: Food safe, non toxic engineering grade plastic., Product Dimensions: Length 25.3cm X Width 36.0cm X Height 48.5cm; Storage tank capacity: Upto 10 Litres under running water; Pack inclusions: Water purifier, Installation kit, External sediment filter Warranty card. Excluded in the box: Booster pump, Pressure reducing valve, an Iron cartridge (These are based on pressure condition, to be purchased at the time of installation). Please refer to the device manual for detailed disclaimers/terms conditions.]",
                productFrontImage="https://m.media-amazon.com/images/I/51SdZINqNZL._SL500_.jpg",
                images=[
                "https://m.media-amazon.com/images/I/51SdZINqNZL._SL500_.jpg",
                "https://m.media-amazon.com/images/I/51vaTMrBOIL._SL500_.jpg",
                "https://m.media-amazon.com/images/I/41AV-xJMgNL._SL500_.jpg",
                "https://m.media-amazon.com/images/I/41-kVQjTymL._SL500_.jpg"
            ],
                offer={
                    "mrp": 24850,
                    "discountedPrice": 12599,
                    "percentageOff": 49 
                }
            ),
            Product(
                id="B09X1P3J6G",
                name="Livpure GLO PRO++ RO+UV+UF | Water Purifier for Home - 7 L Storage | Free Standard Installation | Suitable for Borewell, Tanker, Municipal Water | Black",
                description="[Free Installation : Comes with Livpure Smart Service Plan offering Free Installation Free Service on Demand under Warranty., 7 Stage Purification: Livpure GLO PRO++ provides 7 stage advanced purification: 1) Sediment Flter 2) Pre-activated Carbon Absorber 3) Anti-Scalant Cartridge 4) RO Membrane 5) UV Disinfection 6) Ultra Filteration 7) Silver Impregnated Post Carbon Filter, Ultra Filteration: Ultra Filtration disinfects the water by removing bacteria and viruses without removing beneficial minerals, ensuring pure and safe water., Post Carbon filter: Using post carbon filter gets rid of unpleasant smell from water and enhance water flavour. The silver in the filter stops the regrowth of bacteria to provide drinking water that is safe for consumption., UV Disinfection : Ultraviolet radiation disinfects the water from water borne disease causing bacteria, virus and protozoa, making it safe to drink without the need of handling potential dangerous chemicals. UV does not change the taste or odour of the water and consumes less power.]",
                productFrontImage="https://m.media-amazon.com/images/I/41t-M5L8F9L._SL500_.jpg",
                images= [
                "https://m.media-amazon.com/images/I/41t-M5L8F9L._SL500_.jpg",
                "https://m.media-amazon.com/images/I/412DQK3bqvL._SL500_.jpg",
                "https://m.media-amazon.com/images/I/51snILsCr2L._SL500_.jpg",
                "https://m.media-amazon.com/images/I/41sWsuT2rtL._SL500_.jpg",
                "https://m.media-amazon.com/images/I/410HbCx-o5L._SL500_.jpg"
            ],
                offer={
                    "mrp": 15500,
                    "discountedPrice": 6499,
                    "percentageOff": 58
                }
            ),
        ]

        return StoryData(story_title, summary, products)
