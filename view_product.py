import json
from typing import List


# CustomJSONEncoder = Mock class util for view json
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Category):
            return obj.__dict__
        if isinstance(obj, Promotion):
            return obj.__dict__
        if isinstance(obj, Product):
            return obj.__dict__
        if isinstance(obj, GetProductDetailResponse):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)


# mock category.py
class Category:
    id: int
    categoryName: str

    def __init__(self, id: int, categoryName: str):
        self.id = id
        self.categoryName = categoryName


def getCategory(categoryId: int):
    return next((p for p in getCategories() if p.id == categoryId), None)


def getCategories():
    lips = Category(1, "Lips")
    eyes = Category(2, "Eyes")
    eyebrow = Category(3, "Eyebrow")
    face = Category(4, "Face")
    blush = Category(5, "Blush")
    tools = Category(6, "Tools")

    return [lips, eyes, eyebrow, face, blush, tools]


# mock promotion.py
class Promotion:
    id: int
    promotionName: str
    discount: int

    def __init__(self, id: int, promotionName: str, discount: int):
        self.id = id
        self.promotionName = promotionName
        self.discount = discount


def getPromotion(promotionId: int):
    return next((p for p in getPromotions() if p.id == promotionId), None)


def getPromotions():
    newYearSale = Promotion(1, "New Year Sale", 10)
    summerClearance = Promotion(2, "Summer Clearance", 25)
    holidaySpecial = Promotion(3, "Holiday Special", 15)
    flashSale = Promotion(4, "Flash Sale", 20)
    birthdayDiscount = Promotion(5, "Birthday Discount", 5)

    return [newYearSale, summerClearance, holidaySpecial, flashSale, birthdayDiscount]


# mock product.py
class Product:
    id: int
    productName: str
    price: float
    description: str
    detail: str
    quantity: int
    attribute: List[object]
    categoryId: int
    promotionId: int

    def __init__(self, id: int, productName: str, price: float, description: str, detail: str, quantity: int,
                 attribute: List[object], categoryId: int, promotionId: int):
        self.id = id
        self.productName = productName
        self.price = price
        self.description = description
        self.detail = detail
        self.quantity = quantity
        self.attribute = attribute
        self.categoryId = categoryId
        self.promotionId = promotionId


def getProduct(productId: int):
    return next((p for p in getProducts() if p.id == productId), None)


def getProducts():
    product1 = Product(1, "Lipstick", 10.99, "Long-lasting lipstick",
                       "This lipstick lasts up to 8 hours without fading.", 50,
                       ["Red", "Matte", "Cruelty-free"], 1, 1)

    product2 = Product(2, "Mascara", 8.99, "Volumizing mascara", "Get thick and voluminous lashes with "
                                                                 "this mascara.",
                       30, ["Black", "Waterproof", "Cruelty-free"], 2, 2)
    product3 = Product(3, "Eyeshadow Palette", 24.99, "16 shades eyeshadow palette",
                       "This palette includes 16 shades of eyeshadow for various eye looks.", 20,
                       ["Matte", "Shimmer", "Glitter"], 2, 3)
    product4 = Product(4, "Foundation", 15.99, "Medium coverage foundation",
                       "This foundation provides medium coverage with a natural finish.", 40,
                       ["Fair", "Medium", "Olive"], 4, 5)
    product5 = Product(5, "Blush", 7.99, "Pigmented blush",
                       "Add a pop of color to your cheeks with this highly pigmented blush.", 60,
                       ["Peach", "Rose", "Cruelty-free"], 5, 4)

    return [product1, product2, product3, product4, product5]


class GetProductDetailResponse:
    id: int
    productName: str
    price: float
    description: str
    detail: str
    quantity: int
    attribute: List[object]
    category: Category
    promotion: Promotion


def GetProductDetail():
    productId = 1

    product = getProduct(productId)
    if product is None:
        print(f"productId = {productId} is not found")
        exit(1)

    response = GetProductDetailResponse()
    response.id = product.id
    response.productName = product.productName
    response.price = product.price
    response.description = product.description
    response.detail = product.detail
    response.quantity = product.quantity
    response.attribute = product.attribute
    response.category = getCategory(product.categoryId)
    response.promotion = getPromotion(product.promotionId)

    print(json.dumps(response, cls=CustomJSONEncoder))


# start function get product detail
GetProductDetail()
