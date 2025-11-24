// Copyright (c) 2025, najmudeen and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Member", {
// 	before_save(frm) {
//         frm.doc.full_name = `${frm.doc.first_name} ${frm.doc.last_name || ""}`;

// 	},
// });

// frappe.ui.form.on("Member", {
//     refresh(frm) {
//         frappe.msgprint("Form refreshed!");
//     },
// });
  

// frm.toggle_display("salary", true);   // show
frappe.ui.form.on("Member", {
    refresh(frm) {
        frm.toggle_display("mail_id", false);  // hide field
        frm.toggle_reqd("mail_id", false);     // required should be OFF
        frm.toggle_enable("mail_id", false);   // optional (hidden fields don't need enable)
    }
});

// ---- Action Buttons

// frappe.ui.form.on("Member", {
//     refresh(frm) {
//         frm.add_custom_button("Say Hello", () => {
//             frappe.msgprint("Hello from custom button!");
//         });
        
//         frm.add_custom_button("Open google", () => {
//             window.open("https://www.google.com/", "_blank");
//         }, "Action");
//     },
// });

frappe.ui.form.on("Member", {
    first_name(frm) {
        frm.set_value("full_name", `${frm.doc.first_name} ${frm.doc.last_name || ""}`);

    },
});

frappe.ui.form.on("Member", {
    last_name(frm) {
        frm.set_value("full_name", `${frm.doc.first_name} ${frm.doc.last_name || ""}`);

    },
});

// --- Set Secondary Button

frappe.ui.form.on("Member", {
    refresh(frm) {
        frm.page.set_secondary_action("Download PDF", () => {
            frappe.msgprint("PDF Downloaded!");
        });
    }
});

// --- Set Primary Buttom

// frappe.ui.form.on("Member", {
//     refresh(frm) {
//         frm.page.set_primary_action("Say Hello", () => {
//             frappe.msgprint("Hello from custom button!");
//         });
//     }
// });