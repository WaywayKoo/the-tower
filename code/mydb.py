class DB:
    def __init__(self):
        self.conn = None
        self.cur = None
        self.title_side = '-'*12

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
        return False

    def open(self):
        """ 開啟資料庫連線
        """
        if self.conn is None:
            import sqlite3
            self.conn = sqlite3.connect('gamett.db')
            self.cur = self.conn.cursor()
        return True

    def close(self):
        """ 關閉資料庫連線
        """
        if self.conn is not None:
            self.conn.close()
            self.conn = None
        return True

    def count_word(self):
        """ 計算單字數
        """
        self.cur.execute("SELECT COUNT(*) FROM WORDS")
        return self.cur.fetchone()[0]

    def get_max_id(self, arg_table):
        """ 取得資料最新編號
        """
        self.cur.execute("SELECT MAX(ID) FROM {}".format(arg_table))
        return self.cur.fetchone()[0] + 1

    def list_all_words(self):
        """ 單字列表
        """
        self.cur.execute("SELECT * FROM WORDS")
        all_rows = self.cur.fetchall()
        for row in all_rows:
            print(row)
        print()

    def generate_dict_words(self):
        """ 設定單字字典
        """
        self.cur.execute("SELECT WORD, DEFINITIONS FROM WORDS")
        all_words = self.cur.fetchall()
        list_words = [dict(WORD=row[0], DEFS=row[1]) for row in all_words]
        return list_words


    def get_player_info(self, account):
        """ 查詢考生資訊
        """
        self.cur.execute("SELECT * FROM PLAYER WHERE ID=?", (account,))
        examinee_info = self.cur.fetchone()
        return examinee_info

    def list_all_gamer(self):
        self.cur.execute("SELECT * FROM PLAYER")
        all_rows = self.cur.fetchall()
        for row in all_rows:
            print(row)
        print()

    def check_if_player_exists(self, arg_account):
        self.cur.execute("SELECT COUNT(*) FROM PLAYER WHERE ID=?", (arg_account, ))
        if self.cur.fetchone()[0] == 1:
            return True
        else:
            return False

    def add_player(self, account_id, action):
        """ 增修player
        """
        data_ok = True
        full_name = input('real name: ')
        if full_name == 'q':
            data_ok  = False

        gender = input('性別(F.女性 M.男性): ').upper()
        if gender == 'F':
            gender = 0
        elif gender == 'M':
            gender = 1
        else:
            data_ok = False

        birth_year = input('生日:(xxxx/xx/xx) ')

        # 資料無誤，准許註冊            
        if data_ok:
            if action == 'insert':
                self.cur.execute("INSERT INTO PLAYER VALUES (?, ?, ?, ?)", 
                    (account_id, full_name, gender, birth_year))
                print('註冊成功，可play')
                self.cur.execute(" INSERT INTO SAVE_FILE VALUES (?, 'item', 'cake', 30)", (full_name,))
                self.cur.execute(" INSERT INTO SAVE_FILE VALUES (?, 'item', 'pie', 20 )", (full_name,))
                self.cur.execute(" INSERT INTO SAVE_FILE VALUES (?, 'item', 'crazy juice', 100 )", (full_name,))
                self.cur.execute(" INSERT INTO SAVE_FILE VALUES (?, 'item', 'banana', 15 )", (full_name,))
                self.cur.execute(" INSERT INTO SAVE_FILE VALUES (?, 'item', 'water', 10 )", (full_name,))
                self.cur.execute(" INSERT INTO SAVE_FILE VALUES (?, 'set', 'layer', 1 )", (full_name,))
            elif action == 'update':
                self.cur.execute("UPDATE PLAYER SET NAME=?, GENDER=?, BIRTH=? WHERE ID=?", 
                    (full_name, gender, birth_year, account_id))
            self.conn.commit()
            print('註冊成功，可play')
            return True
            

        else:
            print ('FAIL')
                        


    def get_basic_all_settings(self):
        self.cur.execute("SELECT ID, VALUE FROM SETTINGS")
        all_settings = self.cur.fetchall()
        return dict(all_settings)

    def get_player_all_settings(self, my_account):
        print(my_account)
        self.cur.execute("SELECT TYPE_NAME, TYPE_VALUE FROM SAVE_FILE WHERE ID = ? AND TYPE = 'item'", (my_account,))
        all_items = self.cur.fetchall()
        return dict(all_items)

    def gc_show_every(self):
        self.cur.execute("SELECT * FROM SAVE_FILE")
        every_player = self.cur.fetchall()
        print(every_player)


    # def list_scores_by_account(self, account):
    #     """ 個人成績查詢
    #     """
    #     account_like = ''.join(('%', account, '%'))
    #     self.cur.execute("SELECT * FROM SCORES WHERE ACCOUNT LIKE ?", (account_like,))
    #     all_rows = self.cur.fetchall()
    #     if len(all_rows) > 0:
    #         for row in all_rows:
    #             print(row)
    #     else:
    #         print(account, '查無任何成績')

    # def score_summary(self):
    #     """ 測驗成績統計
    #     """
    #     print(self.title_side, '測驗人數及平均分數', self.title_side)
    #     self.cur.execute("SELECT TYPE, COUNT(*), AVG(SCORE) FROM SCORES GROUP BY TYPE")
    #     all_rows = self.cur.fetchall()
    #     if len(all_rows) > 0:
    #         for row in all_r