select api_invoice.amount, api_customer.name
from api_invoice
join api_customer on api_invoice.customer_id = api_customer.id
where api_invoice.amount = 666;