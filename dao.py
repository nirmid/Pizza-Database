# Data Access Objects:
# All of these are meant to be singletons
from dto import Hat, Supplier


class _Hats:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, hat):
        self._conn.execute("""
               INSERT INTO hats (id, topping, supplier, quantity) VALUES (?, ?, ? ,?)
           """, [hat.id, hat.topping, hat.supplier, hat.quantity])

    def find(self, topping):
        c = self._conn.cursor()
        c.execute("""
            SELECT * FROM hats WHERE topping = ? ORDER BY supplier
        """, [topping])

        return Hat(*c.fetchone())

    def update(self, hat):
        self._conn.execute("""
        UPDATE hats SET quantity=(?) WHERE id=(?) 
        """, [hat.quantity-1, hat.id])
        if hat.quantity-1 == 0:
            self._conn.execute("""
                    DELETE FROM hats WHERE id=(?)
                    """, [hat.id])


class _Suppliers:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, supplier):
        self._conn.execute("""
                INSERT INTO suppliers (id, name) VALUES (?, ?)
        """, [supplier.id, supplier.name])

    def find(self, id):
        c = self._conn.cursor()
        c.execute("""
                SELECT * FROM suppliers WHERE id = ?
            """, [id])

        return Supplier(*c.fetchone())


class _Orders:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, order):
        self._conn.execute("""
            INSERT INTO orders (id, location, hat) VALUES (?, ?, ?)
        """, [order.id, order.location, order.hat])
