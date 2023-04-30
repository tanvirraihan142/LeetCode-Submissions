class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        n = len(player1)
        score_player1 = 0
        score_player2 = 0
        
        for i in range(n):
            if i>=2 and (player1[i-1]==10 or player1[i-2]==10):
                score_player1 += 2*player1[i]
            elif i==1 and player1[i-1]==10:
                score_player1 += 2*player1[i]
            else:
                score_player1 += player1[i]
                
            if i>=2 and (player2[i-1]==10 or player2[i-2]==10):
                score_player2 += 2*player2[i]
            elif i==1 and player2[i-1]==10:
                score_player2 += 2*player2[i]
            else:
                score_player2 += player2[i]
                
        if score_player1 > score_player2:
            return 1
        elif score_player2 > score_player1:
            return 2
        else:
            return 0