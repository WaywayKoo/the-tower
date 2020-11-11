import time
import random
from mydb import DB

class Game:
    def __init__(self):
        self.menu_title = 'The Tower: --'  
        self.account = ''
        self.islogin = False
        self.all_items = ''
        self.all_settings = db.get_basic_all_settings()
        self.hh = self.all_settings['player_h']
        self.b1_hh = self.all_settings['b1_h']
        self.b2_hh = 100000000000000
        self.menu = {
            'a':'登入',
            'b':'註冊',
            'c':'遊玩',
            'q':'離開',
        }
        self.menu_func = {
            'a': lambda c, s: self.login(c, s),
            'b': lambda c, s: self.make_acc(c, s),
            'c': lambda c, s: self.start_game(),
            'q': lambda c, s: self.show_words_randomly(c, s),
        }
        self.divider = '='*20

    def start_game(self):
        if self.islogin:
            print('|')
            print('|')
            print('|')
            print('|')
            print('|')
            print('|')
            print('|')
            print('+=========================+')
            if self.boss_1():
                self.boss_2()

        else:
            print('Login First')

    def login(self, db, func_title):
        """ 登入
        """
        account_input = input('請輸入帳號: ')
        if db.check_if_player_exists(account_input):
            self.account = account_input
            print(db.get_player_info(self.account))
            self.islogin = True
            self.all_stuff = db.get_player_all_settings(self.account)
        else:
            print('LOGIN IN FAIL')
            self.islogin =  False

    def make_acc(self, db, func_title):
        account_input = input('請輸入帳號: ')
        db.add_player(account_input, 'insert')

    def show_menu(self):
        """ 主選單
        """
        print(self.divider)
        if self.account == '':
            print(self.menu_title, '尚未登入')
        else:
            print(self.menu_title, self.account)
        print(self.divider)
        for fid, fname in self.menu.items():
            print('%s:%s' % (fid, fname))
        print(self.divider)
        opt = input('請選擇: ').lower()
        if opt in self.menu.keys():
            return opt, self.menu[opt]
        else:
            return '', '無此功能！'

    def start(self):
        print("Welcome to the TOWER!~~\n")
        time.sleep(2)
        print("You are a warrior, you goal is to kill the FINAL BOSS\n")
        time.sleep(2)
        print("But before you fight the BOSS\nYou will need to fight or to solve a lot of things or BOSS\n\n")

    def check(self):
        print('CHECK:\n')
        print ('++++++++++++++++++++++++')
        print('YOU:')
        print ('Your attack damage:', self.all_settings['atkp'])
        print('Your Armor: ', self.all_settings['defp'])
        print ('++++++++++++++++++++++++')
        print ('BOSS health: ', self.b1_hh)
        print ('BOSS attack damage: ', self.all_settings['b1_atk'])
        print ('BOSS armor: ', self.all_settings['b1_def'])
        print ('++++++++++++++++++++++++')
        print('\n')
        time.sleep(5)

    def battle(self):
        print("===================")
        print ("Health: {}\n" .format(self.hh))
        # print ("Mana: {}\n" .format(self.hh))
        # print ("Layer: %s" %self.all_stuff['layer'])
        print("===================")
        print("1 -- Pysical Attack")
        print("2 -- Magic Attack")
        print("3 -- Item")
        print("4 -- Computer")
        print("5 -- Check")
        print("6 -- Stop")
        print("===================")
        choice = input('')
        if choice.isdigit():    
            choice = int(choice)
            if choice == 1:
                self.fight_p()
            elif choice == 2:
                self.fight_m()
            elif choice == 3:
                self.item()
            elif choice == 4:
                self.computer()
            elif choice == 5:
                self.check()
            elif choice == 6:
                self.stop_game()
        else:
            print("???? I DON'T GET  IT ????")       

    def fight_p(self):
        list_cr = ['no', 'no', 'no', 'no', 'no', 'cr']
        cr = random.choice(list_cr)
        if cr == 'cr':
            dama = self.all_settings['atkp'] * 2.5
            print('Critical Strike')
        elif cr == 'no':
            dama = random.randint(self.all_settings['atkp'] - 3, self.all_settings['atkp'] + 3)
        self.b1_hh = self.b1_hh - (dama - self.all_settings['b1_def'])
        print('BOSS health:', self.b1_hh)
        print('You deal:', dama)

    def fight_m(self):
        dama = self.all_settings['matkp'] * 1.5
        if dama >= 0:
            dama = 1
        self.b1_hh = self.b1_hh - (dama - self.all_settings['b1_def'])
        print('BOSS health:', self.b1_hh)
        print('You deal:', dama)

    def item(self):
        print("===================")
        for key, val in self.all_stuff.items():
            print('{}:{}'.format(key, val))
        print("===================")
        it_c = input('What\'s your choice \n')
        if it_c ==  'cake' and 'cake' in self.all_stuff.keys():
            self.hh = self.hh + self.all_stuff['cake']
            del self.all_stuff['cake']
        elif it_c == 'water' and 'water' in self.all_stuff.keys():
            self.hh = self.hh + self.all_stuff['water']
            del self.all_stuff['water']
        elif it_c == 'pie' and 'pie' in self.all_stuff.keys():
            self.hh = self.hh + self.all_stuff['pie']
            del self.all_stuff['pie']
        elif it_c == 'crazy juice' and 'crazy juice' in self.all_stuff.keys():
            self.hh = self.hh + self.all_stuff['crazy juice']
            del self.all_stuff['crazy juice']
        elif it_c == 'banana' and 'banana' in self.all_stuff.keys():
            self.hh = self.hh + self.all_stuff['banana']
            del self.all_stuff['banana']
        else:
            print("you didn't have that thing")
        if self.hh >= 200:
            self.hh = 200

    def boss_1(self):
        time.sleep(2)
        print("You met an ape with sword")
        time.sleep(1)
        print("seems like a weak monster")
        time.sleep(1)
        while True:
            if self.hh <= 0:
                break
            elif self.b1_hh <= 0:
                break
            self.battle()
            self.b_dama()
            continue
        return True

    def boss_2(self):
        print("You met a ghost, attack doesn't work on him")
        print("Ghost: CHYN CQRB OXA CQN FRW")
        ans_2 = 'TYPE THIS FOR THE WIN'
        while True:
            if self.hh <= 0:
                break
            elif self.b2_hh <= 0:
                break
            ans_player = input('WHAT IS THE GHOST SAYING?????')
            if ans_player == ans_2:
                print('BOSS IS DEAD')
                self.b2_hh = -10000000000000
            self.b_dama()
            continue

    def b_dama(self):
        self.all_settings['b1_def'] = random.randint(self.all_settings['b1_atk'] - 3, self.all_settings['b1_atk'] + 3)
        BB_D = self.all_settings['b1_def'] - self.all_settings['defp']
        self.hh = self.hh - (self.all_settings['b1_def'] - self.all_settings['defp'])
        print('The Boss deal {} damage to you'.format (BB_D))

        
    def computer(self):
        def encrypt():
            the_num = str(input('encrypt: \n'))
            ans_number = []
            key = int(input('input a key\n'))
            for i in range(len(the_num)):
                if the_num[i].isalpha() == True:
                    connect = alphabet.find(the_num[i].lower())
                    ans = (connect + key) % 26
                    ans_number.append(alphabet[ans])
                    final = (''.join(ans_number))
                else:
                    ans_number.append(the_num[i]) 
            print(final.upper())
        def decrypt():
            the_num = str(input('input a string\n'))
            ans_number = []
            key = int(input('input a key\n'))
            for i in range(len(the_num)):
                if the_num[i].isalpha() == True:
                    connect = alphabet.find(the_num[i].lower())
                    ans = (connect - key) % 26
                    ans_number.append(alphabet[ans])
                    final = (''.join(ans_number))
                else:
                    ans_number.append(the_num[i]) 
            print(final.upper())
        def brutal_de():
            the_num = str(input('input a string\n'))
            for j in range (26):
                ans_number = []
                for i in range(len(the_num)):
                    if the_num[i].isalpha() == True:
                        connect = alphabet.find(the_num[i].lower())
                        ans = (connect - j) % 26
                        ans_number.append(alphabet[ans])
                        final = (''.join(ans_number))
                    else:
                        ans_number.append(the_num[i]) 
                print("Key {}:  {}".format( j, final.upper()))
        import random
        t1 = 0
        t2 = 0
        t3 = 0
        while True:
            print('\n')
            print('YOU CAN ENCRYPT AND DCRYPT THINGS FORM THIS COMPUTER\n')
            alphabet = 'abcdefghijklmnopqrstuvwxyz'
            choose = str(input('1:encrypt 2:decrypt 3:brutal e:exit\n'))
            if choose == '1':
                t1 = t1 + 1
                encrypt()
            elif choose == '2':
                t2 = t2 + 1
                decrypt()
            elif choose == '3':
                t3 = t3 + 1
                brutal_de()
                continue
            elif choose == 'e':
                break
        print ('encrypt time：{}'.format(t1))
        print ('decrypt time：{}'.format(t2))
        print ('brutal time：{}'.format(t3))
            


with DB() as db:
    player = Game()
    while True:
        func_id, func_name = player.show_menu()
        if func_id == 'q':
            break
        elif func_id == '':
            print(func_name)
        else:
            player.menu_func[func_id](db, func_name)
        print()