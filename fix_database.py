from database import Database

def fix_database():
    """Fix the database structure by swapping date and foodList_id where needed"""
    print("Starting database fix script...")
    
    # Initialize database
    db = Database()
    
    # Get all deliveries
    query = "SELECT delivery_id, departure_time, date, foodList_id, location_id, org_id FROM delivery"
    all_deliveries = db.execute_query(query)
    
    if not all_deliveries:
        print("No deliveries found in the database.")
        return
    
    print(f"Found {len(all_deliveries)} delivery records to process.")
    
    # For each delivery, check if the date and foodList_id are swapped
    for delivery in all_deliveries:
        delivery_id = delivery[0]
        departure_time = delivery[1]
        date_field = delivery[2]
        foodlist_id_field = delivery[3]
        location_id = delivery[4]
        org_id = delivery[5]
        
        print(f"Processing delivery ID {delivery_id}:")
        print(f"  Current values: date={date_field}, foodList_id={foodlist_id_field}")
        
        # Check if the date field contains a valid date
        is_date_correct = isinstance(date_field, str) and "-" in date_field
        
        # Check if the foodList_id field contains a valid date instead
        is_foodlist_id_date = isinstance(foodlist_id_field, str) and "-" in foodlist_id_field
        
        if is_date_correct and not is_foodlist_id_date:
            print(f"  Entry already correct for delivery ID {delivery_id}")
            continue
            
        if not is_date_correct and is_foodlist_id_date:
            # The fields are swapped, so swap them back
            correct_date = foodlist_id_field
            
            # Try to determine the correct food list ID
            if date_field and isinstance(date_field, int):
                correct_foodlist_id = date_field
            elif date_field and isinstance(date_field, str) and date_field.isdigit():
                correct_foodlist_id = int(date_field)
            else:
                # Default to 1 if we can't determine
                correct_foodlist_id = 1
                
            print(f"  Fixing: date={correct_date}, foodList_id={correct_foodlist_id}")
            
            # Update the record in the database
            update_query = """
                UPDATE delivery 
                SET date = ?, foodList_id = ? 
                WHERE delivery_id = ?
            """
            try:
                db.cursor.execute(update_query, (correct_date, correct_foodlist_id, delivery_id))
                db.commit()
                print(f"  ✓ Fixed delivery ID {delivery_id}")
            except Exception as e:
                print(f"  ✗ Error fixing delivery ID {delivery_id}: {e}")
        else:
            print(f"  ⚠ Couldn't determine fix for delivery ID {delivery_id}")
    
    print("Database fix completed.")
    
    # Verify the fixes
    all_deliveries = db.execute_query(query)
    print("\nVerifying fixes:")
    for delivery in all_deliveries:
        delivery_id = delivery[0]
        date_field = delivery[2]
        foodlist_id_field = delivery[3]
        print(f"Delivery ID {delivery_id}: date={date_field}, foodList_id={foodlist_id_field}")
    
    db.close()

if __name__ == "__main__":
    fix_database() 