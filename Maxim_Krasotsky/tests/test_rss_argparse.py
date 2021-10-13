"""checks the functions of the rss_argparse module"""

from rss_package import parse_args


def test_parse_args_no_url():
    """checks the value of the arguments if you do not pass the link"""
    args = parse_args(["--version"])
    assert not args.source
    assert not args.limit
    assert args.version
    assert not args.verbose
    assert not args.json


def test_parse_args_no_arguments():
    """checks the value of the arguments if no arguments are passed"""
    url = 'https://news.yahoo.com/rss/'
    args = parse_args([url])
    assert args.source
    assert not args.limit
    assert not args.version
    assert not args.verbose
    assert not args.json


def test_parse_args_one_argument():
    """checks the value of the arguments if one argument are passed"""
    url = 'https://www.kommersant.ru/RSS/news.xml'
    args = parse_args([url, "--json"])
    assert args.source
    assert not args.limit
    assert not args.version
    assert not args.verbose
    assert args.json


def test_parse_args_two_arguments():
    """checks the value of the arguments if two argument are passed"""
    url = 'https://lenta.ru/rss'
    args = parse_args([url, "--json", "--version"])
    assert args.source
    assert not args.limit
    assert args.version
    assert not args.verbose
    assert args.json


def test_parse_args_three_arguments():
    """checks the value of the arguments if three argument are passed"""
    url = 'https://www.vesti.ru/vesti.rss'
    args = parse_args([url, "--limit", "100", "--verbose", "--json"])
    assert args.source
    assert args.limit == 100
    assert not args.version
    assert args.verbose
    assert args.json


def test_parse_args_all_arguments():
    """checks the value of the arguments if all argument are passed"""
    url = 'https://people.onliner.by/feed'
    args = parse_args([url, "--limit", "101010", "--verbose", "--json", "--version"])
    assert args.source
    assert args.limit == 101010
    assert args.version
    assert args.verbose
    assert args.json
