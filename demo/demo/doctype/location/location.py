import frappe
from frappe.model.document import Document

class Location(Document):
    pass

@frappe.whitelist()
def get_children(doctype, parent=None, **filters):
    if parent in ("", None):
        parent = None
    
    locations = frappe.get_list(
        "Location",
        fields=["name as value", "location_name as title", "is_group"],
        filters={"parent_location": parent},
        order_by="location_name"
    )
    return locations

@frappe.whitelist()
def add_node():
    args = frappe.local.form_dict
    new_location = frappe.new_doc("Location")
    new_location.location_name = args.location_name
    new_location.parent_location = args.parent
    new_location.is_group = 0
    new_location.insert()
    frappe.db.commit()
    return new_location.name
