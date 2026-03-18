import frappe
from frappe.model.document import Document


class PaymentMethodMaster(Document):
	def validate(self):
		if not self.payment_method_id:
			frappe.throw("Payment Method ID is required")

		if not isinstance(self.payment_method_id, int):
			frappe.throw("Payment Method ID must be integer")

		if self.payment_method_id < 0:
			frappe.throw("Payment Method ID cannot be negative")

		if not self.payment_method_name:
			frappe.throw("Payment Method Name is required")
