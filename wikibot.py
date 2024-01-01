from mylib.bot import scrape
import click

@click.command()
@click.option('--name',prompt='Wikipedia page to scrape',
              help='Web page we want to scrape')
@click.option('--length',
              help='The length of the output')
def scrape_cli(name, length):
    results = scrape(name, length)
    click.echo(click.style(f"{results}:", fg="red", bg="white"))

if __name__=='__main__': #it will only run if it is run as a script
    scrape_cli()
