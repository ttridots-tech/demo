# Copyright (c) 2025, najmudeen and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Members(Document):
	def before_save(self):
		self.full_name = f"{self.first_name} {self.last_name or ''}"

	def validate(self):
		if not self.age:
			frappe.throw("Age is required")
		
		if self.age < 18:
				frappe.throw("Age must be greater than 18")

	def after_insert(self):
		frappe.msgprint("Member inserted successfully")
		# frappe.sendmail(
		# 	recipients=self.mail_id,
		# 	subject="Welcome to our club",
		# 	message="Welcome to our club. You are now a member of our club."
		# )
		