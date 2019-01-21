import click
from datetime import datetime

@click.group()
def main():
        """
        Welcome to comment mockup section
        """
        

@main.command()
def create_comment(message, author, timestamp):
	pass

@main.command()
def edit_comment(message, author, timestamp):
      pass 

@main.command()
def delete_comment(message, author, timestamp):
      pass   

    

if __name__ == '__main__':
	main()
