from src.models import Schema, Table, Column

menu_schema = Schema(
    tables=[
        Table(name='menu_items', columns=[
            Column(name='category'), 
            Column(name='item'), 
            Column(name='solo_price'), 
            Column(name='meal_price')
            ]
            )
        ]
)

menu_data = {'tables': [
    {'name': 'menu_items', 'columns': [
        {'category': 'BREAKFAST', 'item': 'BACON, EGG & CHEESE BISCUIT', 'solo_price': '$3.19', 'meal_price': '$4.39'}, 
        {'category': 'BREAKFAST', 'item': 'EGG MCMUFFIN®', 'solo_price': '$2.79', 'meal_price': '$3.99'}, 
        {'category': 'BREAKFAST', 'item': 'SAUSAGE MCMUFFIN®', 'solo_price': '$1.19', 'meal_price': None}, 
        {'category': 'BREAKFAST', 'item': 'SAUSAGE MCMUFFIN® WITH EGG', 'solo_price': '$3.19', 'meal_price': '$4.19'}, 
        {'category': 'BREAKFAST', 'item': 'SAUSAGE BISCUIT', 'solo_price': '$2.99', 'meal_price': None}, 
        {'category': 'BREAKFAST', 'item': 'SAUSAGE BISCUIT WITH EGG', 'solo_price': '$2.79', 'meal_price': '$3.99'}, 
        {'category': 'BREAKFAST', 'item': 'BACON, EGG & CHEESE MCGRIDDLES®', 'solo_price': '$3.29', 'meal_price': '$4.49'}, 
        {'category': 'BREAKFAST', 'item': 'SAUSAGE MCGRIDDLES®', 'solo_price': '$2.79', 'meal_price': '$4.49'}, 
        {'category': 'BREAKFAST', 'item': 'SAUSAGE, EGG & CHEESE MCGRIDDLES ®', 'solo_price': '$3.29', 'meal_price': '$4.49'}, 
        {'category': 'BREAKFAST', 'item': 'BIG BREAKFAST®', 'solo_price': '$3.69', 'meal_price': None}, 
        {'category': 'BREAKFAST', 'item': 'BIG BREAKFAST® WITH HOTCAKES', 'solo_price': '$5.49', 'meal_price': None}, 
        {'category': 'BREAKFAST', 'item': 'HOTCAKES', 'solo_price': '$2.49', 'meal_price': None}, 
        {'category': 'BREAKFAST', 'item': 'HOTCAKES AND SAUSAGE', 'solo_price': '$3.19', 'meal_price': None}, 
        {'category': 'BREAKFAST', 'item': 'SAUSAGE BURRITO', 'solo_price': '$2.39', 'meal_price': '$4.29'}, 
        {'category': 'BREAKFAST', 'item': 'HASH BROWNS', 'solo_price': '$1.09', 'meal_price': None}, 
        {'category': 'BREAKFAST', 'item': 'FRUIT & MAPLE OATMEAL', 'solo_price': '$1.99', 'meal_price': None}, 
        {'category': 'BURGERS', 'item': 'MCRIB®', 'solo_price': '$3.69', 'meal_price': '$7.49'}, 
        {'category': 'BURGERS', 'item': 'BIG MAC®', 'solo_price': '$3.99', 'meal_price': '$5.99'}, 
        {'category': 'BURGERS', 'item': 'QUARTER POUNDER® WITH CHEESE', 'solo_price': '$3.79', 'meal_price': '$5.79'}, 
        {'category': 'BURGERS', 'item': 'DOUBLE QUARTER POUNDER® WITH CHEESE', 'solo_price': '$4.79', 'meal_price': '$6.69'}, 
        {'category': 'BURGERS', 'item': 'QUARTER POUNDER® WITH CHEESE DELUXE', 'solo_price': '$5.79', 'meal_price': '$8.69'}, 
        {'category': 'BURGERS', 'item': 'MCDOUBLE®', 'solo_price': '$2.52', 'meal_price': None}, 
        {'category': 'BURGERS', 'item': 'QUARTER POUNDER® WITH CHEESE BACON', 'solo_price': '$5.99', 'meal_price': '$8.99'}, 
        {'category': 'BURGERS', 'item': 'CHEESEBURGER', 'solo_price': '$2.79', 'meal_price': '$6.59'}, 
        {'category': 'BURGERS', 'item': 'DOUBLE CHEESEBURGER', 'solo_price': '$2.59', 'meal_price': None}, 
        {'category': 'BURGERS', 'item': "HAMBURGER: THE CLASSIC MCDONALD'S BURGER", 'solo_price': '$2.49', 'meal_price': None}, 
        {'category': 'CHICKEN & FISH SANDWICHES', 'item': 'CRISPY CHICKEN SANDWICH', 'solo_price': '$4.29', 'meal_price': '$7.49'}, 
        {'category': 'CHICKEN & FISH SANDWICHES', 'item': 'DELUXE CRISPY CHICKEN SANDWICH', 'solo_price': '$4.89', 'meal_price': '$7.99'}, 
        {'category': 'CHICKEN & FISH SANDWICHES', 'item': 'SPICY CHICKEN SANDWICH', 'solo_price': '$4.49', 'meal_price': '$7.59'}, 
        {'category': 'CHICKEN & FISH SANDWICHES', 'item': 'SPICY DELUXE CRISPY CHICKEN SANDWICH', 'solo_price': '$4.99', 'meal_price': '$7.99'}, 
        {'category': 'CHICKEN & FISH SANDWICHES', 'item': 'FILET-O-FISH®', 'solo_price': '$3.79', 'meal_price': '$5.79'}, 
        {'category': 'CHICKEN & FISH SANDWICHES', 'item': 'MCCHICKEN®', 'solo_price': '$2.49', 'meal_price': None}]
    }
    ], 
    'relationships': None
}
