import stripe
from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def stripe_create_product(course):
    return stripe.Product.create(name=f'Оплата курса "{course.course_name}"')


def stripe_create_price(product, amount):
    return stripe.Price.create(
        currency="rub",
        unit_amount=amount * 100,
        product=product.get("id"),
    )


def stripe_create_session(price):
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
