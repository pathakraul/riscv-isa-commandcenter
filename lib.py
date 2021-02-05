import os
import sys
import argparse
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown
from rich.text import Text
from rich.panel import Panel

console = Console()

def display_R(one="opcode", two="rd", three="funct3", four="rs1", five="rs2", six="funct7"):
    table = Table(title="R-Type", show_header=True, header_style="bold magenta", title_style="white")
    table.add_column("31:25(7)", width=24, justify="center")
    table.add_column("24:20(5)", width=11, justify="center")
    table.add_column("19:15(5)", width=10, justify="center")
    table.add_column("14:12(3)", width=10, justify="center")
    table.add_column("11:07(5)", width=23, justify="center")
    table.add_column("06:00(7)", width=14, justify="center")
    table.add_row(six, five, four, three, two, one)
    console.print(table) 

def display_I(one="opcode", two="rd", three="funct3", four="rs1", five="imm[11:0]"): 
    table = Table(title="I-Type", show_header=True, header_style="bold magenta", title_style="white")
    table.add_column("31:20(12)", width=38, justify="center")
    table.add_column("19:15(5)", width=10, justify="center")
    table.add_column("14:12(3)", width=10, justify="center")
    table.add_column("11:07(5)", width=23, justify="center")
    table.add_column("06:00(7)", width=14, justify="center")
    table.add_row(five, four, three, two, one)
    console.print(table)

def display_S(one="opcode", two="imm[4:0]", three="funct3", four="rs1", five="rs2", six="imm[11:5]"): 
    table = Table(title="S-Type", show_header=True, header_style="bold magenta", title_style="white")
    table.add_column("31:25(7)", width=23, justify="center")
    table.add_column("24:20(5)", width=12, justify="center")
    table.add_column("19:15(5)", width=10, justify="center")
    table.add_column("14:12(3)", width=10, justify="center")
    table.add_column("11:07(5)", width=23, justify="center")
    table.add_column("06:00(7)", width=14, justify="center")
    table.add_row(six, five, four, three, two, one)
    console.print(table)

def display_U(one="opcode", two="rd", three="imm[31:12]"): 
    table = Table(title="U-Type", show_header=True, header_style="bold magenta", title_style="white")
    table.add_column("31:12(20)", width=64, justify="center")
    table.add_column("11:07(5)", width=23, justify="center")
    table.add_column("06:00(7)", width=14, justify="center")
    table.add_row(three, two, one)
    console.print(table)

def display_B(one="opcode", two="imm[11]", three="imm[4:1]", four="funct3", five="rs1", six="rs2", seven="imm[10:5]", eight="imm[5]"): 
    table = Table(title="B-Type", show_header=True, header_style="bold magenta", title_style="white")
    table.add_column("31:31(1)", width=10, justify="center")
    table.add_column("30:25(6)", width=10, justify="center")
    table.add_column("24:20(5)", width=12, justify="center")
    table.add_column("19:15(5)", width=10, justify="center")
    table.add_column("14:12(3)", width=10, justify="center")
    table.add_column("11:08(4)", width=10, justify="center")
    table.add_column("07:07(1)", width=10, justify="center")
    table.add_column("16:00(7)", width=14, justify="center")
    table.add_row(eight, seven, six, five, four, three, two, one)
    console.print(table)

def display_J(one="opcode", two="rd", three="imm[19:12]", four="imm[11]", five="imm[10:1]", six="imm[20]"): 
    table = Table(title="J-Type", show_header=True, header_style="bold magenta", title_style="white")
    table.add_column("31:31(1)", width=10, justify="center")
    table.add_column("30:21(10)", width=13, justify="center")
    table.add_column("20:20(1)", width=9, justify="center")
    table.add_column("19:12(8)", width=23, justify="center")
    table.add_column("11:07(5)", width=23, justify="center")
    table.add_column("06:00(7)", width=14, justify="center")
    table.add_row(six, five, four, three, two, one)
    console.print(table)