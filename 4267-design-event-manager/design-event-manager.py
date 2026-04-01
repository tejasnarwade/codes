import heapq
class EventManager:

    def __init__(self, events: list[list[int]]):
        self.priorities = {eid:prio for eid , prio in events}
        self.pq = [(-prio, eid) for eid, prio in events]
        heapq.heapify(self.pq)
        
        

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        self.priorities[eventId]=newPriority
        heapq.heappush(self.pq,(-newPriority,eventId))
        

    def pollHighest(self) -> int:
        while self.pq:
            neg_prio, eid = heapq.heappop(self.pq)
            prio = -neg_prio
            if eid in self.priorities and self.priorities[eid]==prio:
                del self.priorities[eid]
                return eid
        return -1
        


# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()