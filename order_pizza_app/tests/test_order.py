from rest_framework.test import APITestCase, APIClient

from order_pizza_app.models import Pizza, Order


PIZZA_NAME1 = "PizzaTest1"
DESCRIPTION1 = "Pizza test description1"
PIZZA_NAME2 = "PizzaTest2"
DESCRIPTION2 = "Pizza test description2"
PIZZA_SIZE = "30cm"
CUSTOMER_NAME = "TestCustomer"
CUSTOMER_NAME2 = "TestCustomer2"
ADDRESS = "Test address 123"


class OrderAPITestCase(APITestCase):
    """
    Order API
    """

    url = '/api/order/'
    client = APIClient()

    def test_get_order_list(self):
        """GET /api/order/ returns a list of orders"""
        pizza = self._create_pizza(PIZZA_NAME1, DESCRIPTION1)
        test_order = Order(pizza_id=pizza.id, pizza_size=PIZZA_SIZE,
                           customer_name=CUSTOMER_NAME, address=ADDRESS)
        test_order.save()

        resp = self.client.get(self.url)

        self.assertTrue(len(resp.data) == Pizza.objects.count())

    def test_get_order_by_id(self):
        """GET api/order/{pk}/ returns an order"""
        pizza = self._create_pizza(PIZZA_NAME1, DESCRIPTION1)
        test_order = Order(pizza_id=pizza.id, pizza_size=PIZZA_SIZE,
                           customer_name=CUSTOMER_NAME, address=ADDRESS)
        test_order.save()

        url_detail = self.url + str(test_order.id) + '/'
        resp = self.client.get(url_detail)

        self.assertTrue(resp.data == {
            'pizza': pizza.id,
            'pizza_size': PIZZA_SIZE,
            'customer_name': CUSTOMER_NAME,
            'address': ADDRESS
        })

    def test_get_order_by_customer_name(self):
        """GET api/order/?customer_name={string} returns a list of orders"""
        pizza = self._create_pizza(PIZZA_NAME1, DESCRIPTION1)
        test_order1 = Order(pizza_id=pizza.id, pizza_size=PIZZA_SIZE,
                           customer_name=CUSTOMER_NAME, address=ADDRESS)
        test_order2 = Order(pizza_id=pizza.id, pizza_size=PIZZA_SIZE,
                           customer_name=CUSTOMER_NAME2, address=ADDRESS)
        test_order1.save()
        test_order2.save()

        url_detail = self.url + '?customer_name=' + test_order2.customer_name

        resp = self.client.get(url_detail)

        self.assertTrue(resp.data == [{
            'pizza': pizza.id,
            'pizza_size': PIZZA_SIZE,
            'customer_name': CUSTOMER_NAME2,
            'address': ADDRESS
        }])

    def test_create_new_order(self):
        """POST /api/order/ returns an order"""
        pizza = self._create_pizza(PIZZA_NAME1, DESCRIPTION1)

        resp = self.client.post(self.url, {
            'pizza': pizza.id,
            'pizza_size': PIZZA_SIZE,
            'customer_name': CUSTOMER_NAME,
            'address': ADDRESS
        }, format='json')

        self.assertEqual(resp.status_code, 201)

    def test_update_order_by_id(self):
        """PUT api/order/{pk}/ returns an order"""
        pizza1 = self._create_pizza(PIZZA_NAME1, DESCRIPTION1)
        pizza2 = self._create_pizza(PIZZA_NAME2, DESCRIPTION2)
        test_order = Order(pizza_id=pizza1.id, pizza_size=PIZZA_SIZE,
                           customer_name=CUSTOMER_NAME, address=ADDRESS)
        test_order.save()

        url_detail = self.url + str(test_order.id) + '/'

        resp = self.client.put(url_detail, {
            'pizza': pizza2.id,
            'pizza_size': "50cm",
            'customer_name': "Test Customer2",
            'address': "Teas Address 234"
        })

        changed_order = Order.objects.get(id=test_order.id)

        self.assertTrue(resp.data == {
            'pizza': changed_order.pizza_id,
            'pizza_size': changed_order.pizza_size,
            'customer_name': changed_order.customer_name,
            'address': changed_order.address
        })
        self.assertEqual(resp.status_code, 200)

    def test_delete_pizza_by_id(self):
        """DELETE /api/pizza/{pk}/ returns an order"""
        pizza = self._create_pizza(PIZZA_NAME1, DESCRIPTION1)
        test_order = Order(pizza_id=pizza.id, pizza_size=PIZZA_SIZE,
                           customer_name=CUSTOMER_NAME, address=ADDRESS)
        test_order.save()

        url_detail = self.url + str(test_order.id) + '/'

        resp = self.client.delete(url_detail)

        self.assertEqual(Pizza.objects.filter(id=pizza.id).count(), 1)
        self.assertEqual(Order.objects.filter(id=test_order.id).count(), 0)
        self.assertEqual(resp.status_code, 204)

    def _create_pizza(self, pizza_name, description):
        """create instance of Pizza class, return pizza_id"""
        test_pizza = Pizza(pizza_name="PizzaTest",
                           description="Pizza test description")
        test_pizza.save()
        return test_pizza
