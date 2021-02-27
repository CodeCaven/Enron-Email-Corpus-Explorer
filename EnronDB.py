import MySQLdb

class EnronDB:
    """The database class that connects to a MYSQL database"""
    def __init__(self, user, pword, database):
        """Constructor
        Input: username and password of MySQL connection and database name"""
        self.username = user
        self.password = pword
        self.database = database
        try:
            self.db = MySQLdb.connect("localhost", self.username, self.password, self.database)
            self.cursor = self.db.cursor()
        except:
            print("Database load error ")

    def get_edge_data(self):
        """Edge data for graph"""
        sql = "SELECT m.sender, r.rvalue FROM MESSAGE m, recipientinfo r WHERE m.mid = r.mid"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_employees(self):
        """Enron employees list"""
        sql = "SELECT firstName,lastName,email_id FROM employeelist ORDER BY lastName,firstName"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_user_messages_by_email(self, email):

        """User messages by email address"""

        sql = "SELECT m.sender, r.rvalue, DATE_FORMAT(m.date, '%%Y/%%m/%%d')," \
              " DATE_FORMAT(m.date, '%%H:%%i:%%s'), m.subject, r.rid" \
              " from message m, recipientinfo r " \
              "WHERE m.mid = r.mid " \
              "AND (r.rvalue = '%s' OR m.sender = '%s')" % (email, email)
              #"ORDER by m.sender, r.rvalue, m.date"
                # take out ordering due to speed issues

        try:
            self.cursor.execute(sql)
        except Exception as e:
            print("DEV: DB ERROR")
            print(e)
            return ()
        return self.cursor.fetchall()

    def get_message_by_rid(self, rid):
        """Get user message by its id"""
        sql = "SELECT m.sender, r.rvalue, r.rtype, m.subject, DATE_FORMAT(m.date, '%%Y/%%m/%%d'), DATE_FORMAT(m.date, '%%H:%%i:%%s')," \
              "m.body FROM message m, recipientinfo r " \
              "WHERE m.mid = r.mid "\
              "AND r.rid = '%d'" % (rid)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def full_text_search_subject(self, search_term):
        """Implemntation of Vector Space Model in MySQL natural language mode subject"""
        sql = "SELECT m.sender, r.rvalue, DATE_FORMAT(m.date, '%%Y/%%m/%%d')," \
              " DATE_FORMAT(m.date, '%%H:%%i:%%s'), m.subject, r.rid" \
              " from message m, recipientinfo r " \
              "WHERE m.mid = r.mid " \
              "AND MATCH(m.subject) AGAINST('%s' IN NATURAL LANGUAGE MODE)" % (search_term)
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            return ()

    def full_text_search_message(self, search_term):
        """Implemntation of Vector Space Model in MySQL natural language mode message"""
        sql = "SELECT m.sender, r.rvalue, DATE_FORMAT(m.date, '%%Y/%%m/%%d')," \
              " DATE_FORMAT(m.date, '%%H:%%i:%%s'), m.subject, r.rid" \
              " from message m, recipientinfo r " \
              "WHERE m.mid = r.mid " \
              "AND MATCH(m.body) AGAINST('%s' IN NATURAL LANGUAGE MODE)" % (search_term)
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            return ()

    def get_message_body_by_email(self, email):

        """Get the message body by email address for clustering"""

        sql = "SELECT m.body "\
              " from message m, recipientinfo r " \
              "WHERE m.mid = r.mid " \
              "AND (r.rvalue = '%s' OR m.sender = '%s')" % (email, email)
        # "ORDER by m.sender, r.rvalue, m.date"
        # take out ordering due to speed issues

        try:
            self.cursor.execute(sql)
        except Exception as e:
            print("DEV: DB ERROR")
            print(e)
            return ()
        return self.cursor.fetchall()

    def get_message_body_by_name(self, first, last):

        """Get the message body by name address, for testing"""
        sql = "SELECT m.body "\
              " from message m, recipientinfo r " \
              "WHERE m.mid = r.mid " \
              "AND (r.rvalue = (SELECT email_id from employeelist where firstName = '%s' and lastName = '%s')" \
              " OR m.sender = (SELECT email_id from employeelist where firstName = '%s' and lastName = '%s'))" % (first, last, first, last)
        # "ORDER by m.sender, r.rvalue, m.date"
        # take out ordering due to speed issues

        try:
            self.cursor.execute(sql)
        except Exception as e:
            print("DEV: DB ERROR")
            print(e)
            return ()
        return self.cursor.fetchall()

    # DEVELOPMENT
    def describe(self, tablename):
        try:
            sql = "DESCRIBE " + str(tablename)
            self.cursor.execute(sql)
            result =  self.cursor.fetchall()
            for line in result:
                print(line)
        except Exception as e:
            print(e)

    def explain(self, statement):
        try:
            sql = "EXPLAIN " + statement
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as e:
            print(e)

    def create_index(self, table, column, text):
        # text has true/false value for text fields(use first 20 chars to index)
        if not text:
            try:
                sql = "CREATE INDEX " + table + "_" + column + " ON " + table + "(" + column + ")"
                result = self.cursor.execute(sql)
                print(result)
            except Exception as e:
                print(e)
        else:
            try:
                sql = "CREATE INDEX " + table + "_" + column + " ON " + table + "(" + column + "(20))"
                result = self.cursor.execute(sql)
                print(result)
            except Exception as e:
                print(e)

    def create_full_text_index(self, column):
        try:
            sql = "CREATE FULLTEXT INDEX full_text_" + column + " ON message(" + column + ")"
            result = self.cursor.execute(sql)
            print(result)
        except Exception as e:
            print(e)

    def show_indexes(self, tablename):
        sql = "SHOW INDEXES FROM " + tablename
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        for line in result:
            print(line)

    def messages(self):
        sql = "SELECT COUNT(*) FROM RECIPIENTINFO"
        self.cursor.execute(sql)
        count = self.cursor.fetchall()
        print(count)
