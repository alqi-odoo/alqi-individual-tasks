# alqi - Luxer Sale Subscription

[Link](https://www.odoo.com/web#id=3364799&cids=3&menu_id=4720&action=4665&active_id=3364781&model=project.task&view_type=form) to the task.

## Steps to Complete
- [X] Inherit the `account.move` model.
- [X] Inherit the `sale.order` model.
- [X] Add the `site_address` field to both models.
- [X] Inherit the `account.view_move_form` view.
- [X] Inherit the `sale.view_order_form` view.
- [X] Add the `site_address` field to both views.
- [X] Find how the `sale_subscription` module updates an invoice with the data from the sale order.
- [X] Override the `_prepare_invoice` method to include a `site_address` key in the invoice values.

## Issues/Blocking Points
- [X] Unsure where exactly the `sale_subscription` module updates an invoice.

## Topics I Need Clarification On
- N/A
      
## Interns Who Helped Me
- N/A

## Interns I Helped
- N/A
