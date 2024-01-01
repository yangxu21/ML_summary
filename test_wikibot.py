from mylib.bot import scrape
from wikibot import scrape_cli
from click.testing import CliRunner

def test_scrape():  # testing the function
    assert "Microsoft" in scrape("Microsoft")

def test_wikibot():  # testing the click
    runner = CliRunner()
    result = runner.invoke(scrape_cli, ['--name', 'Microsoft', '--length', '1'])
    assert result.exit_code == 0
    assert 'Microsoft' in result.output