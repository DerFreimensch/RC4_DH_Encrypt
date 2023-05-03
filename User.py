import random
import Deffie_Hellman as DH
import Global


class User:

    def __int__(self, num: int):
        self.user_id = Global.users[num]
        self.secure_key = random.randint(10, 50)
        self.open_key = DH.G**self.secure_key//DH.P
        del Global.users[num]
        print(f"Создан пользователь с ID: {self.user_id}")

    def send_key(self,  user_id_rec):
        pass

    def __str__(self):
        return str(self.user_id)
