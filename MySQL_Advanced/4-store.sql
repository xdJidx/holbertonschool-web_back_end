-- 1. Create a trigger that will update the quantity of an item
-- in the items table when a new order is placed. 
CREATE TRIGGER decrease_item_quantity
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
