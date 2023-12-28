#programmed by TaehuaGang

class Server:
    def __init__(self):
        self.q = []

    # 1
    def makeOrder(self, orderNumber, orderList):
        existAlready = False
        for order in self.q:
            if order[0] == orderNumber:
                existAlready = True
        if existAlready == True: 
            return -1
        else:
            tmp = []
            tmp.append(orderNumber)
            tmp.append(orderList)
            self.q.append(tmp)
            return tmp

    # 2
    def getWaitingTime(self, orderNumber, timePerProduct):
        waitingTime = 0
        existFlag = False
        for order in self.q:
            waitingTime += len(order[1]) * timePerProduct
            if order[0] == orderNumber:
                existFlag = True
                break 
        if existFlag == True:
            return waitingTime
        else:
            return -1 

    # 3
    def serveOrder(self):
        orderNumber = self.q[0][0]
        orderList = self.q[0][1] 
        del self.q[0]
        return orderNumber, orderList

    # 4
    def getOrderNumber(self):
        return len(self.q)

    # 5
    def cancelOrder(self, orderNumber):
        orderIndex = -1
        count = 0
        for order in self.q:
            if order[0] == orderNumber:
                orderIndex = count
                break
            count += 1 
        if orderIndex == -1:
            return -1, -1
        else:
            orderNumber = self.q[orderIndex][0]
            orderList = self.q[orderIndex][1]
            del self.q[orderIndex]
            return orderNumber, orderList

    # 6
    def makeOrderVIP(self, orderNumber, orderList):
        existAlready = False
        for order in self.q:
            if order[0] == orderNumber:
                existAlready = True
        if existAlready == True: 
            return -1
        else:
            tmp = []
            tmp.append(orderNumber)
            tmp.append(orderList)
            self.q.insert(0, tmp) 

            tmp = []
            for item in self.q:
                tmp.append(item[0]) 
            return tmp

    # 7
    def giveService(self, orderNumber, serviceProduct):
        orderIndex = -1
        count = 0
        for order in self.q:
            if order[0] == orderNumber:
                orderIndex = count
                break
            count += 1
        if orderIndex == -1:
            return -1, -1
        else:
            orderNumber = self.q[orderIndex][0]
            self.q[orderIndex][1].append(serviceProduct)
            orderList = self.q[orderIndex][1]
            return orderNumber, orderList 

    # 8
    def getOrderItems(self):
        count = 0
        for order in self.q:
            count += len(order[1])
        return count

    
             