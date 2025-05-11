import sqlite3

def fix_database():
    print("Performing database overhaul...")
    
    try:
        # Connect to the database
        conn = sqlite3.connect("donationdriveDBMS.db")
        cursor = conn.cursor()
        
        # Completely recreate the delivery with correct values
        cursor.execute("DELETE FROM delivery WHERE delivery_id = 1")
        
        # Insert the correct data directly
        cursor.execute("""
            INSERT INTO delivery (delivery_id, departure_time, date, foodList_id, location_id, org_id)
            VALUES (1, '09:00', '2025-05-12', 1, 'QC', 1)
        """)
        conn.commit()
        
        # Verify the changes directly with column names
        cursor.execute("""
            SELECT 
                d.delivery_id, 
                d.departure_time, 
                d.date, 
                d.foodList_id,
                f.name AS food_list_name,
                d.org_id,
                o.name AS org_name,
                d.location_id,
                l.location_name
            FROM delivery d
            JOIN food_list f ON d.foodList_id = f.foodList_id
            JOIN org_info o ON d.org_id = o.org_id
            JOIN location_info l ON d.location_id = l.location_id
            WHERE d.delivery_id = 1
        """)
        
        # Get column names
        columns = [description[0] for description in cursor.description]
        print("Database columns:", columns)
        
        # Get the data
        result = cursor.fetchone()
        if result:
            print("\nDatabase values:")
            for i, col in enumerate(columns):
                print(f"{col}: {result[i]}")
            
            # Make sure the organization value is CARE Philippines
            org_name = result[6]  # org_name should be at index 6
            if org_name != "CARE Philippines":
                print(f"Warning: Organization is '{org_name}', not 'CARE Philippines'")
                
            # Make sure location is Quezon City
            location_name = result[8]  # location_name should be at index 8
            if location_name != "Quezon City":
                print(f"Warning: Location is '{location_name}', not 'Quezon City'")
                
            # Make sure food list starts with "Food List 1"
            food_list_name = result[4]  # food_list_name should be at index 4
            if not food_list_name.startswith("Food List 1"):
                print(f"Warning: Food list is '{food_list_name}', doesn't start with 'Food List 1'")
        else:
            print("Failed to retrieve delivery data")
        
        conn.close()
        print("\nDatabase overhaul completed")
    except Exception as e:
        print(f"Error fixing database: {e}")

if __name__ == "__main__":
    fix_database() 