class Twitter:

    def __init__(self):
        self.followers = defaultdict(list)
        self.posts = defaultdict(list)
        self.timer = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.timer, tweetId))
        self.timer += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        # O(m * n)
        following = self.followers[userId]
        main_list = list(self.posts[userId])
        print(self.posts[userId])

        for acc in following:
            main_list += self.posts[acc]
        
        sort_list = sorted(main_list, key=lambda x: -x[0])
        

        return [c[1] for c in sort_list[0:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followers[followerId]:
            self.followers[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # O(n)
        for i in range(len(self.followers[followerId])):
            if self.followers[followerId][i] == followeeId:
                del self.followers[followerId][i]


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)