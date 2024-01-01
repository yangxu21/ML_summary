import fire
from mylib.bot import scrape

if __name__ == "__main__":
    fire.Fire(
        scrape
    )  # a super easy way to make command line tool (instead of using click)
    # python fire-cli.py --name Facebook --length 2
