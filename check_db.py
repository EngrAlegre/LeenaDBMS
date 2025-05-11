from database import Database

# Initialize database
db = Database()

# Get all deliveries
deliveries = db.get_all_deliveries()

if deliveries:
    print("Found deliveries. First delivery details:")
    print(f"Delivery ID: {deliveries[0][0]}")
    print(f"Departure Time: {deliveries[0][1]}")
    print(f"Date: {deliveries[0][2]}")
    print(f"FoodList ID: {deliveries[0][3]}")
    print(f"Location ID: {deliveries[0][4]}")
    print(f"Org ID: {deliveries[0][5]}")
    print(f"Food List Name: {deliveries[0][6]}")
    print(f"Org Name: {deliveries[0][7]}")
    print(f"Location Name: {deliveries[0][8]}")
    
    print("\nColumn Types:")
    for i, val in enumerate(deliveries[0]):
        print(f"Column {i}: {type(val)}, Value: {val}")
else:
    print("No deliveries found in database")

# Let's also check a direct database query to see what's in the delivery table
print("\nDirect Query from Delivery Table:")
direct_query = db.execute_query("SELECT * FROM delivery")
if direct_query:
    print(f"Raw delivery data: {direct_query[0]}")
    print(f"Date from direct query: {direct_query[0][2]}")
    print(f"Date type: {type(direct_query[0][2])}")
else:
    print("No direct delivery data found") 