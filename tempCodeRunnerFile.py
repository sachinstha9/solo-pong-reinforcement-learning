
        if (self.ballPosition[0] + (self.ballSize / 2) > self.paddlePosition[0] and self.ballPosition[0] - (self.ballSize / 2) < self.paddlePosition[0] + self.paddleWidth) and (self.ballPosition[1] + (self.ballSize / 2) >= self.paddlePosition[1]):
            reward = 10
        
        if self.ballPosition[1] > HEIGHT: