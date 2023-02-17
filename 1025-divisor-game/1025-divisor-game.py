class Solution:
    def divisorGame(self, n: int) -> bool:
        return n%2==0

    # 1->lose(n=1, we can't choose anything)
    # 2->win
    # 3->lose
    # 4->win   if u see, even count takes win event and odd takes lose event
    # 5->lose
    # 6->win
    