from rich.console import Console


def show_args(args: tuple[dict[str, str]] | dict[str, str]) -> None:
    c = Console()
    c.print('[bold]ARGUMENTS[/]\n', justify='left', style='#dcbdfb')
    c.print_json(data=args, indent=4)
