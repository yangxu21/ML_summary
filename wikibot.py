import wikipedia
import click

@click.command()
@click.option('--name',prompt='Wikipedia page to scrape',
              help='Web page we want to scrape')

def scrape(name="Microsoft", length=1):
    results = wikipedia.summary(name, sentences=length)
    click.echo(click.style(f"{results}:", fg="red", bg="white"))

if __name__=='__main__': #it will only run if it is run as a script
    scrape()
