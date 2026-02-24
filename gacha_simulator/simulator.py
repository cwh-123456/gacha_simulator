from random import randint

class Simulator:
    '''简易的抽卡模拟器'''

    def __init__(self, pink_ball):
        '''初始化各项抽卡数据'''
        #资源与结果
        self.num = pink_ball
        self.remain = pink_ball
        self.result = []

        #各项概率
        self.basis = 0.006
        self.rise = 0.06
        self.odds = self.basis
        self.capture_base = 0.55
        self.change_odds()

        #保底机制相关
        self.wai = 0

        #捕获明光机制相关
        self.lianwai = 0

        self.gacha()

    def __str__(self):
        '''输出结果'''
        s = ''
        for i in self.result:
            kind, is_capture, sum = i
            s += f'{kind:<3} {is_capture:<7} {sum:<3} \n'
        s += f'还剩{self.remain}抽'
        return s

    def change_odds(self):
        '''为了便于模拟，将各项概率分别扩大若干倍'''
        self.basis *= 1000
        self.rise *= 1000
        self.odds *= 1000
        self.capture_base *= 100

    def gacha(self):
        '''开始抽卡'''
        while self.num:
            self.odds = self.basis
            for i in range(1, 91):
                if self.num == 0:
                    break
                self.num -= 1
                if i > 73:
                    self.odds += self.rise
                if randint(1, 1000) <= self.odds:
                    if self.lianwai == 3:
                        self.lianwai = 0
                        self.result.append(['限定', '捕获明光     ', i])
                    else:
                        if randint(1, 100) <= self.capture_base:
                            self.lianwai = 0
                            self.result.append(['限定', '小保底       ', i])
                        else:
                            self.wai = 1
                            self.lianwai += 1
                            self.result.append(['常驻', '小保底（歪）', i])
                    
                    self.remain -= i
                    break
            if self.wai:
                self.odds = self.basis
                for i in range(1, 91):
                    if self.num == 0:
                        break
                    self.num -= 1
                    if i > 73:
                        self.odds += self.rise
                    if randint(1, 1000) <= self.odds:
                        self.wai = 0
                        self.result.append(['限定', '大保底       ', i])
                        self.remain -= i
                        break


if __name__ == '__main__':
    sim = Simulator(500)
    print(sim)
