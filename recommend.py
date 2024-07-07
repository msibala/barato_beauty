
import sqlite3

def get_recommendations(skin_type, budget):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    
    cur.execute("""
        SELECT * FROM products 
        WHERE skin_type = ? AND budget_category = ?
        LIMIT 5
    """, (skin_type, budget))
    
    recommendations = cur.fetchall()
    conn.close()
    
    return recommendations

# Example usage
skin_type = "oily"
budget = "low"
recommendations = get_recommendations(skin_type, budget)
for product in recommendations:
    print(f"Name: {product[1]}, Price: ${product[3]}")