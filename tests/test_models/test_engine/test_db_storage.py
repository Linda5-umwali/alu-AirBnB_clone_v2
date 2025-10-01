#!/usr/bin/python3
"""
Unittests for DBStorage engine
"""
import os
import unittest
import MySQLdb
from console import HBNBCommand


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                 "Tests only apply to DB storage")
class TestDBStorage(unittest.TestCase):
    """Test cases for DB storage"""

    def setUp(self):
        """Set up DB connection + console"""
        self.conn = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB'),
            port=3306
        )
        self.cur = self.conn.cursor()
        self.console = HBNBCommand()

    def tearDown(self):
        """Close DB connection"""
        self.cur.close()
        self.conn.close()

    def test_create_state_in_db(self):
        """
        Validate that `create State name="California"`
        actually inserts a row into states table
        """
        # Step 1: count before
        self.cur.execute("SELECT COUNT(*) FROM states;")
        old_count = self.cur.fetchone()[0]

        # Step 2: execute console command
        self.console.onecmd('create State name="California"')

        # Step 3: count after
        self.cur.execute("SELECT COUNT(*) FROM states;")
        new_count = self.cur.fetchone()[0]

        # Step 4: validate difference
        self.assertEqual(new_count, old_count + 1)

    def test_create_city_in_db(self):
        """
        Validate that `create City name="San_Francisco" state_id=<id>`
        inserts a row into cities table
        """
        # First create a State
        self.console.onecmd('create State name="Nevada"')
        self.cur.execute("SELECT id FROM states WHERE name='Nevada';")
        state_id = self.cur.fetchone()[0]

        # Count cities before
        self.cur.execute("SELECT COUNT(*) FROM cities;")
        old_count = self.cur.fetchone()[0]

        # Create city linked to that state
        self.console.onecmd(f'create City name="Reno" state_id="{state_id}"')

        # Count cities after
        self.cur.execute("SELECT COUNT(*) FROM cities;")
        new_count = self.cur.fetchone()[0]

        self.assertEqual(new_count, old_count + 1)
