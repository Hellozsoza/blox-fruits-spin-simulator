import tkinter
import customtkinter
import os
import random as R
from PIL import Image

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

HEIGHT = 450
WIDTH = 650

def openFile1(file_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    script_dir.replace('\\','/')
    file_path = os.path.join(script_dir, file_name)
    file_path.replace('\\','/')
    return file_path

def openFile(file_name):
   script_dir = os.path.dirname(os.path.abspath(__file__))
   script_dir.replace('\\','/')
   file_path = os.path.join(script_dir, file_name)
   file_path.replace('\\','/')
   return file_path

path = os.path.dirname(os.path.abspath(__file__))
kitsuneico = openFile1("KitsuneFruit.ico")

root = customtkinter.CTk()
root.title("Blox Fruit Spin Simulator V2")
root.geometry((f"{WIDTH}x{HEIGHT}"))
root.resizable(False, False)
root.wm_iconbitmap(kitsuneico)

fruits = ["RocketFruit.png", "SpinFruit.png", "ChopFruit.png", "SpringFruit.png", "BombFruit.png", "SmokeFruit.png", "SpikeFruit.png", "FlameFruit.png", "FalconFruit.png", "IceFruit.png", "SandFruit.png", "DarkFruit.png", "DiamondFruit.png", "LightFruit.png", "RubberFruit.png", "BarrierFruit.png", "GhostFruit.png", "MagmaFruit.png", "QuakeFruit.png", "BuddhaFruit.png", "LoveFruit.png", "SpiderFruit.png", "SoundFruit.png", "PhoenixFruit.png", "PortalFruit.png", "RumbleFruit.png", "PainFruit.png", "BlizzardFruit.png", "GravityFruit.png", "MammothFruit.png", "TrexFruit.png", "DoughFruit.png", "ShadowFruit.png", "VenomFruit.png", "ControlFruit.png", "SpiritFruit.png", "DragonFruit.png", "LeopardFruit.png", "kitsune.png"]

def spin(fruits):
    fruit = R.choice(fruits)
    return fruit

def changeShownFruit(shownFruit, fruit):
    shownFruit.configure(image=customtkinter.CTkImage(Image.open(openFile(fruit)), size=(177, 180)))

Frame1 = customtkinter.CTkFrame(master=root, border_width=10)
Frame1.place(x=47, y=145)

shownFruit = customtkinter.CTkLabel(
    master=root,
    bg_color=[
        'gray86',
        'gray17'],
    image=customtkinter.CTkImage(
        Image.open(openFile("BarrierFruit.png")),
        size=(
            174,
            174)),
    compound="center",
    height=30,
    text="")
shownFruit.place(x=62, y=158)

Label1 = customtkinter.CTkLabel(
    master=root,
    width=80,
    font=customtkinter.CTkFont(
        'Nerko One',
        size=39,
        weight='bold'),
    height=30,
    text="Your Fruit")
Label1.place(x=57, y=76)

Button1 = customtkinter.CTkButton(
    master=root,
    font=customtkinter.CTkFont(
        'Nerko One',
        size=42,
        weight='bold'),
    width=211,
    height=68,
    text="Spin",
    command=lambda: changeShownFruit(shownFruit=shownFruit, fruit=spin(fruits=fruits)),
    fg_color="#14af75",
    hover_color="#0a6d5f",
    text_color=[
        'gray98',
        '#DCE4EE'],
    text_color_disabled=[
        'gray78',
        'gray68'])
Button1.place(x=373, y=293)

root.mainloop()