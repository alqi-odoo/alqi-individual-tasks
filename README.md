# alqi - NY P&W Shoes

[Link](https://www.odoo.com/web#id=3364783&cids=3&menu_id=4720&action=4665&active_id=3364781&model=project.task&view_type=form) to the task.

## Steps to Complete
- [X] Inherit the `product.template` model.
- [X] Add the `pairs_per_case` field.
- [X] Add the `price_per_pair` field.
- [X] Override the `list_price` field to make it computed.
- [X] Add a compute and inverse method for the `list_price` field.
- [X] Inherit the `product.product_template_only_form_view` view.
- [X] Add the `pairs_per_case` and `price_per_pair` fields to the view.
- [X] Add a new `detailed_type` called `shoes`.
- [X] Make the `pairs_per_case` and `price_per_pair` fields only visible when the `detailed_type` is set to `shoes`.
- [X] Make the `list_price` read-only if and only if either of `pairs_per_case` or `price_per_pair` is not equal to 0.
- [X] Add constraints to ensure that the `pairs_per_case` and `price_per_pair` fields are non-negative.

## Issues/Blocking Points
- [X] Unsure whether `list_price` should be read-only if both of the `pairs_per_case` and `price_per_pair` fields are not equal to 0 or if either of the fields is not equal to 0.

## Topics I Need Clarification On
- N/A
      
## Interns Who Helped Me
- N/A

## Interns I Helped
- N/A
