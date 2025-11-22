# Copyright (c) 2025, najmudeen and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Members(Document):

	def validate(self):
		if not self.age:
			frappe.throw("Age is required")
		
		if self.age < 18:
				frappe.throw("Age must be greater than 18")

	# def after_insert(self):
		# frappe.msgprint("Member inserted successfully")
		# frappe.sendmail(
		# 	recipients=self.mail_id,
		# 	subject="Welcome to our club",
		# 	message="Welcome to our club. You are now a member of our club."
		# )


@frappe.whitelist()
def get_members_with_empty_email():
	"""Get members with empty email addresses"""
	members = frappe.get_all("Members",
		filters={"mail_id": ""},
		fields=["name", "full_name", "mail_id"]
	)
	return members

@frappe.whitelist()
def get_mail_id():
	email = frappe.db.get_value("Members", "61", "mail_id")
	return email


@frappe.whitelist()
def create_member():
	"""Create a new member"""
	first_name = "Siva"
	last_name = "Kumaran"
	full_name = f"{first_name} {last_name}".strip()
	
	member = frappe.get_doc({
		"doctype": "Members",
		"first_name": first_name,
		"last_name": last_name,
		"full_name": full_name,
		"mail_id": "siva@test.com",
		"age": 23
	})
	member.insert()
	return member
