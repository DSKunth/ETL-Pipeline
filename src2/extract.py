import psycopg2
import pandas as pd


def connect_to_redshift(dbname, host, port, user, password):
    """Method that connects to redshift. This gives a warning so will look for another solution"""

    connect = psycopg2.connect(
        dbname=dbname, host=host, port=port, user=user, password=password
    )

    print("connection to redshift made")

    return connect

def extract_transaction_data(dbname, host, port, user, password):
    """
    This function connects to redshift, extracts online transactions data and carry out the following transformation tasks:
    1. Select everything from online_transaction table and description from stock_description table
    2. Filters on where customer_id is not equal to ‘’
    3. Filters on where stock_code not in BANK CHARGES, POST, D, M, CRUK
    4. If the description is null replaces it with 'Unknown'
    5. Fix the invoice_date field from object to datetime
    6. Add a variable/column for total order value (price x quantity)

    """

    # connect to redshift
    connect = connect_to_redshift(dbname, host, port, user, password)

    # query to extract online transactions data

    query = """
    SELECT ot.invoice, 
           ot.stock_code,
           CASE WHEN s.description IS NULL THEN 'Unknown'
                ELSE s.description END AS description,
           ot.price,
           ot.quantity,
            /* add a column for total order value */
           ot.price * ot.quantity AS total_order_value,
           CAST(invoice_date As DateTime) AS invoice_date,
           ot.customer_id,
           ot.country
    FROM bootcamp.online_transactions ot
    /* this is a subquery that removes '?' from the stock_description table */
    LEFT JOIN ( SELECT *
                FROM bootcamp.stock_description
                WHERE description <> '?') AS s
    ON ot.stock_code = s.stock_code
    WHERE ot.customer_id <> ''
    AND ot.stock_code NOT IN ('BANK CHARGES', 'POST', 'D', 'M', 'CRUK')
    """

    online_trans_cleaned = pd.read_sql(query, connect)

    print('The shape of the extracted and transformed data:', online_trans_cleaned.shape)

    return online_trans_cleaned
