from rest_framework.test import APITestCase, APIClient

from order_pizza_app.models import Pizza


class PizzaAPITestCase(APITestCase):

    """
    Pizza API
    """

    url = '/api/pizza/'
    client = APIClient()

    # def setUp(self):
    #     pizza_name = "PizzaTest"
    #     description = "Pizza test description"
    #     new_pizza = Pizza(pizza_name=pizza_name, description=description)
    #     new_pizza.save()

    def test_get_pizza_list(self):
        """GET /api/pizza/ returns a list of pizzas"""
        new_pizza = Pizza(pizza_name="Some pizza name", description="Pizza test description")
        new_pizza.save()
        resp = self.client.get(self.url, format='json')

        self.assertTrue(len(resp.data) == Pizza.objects.count())

    def test_get_pizza_by_id(self):

        """GET api/pizza/{pk}/ returns a pizza"""
        pizza_name = "PizzaTest"
        description = "Pizza test description"
        new_pizza = Pizza(pizza_name=pizza_name, description=description)
        new_pizza.save()

        url_detail = self.url + str(new_pizza.id) + '/'
        resp = self.client.get(url_detail)

        self.assertTrue(resp.data == {'pizza_name': pizza_name, 'description': description})

    def test_create_new_pizza(self):
        """POST /api/pizza/ returns a pizza"""
        resp = self.client.post(self.url, {'pizza_name': 'Some pizza name', 'description': 'Pizza test description'})

        self.assertEqual(resp.status_code, 201)

    def test_update_pizza_by_id(self):
        """PUT api/pizza/{pk}/ returns a pizza"""
        pizza_name = "PizzaTest"
        description = "Pizza test description"
        new_pizza = Pizza(pizza_name=pizza_name, description=description)
        new_pizza.save()

        url_detail = self.url + str(new_pizza.id) + '/'
        resp = self.client.put(url_detail, {'pizza_name': 'New pizza name', 'description': 'New pizza description'})

        checged_pizza = Pizza.objects.get(id=new_pizza.id)
        changed_pizza_name = checged_pizza.pizza_name
        changed_pizza_description = checged_pizza.description

        self.assertTrue(resp.data == {'pizza_name': changed_pizza_name, 'description': changed_pizza_description})
        self.assertEqual(resp.status_code, 200)

    def test_delete_pizza_by_id(self):
        """DELETE /api/pizza/{pk}/ returns a pizza"""
        pizza_name = "PizzaTest"
        description = "Pizza test description"
        new_pizza = Pizza(pizza_name=pizza_name, description=description)
        new_pizza.save()
        url_detail = self.url + str(new_pizza.id) + '/'

        resp = self.client.delete(url_detail)

        self.assertEqual(Pizza.objects.filter(id=new_pizza.id).count(),0)
        self.assertEqual(resp.status_code, 204)
