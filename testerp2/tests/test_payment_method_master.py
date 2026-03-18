import frappe
from frappe.tests.utils import FrappeTestCase


class TestPaymentMethodMaster(FrappeTestCase):

    def test_create_payment_method(self):
        doc = frappe.get_doc(
            {
                "doctype": "Payment Method Master",
                "payment_method_id": 1,
                "payment_method_name": "UPI",
            }
        )
        doc.insert()

        self.assertTrue(doc.name)

    def test_invalid_id(self):
        self.assertRaises(
            Exception,
            frappe.get_doc(
                {
                    "doctype": "Payment Method Master",
                    "payment_method_id": "ABC",
                    "payment_method_name": "Card",
                }
            ).insert,
        )
