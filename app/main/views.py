from flask import render_template
from . import main
from ..request import get_sources, get_articles




@main.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """

    general_list = get_sources('us', 'general')
    business_list = get_sources('us', 'business')
    technoloogy_list = get_sources('us', 'technology')
    sports_list = get_sources('us', 'sports')
    health_list = get_sources('us', 'health')
    science_list = get_sources('us', 'science')
    entertainment_list = get_sources('us', 'entertainment')
    test_args = 'Working!'
    return render_template('index.html',
                            test_param=test_args,
                            general=general_list,
                            business=business_list,
                            technology=technoloogy_list,
                            sports=sports_list,
                            health=health_list,
                            science=science_list,
                            entertainment=entertainment_list)


@main.route('/news/<id>')
def news(id):
    """
    View articles page that returns the news article from a highlight
    """
    news_args = get_articles(id)
    highlight_args = 'Route Working!!'
    # name = f'{results_list}'
    return render_template('news.html',
                           highlight_param=highlight_args,
                           news=news_args)
