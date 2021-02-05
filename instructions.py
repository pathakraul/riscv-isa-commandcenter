from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown
from rich.text import Text
from rich.panel import Panel
from lib import *

console = Console()

def instruction_add():
    text = Text.assemble( ("add", "bold magenta underline"), (" rd,", "bold red underline"), (" rs1,", "bold blue underline"), (" rs2", "bold yellow underline"), justify="left")
    text.append("\nHELP:", style="bold white")
    text.append("  x[rd] = x[rs1] + x[rs2]", style="bold green")
    text.append("\n♦ Add. R-type, RV32I and RV64I. \n♦ Adds register x[rs2] to register x[rs1] and writes the result to x[rd]. \n♦ Arithmetic overflow is ignored.")
    console.print(text)
    display_R(one="0110011", two="rd", three="000", four="rs1", five="rs2", six="0000000")

def instruction_addi():
    text = Text.assemble( ("addi", "bold magenta underline"), (" rd,", "bold red underline"), (" rs1,", "bold blue underline"), (" immediate", "bold yellow underline"), justify="left")
    text.append("\nHELP:", style="bold white")
    text.append("  x[rd] = x[rs1] + sext(immediate)", style="bold green")
    text.append("\n♦ Add Immediate. I-type, RV32I and RV64I. \n♦ Adds the sign-extended immediate to register x[rs1] and writes the result to x[rd]. \n♦ Arithmetic overflow is ignored.")
    console.print(text)
    display_I(one="0010011", two="rd", three="000", four="rs1", five="imm[11:0]")

def instruction_addiw():
    text = Text.assemble( ("addiw", "bold magenta underline"), (" rd,", "bold red underline"), (" rs1,", "bold blue underline"), (" immediate", "bold yellow underline"), justify="left")
    text.append("\nHELP:", style="bold white")
    text.append("  x[rd] = sext((x[rs1] + sext(immediate))[31:0]", style="bold green")
    text.append("\n♦ Add Word Immediate. I-type, RV64I only. \n♦ Adds the sign-extended immediate to x[rs1], truncates the result to 32 bits, \n  and writes the sign-extended result to x[rd].  \n♦ Arithmetic overflow is ignored.")
    console.print(text)
    display_I(one="0011011", two="rd", three="000", four="rs1", five="imm[11:0]")

def instruction_addw():
    text = Text.assemble( ("addw", "bold magenta underline"), (" rd,", "bold red underline"), (" rs1,", "bold blue underline"), (" rs2", "bold yellow underline"), justify="left")
    text.append("\nHELP:", style="bold white")
    text.append("  x[rd] = sext((x[rs1] + x[rs2])[31:0])", style="bold green")
    text.append("\n♦ Add Word. R-type, RV64I only. \n♦ Adds register x[rs2] to register x[rs1], truncates the result to 32 bits, \n  and writes the signextended result to x[rd]. \n♦ Arithmetic overflow is ignored.")
    console.print(text)
    display_R(one="0111011", two="rd", three="000", four="rs1", five="rs2", six="0000000")


def instruction_and():
    text = Text.assemble( ("and", "bold magenta underline"), (" rd,", "bold red underline"), (" rs1,", "bold blue underline"), (" rs2", "bold yellow underline"), justify="left")
    text.append("\nHELP:", style="bold white")
    text.append("  x[rd] = x[rs1] & x[rs2]", style="bold green")
    text.append("\n♦ AND. R-type, RV32I and RV64I. \n♦ Computes the bitwise AND of registers x[rs1] and x[rs2] and writes the result to x[rd]. \n♦ Compressed form: c.and rd, rs2.")
    console.print(text)
    display_R(one="011011", two="rd", three="111", four="rs1", five="rs2", six="0000000")

def instruction_andi():
    text = Text.assemble( ("andi", "bold magenta underline"), (" rd,", "bold red underline"), (" rs1,", "bold blue underline"), (" immediate", "bold yellow underline"), justify="left")
    text.append("\nHELP:", style="bold white")
    text.append("  x[rd] = x[rs1] & sext(immediate)", style="bold green")
    text.append("\n♦ AND Immediate. I-type, RV32I and RV64I. \n♦ Computes the bitwise AND of the sign-extended immediate and register x[rs1] and writes the result to x[rd]. \n♦ Compressed form: c.andi rd, imm.")
    console.print(text)
    display_R(one="0010011", two="rd", three="111", four="rs1", five="imm[11:0]")

def instruction_auipc():
    text = Text.assemble( ("auipc", "bold magenta underline"), (" rd,", "bold red underline"), (" immediate,", "bold blue underline"), justify="left")
    text.append("\nHELP:", style="bold white")
    text.append("  x[rd] = pc + sext(immediate[31:12] << 12)", style="bold green")
    text.append("\n♦ Add Upper Immediate to PC. U-type, RV32I and RV64I. \n♦ Adds the sign-extended 20-bit immediate, left-shifted by 12 bits, to the pc, and writes the result to x[rd].")
    console.print(text)
    display_R(one="0010111", two="rd", three="imm[31:12]")