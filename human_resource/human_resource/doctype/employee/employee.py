# Copyright (c) 2023, mahmoud and contributors
# For license information, please see license.txt

# import frappe
from frappe import *
from frappe.model.document import Document
from datetime import datetime
class Employee(Document):
 def validate(doc): 
  if doc.date_of_brith:
    today = datetime.now()
    dob = datetime.strptime(doc.date_of_brith, '%Y-%m-%d')
    doc.age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    if doc.age > 60:
     throw("age cannot be more than 60 years.")
		

  else:
	    throw("choose your birthday")
