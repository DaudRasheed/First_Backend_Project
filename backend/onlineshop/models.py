from django.db import models

# Create your models here.
# The `TimestampModel` class is an abstract model in Python with `created_at` and `updated_at` fields
# representing timestamps.
class TimestampModel(models.Model):
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)
    # The class Meta is defined with an abstract attribute set to True.
    class Meta:
        # In Django models, setting `abstract = True` in the `Meta` class of a model indicates that
        # the model is an abstract base class. Abstract base classes are used to define fields and
        # methods that can be inherited by other models but are not intended to be used to create
        # database tables for themselves.
        abstract = True
# This Python class defines a model for a category with attributes for category name and description.
class Category(TimestampModel):
    category_name = models.CharField(max_length=180)
    description = models.TextField(max_length=250)
    
    def __str__(self):
        """
        The above function defines a `__str__` method that returns the `category_name` attribute of an
        object when it is converted to a string.
        :return: The `__str__` method is returning the `category_name` attribute of the object.
        """
        return self.category_name
# This Python class defines a Product model with fields for product name, description, price, image,
# and category.
class Product(TimestampModel):
    product_name = models.CharField(max_length=180)
    description = models.TextField(max_length=180)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.FileField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) :
        return self.product_name
# This Python class defines an order model with fields for customer name, email, product, and
# quantity.
class Order(TimestampModel):
    customer_name = models.CharField(max_length=180)
    customer_email = models.EmailField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    """
        The function defines a model field for quantity and a string representation method for an order
        object.
        :return: The `__str__` method is being defined for a model class. It returns a string
        representation of an instance of the model class. In this case, it returns a string in the format
        "Order #{self.id}", where `self.id` is the id of the instance.
        """

    def __str__(self) :
        return f"Order #{self.id}"
