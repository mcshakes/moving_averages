from nltk.sentiment.vader import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()


class VaderScore:
    def __init__(self):
        pass

    def compound_vader_scores(self, news):
        cs = []
        for row in range(len(news)):
            cs.append(analyzer.polarity)

            cs.append(analyzer.polarity_scores(
                news['title'].iloc[row])['compound'])

        news['compound_vader_score'] = cs
        news = news[(news[['compound_vader_score']] != 0).all(
            axis=1)].reset_index(drop=True)

        return news.head()
