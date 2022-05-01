import tools 
#Now we support:
#tools.downAuthor_All(id):download all the pictures for a specific author
#tools.downRankings_top30(date,mode,content):download top30 pictures in the rankings
#e.g. date: 20220430
#mode: 'daily', 'weekly', 'monthly', 'rookie', 'original', 'male', 'female'
#content: '插画'，'all'

#Examples:
tools.downRankings_top30(20220430,'daily','插画')