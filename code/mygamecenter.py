
from mydb import DB

class Gcenter:
    def __init__(self):
        self.menu_title = 'Game Center'
        self.menu = {
            'a':'參測玩家列表',
            'b':'玩家設定列表',
            'c':'個人成績查詢',
            'q':'離開',
        }
        self.menu_func = { 
            'a': lambda c, s: self.show_player(c, s),
            'b': lambda c, s: self.search_set(c, s),
        }
        self.divider = '='*20
    def search_set(self, db, func_title):
        all_settings = db.gc_show_everyw()
        print(all_settings)

    def show_menu(self):
        print(self.divider)
        print(self.menu_title)
        print(self.divider)
        for fid, fname in self.menu.items():
            print('%s:%s' % (fid, fname))
        print(self.divider)
        opt = input('請選擇: ').lower()
        if opt in self.menu.keys():
            return opt, self.menu[opt]
        else:
            return '', '無此功能！'

    def show_player(self, db, func_title):
        """ 參測考生列表
        """
        db.list_all_gamer()
        return func_title

    def score_list(self, db, func_title):
        """ 個人成績查詢
        """
        while True:
            qaccount = input('請輸入帳號 (exit.離開): ')
            if qaccount == 'exit':
                break
            db.list_scores_by_account(qaccount)
        return func_title    

# entry point
with DB() as db:
    player = Gcenter()
    while True:
        func_id, func_name = player.show_menu()
        if func_id == 'q':
            break
        elif func_id == '':
            print(func_name)
        else:
            player.menu_func[func_id](db, func_name)
        print()
