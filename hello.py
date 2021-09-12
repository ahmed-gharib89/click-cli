#!/usr/bin/env python
# -*- coding: utf-8 -*-
import click
import glob


# Command line tool to search for files by type
@click.command()
# Option to specify the file path
@click.option(
    "--path",
    default=".",
    prompt="Enter the file path to search in!",
    help="Path to search for files",
)
# Option to specify the file type
@click.option(
    "--ftype",
    default="*",
    prompt="Enter the file type to search for!",
    help="File type to search for",
)
def search(path, ftype):
    """
    Search for files by type
    """
    # Get all files in the path
    files = glob.glob(path + "/*." + ftype)
    click.echo(click.style("Found matches:", fg="red"))
    # Print the files
    for file in files:
        click.echo(click.style(file, bg="white", fg="black"))


if __name__ == "__main__":
    search()
