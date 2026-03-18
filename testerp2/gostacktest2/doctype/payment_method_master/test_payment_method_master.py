import frappe
from frappe.tests.utils import FrappeTestCase


class TestPaymentMethodMaster(FrappeTestCase):
	def test_create_valid_payment_method(self):
		doc = frappe.get_doc(
			{
				"doctype": "Payment Method Master",
				"payment_method_id": 1,
				"payment_method_name": "UPI",
			}
		)
		doc.insert()

		self.assertIsNotNone(doc.name)

	def test_missing_name(self):
		with self.assertRaises(frappe.ValidationError):
			doc = frappe.get_doc({"doctype": "Payment Method Master", "payment_method_id": 2})
			doc.insert()

	def test_invalid_id_type(self):
		with self.assertRaises(frappe.ValidationError):
			doc = frappe.get_doc(
				{
					"doctype": "Payment Method Master",
					"payment_method_id": "ABC",
					"payment_method_name": "Card",
				}
			)
			doc.insert()

	def test_negative_id(self):
		with self.assertRaises(frappe.ValidationError):
			doc = frappe.get_doc(
				{
					"doctype": "Payment Method Master",
					"payment_method_id": -1,
					"payment_method_name": "Cash",
				}
			)
			doc.insert()
