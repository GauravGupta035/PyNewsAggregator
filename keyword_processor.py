try:
    from GoogleNews import GoogleNews
    from newspaper import Article
    import datetime
    import re
except:
    print("missing module/s: GoogleNews and/or datetime")


def get_age(x):
    """returns age in minutes"""
    x = x.split()
    age = int(x[0])
    # print(x[1])
    if re.search('min', x[1], re.IGNORECASE):
        return age
    elif re.search('hour', x[1], re.IGNORECASE):
        return age * 60
    elif re.search('day', x[1], re.IGNORECASE):
        return age * 24 * 60
    return 0


class KeywordProcessor:
    def __init__(self, keyword):
        self.keyword = keyword

    def fetch_links(self):
        try:
            to_date = datetime.datetime.now()
            from_date = to_date - datetime.timedelta(days=1)

            to_date = str(to_date.month) + '/' + str(to_date.day) + '/' + str(to_date.year)
            from_date = str(from_date.month) + '/' + str(from_date.day) + '/' + str(from_date.year)

            google_news = GoogleNews()

            google_news.setlang('en')
            google_news.setTimeRange(from_date, to_date)

            google_news.search(self.keyword)

            return google_news.result()
        except:
            return ''

    def display_links(self):
        try:
            for link in self.fetch_links():
                print(link.get('link', ''))
        except:
            pass

    def most_relevant(self):
        """returns most relevant article"""
        pattern = ''
        for keyword in self.keyword.split():
            pattern = pattern + keyword + '|'
        pattern = pattern[:len(pattern) - 1]
        # print(pattern)
        max_matches = 0
        most_relevant_site = ''
        min_age = 24 * 60  # needs to be updated according to mailing frequency
        for link in self.fetch_links():
            try:
                article = Article(link.get('link', ''))
                article.download()
                article.parse()
                matches = re.findall(pattern, article.text, re.IGNORECASE)
                matches = set([x.casefold() for x in matches])
                try:
                    age = get_age(link.get('date', ''))
                except:
                    pass
                print('Current article age:', age, 'mins\nBest article age:', min_age, 'mins\nMatches:', matches,
                      '\nLink:', link.get('link', ''), '\n')
                if len(matches) >= max_matches and age <= min_age:
                    max_matches = len(matches)
                    min_age = age
                    most_relevant_site = link.get('link', '')
            except:
                pass
        most_relevant_article = Article(most_relevant_site)
        most_relevant_article.download()
        most_relevant_article.parse()
        return most_relevant_article
