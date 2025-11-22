# Copyright (c) 2025, najmudeen and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Sample(Document):
	def before_save(self):
		self.filed_3 = f"{self.filed_1} {self.filed_2}"
