class Twitter:

    def __init__(self):
        self.following = defaultdict(list)
        self.timestamp = 0
        self.tweets = defaultdict(deque)
        # self.feed = defaultdict(list)


    def postTweet(self, userId: int, tweetId: int) -> None:
        if len(self.tweets[userId]) == 10:
            self.tweets[userId].popleft()
        self.tweets[userId].append([self.timestamp, tweetId])
        self.timestamp += 1

        # temp = self.follower[userId] + [userId]
        # for f in temp:
        #     if len(self.feed[f]) < 10:
        #         heapq.heappush(self.feed[f], tweetId)
        #     else:
        #         curr = heapq.heappop(self.feed[f])
        #         heapq.heappush(self.feed[f], max(curr, tweetId))
        # print(self.feed[userId])

        

    def getNewsFeed(self, userId: int) -> List[int]:
        minH = []
        for user in self.following[userId] + [userId]:
            for tweet in self.tweets[user]:
                if len(minH) < 10:
                    heapq.heappush(minH, tweet)
                else:
                    ts, tw = heapq.heappop(minH)
                    if tweet[0]> minH[0][0]:
                        heapq.heappush(minH, tweet)

        

        # return sorted(tweetid for _,tweetid in minH, key = lambda x: x[]0, reverse = True)
        return [tweetid for _, tweetid in sorted(minH, reverse = True)]


        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followeeId not in self.following[followerId] :
            self.following[followerId].append(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)