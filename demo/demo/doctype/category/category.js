// Copyright (c) 2025, najmudeen and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Category", {
// 	refresh(frm) {

// 	},
// });


frappe.treeview_settings['Category'] = {
    breadcrumb: "Category",
    title: "Category Tree",
    fields: ["category_name", "description"],
    get_tree_nodes: "demo.api.get_category_nodes",
    onload: function(tree) {
        console.log("Tree Loaded");
    }
};

