import praw
#get_reddit_agent links to my script on reddit
def get_reddit_agent(user_agent, client_id, client_secret, redirect='https://127.0.0.1'):
    reddit_agent = praw.Reddit(client_id = client_id, client_secret = client_secret, user_agent = "Trump's World", username = 'redditbot333', password = 'hotbot333')
    return reddit_agent

if __name__ == '__main__':
    print('If you would like to search a keyword in titles of listed subreddits, enter keyword.')
    print('Otherwise, hit enter without entering anything')
    keyword = input().lower()
    print("Please wait while subreddits are searched")
    client_id = 'gpVF2dKDnikxrA'
    client_secret = 'mQjr46anmuO48UsuXFr-lb4WyPE'
    reddit_agent = get_reddit_agent("Trump's World", client_id, client_secret)
    #list of political subreddits
    trump_subreddits = ['The_Donald', 'EnoughTrumpSpam', 'politics', 'news', 'hillaryclinton', 'worldpolitics', 'Business', 'uspolitics', 'AmericanPolitics', 'Republican']
    #keep track of comments containing Trump
    trump_subs = []
    total_subs = []
    keyword_subs = []
    trump_name = ['trump', 'donald']
    #scroll through subreddits and extract top 100 hot post titles and search
    #for trump or donald keywords in titles and track number of titles
    #containing those keywords
    for subreddit in trump_subreddits:
        trump_titles = [0, subreddit]
        total_titles = [0, subreddit]
        keyword_titles = [0, subreddit]
        for submission in reddit_agent.subreddit(subreddit).hot(limit=100):
            total_titles[0] += 1
            if any(word in submission.title.lower() for word in trump_name):
                trump_titles[0] += 1
            if keyword != '':
                if keyword in submission.title.lower():
                    keyword_titles[0] += 1
        trump_subs.append(trump_titles)
        total_subs.append(total_titles)
        keyword_subs.append(keyword_titles)
    #print results
    for i in range(len(trump_subs)):
        print('Subreddit:', trump_subs[i][1], ':' , 'Donald Trump referenced in', trump_subs[i][0], 'out of', total_subs[i][0], 'submissions')
        if keyword != '':
            print('Subreddit:', keyword_subs[i][1], ': keyword', keyword, 'referenced in', keyword_subs[i][0], 'out of', total_subs[i][0], 'submissions')
